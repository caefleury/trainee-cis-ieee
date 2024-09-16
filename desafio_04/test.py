import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from imblearn.over_sampling import SMOTE
from scipy.special import expit
import matplotlib.pyplot as plt

file_path = 'desafio_04/creditcard.ipynb'
credit_card = pd.read_csv(file_path, sep=',', on_bad_lines='skip', low_memory=False)

print(credit_card.info())
print(credit_card.isnull().sum())

# Definição da camada da rede neural
class NeuralLayer:
    def __init__(self, input_size, neuron_count):
        self.weights = np.random.randn(input_size, neuron_count) * 0.01
        self.biases = np.zeros((1, neuron_count))

    def forward(self, inputs):
        self.input = inputs
        self.output = np.dot(inputs, self.weights) + self.biases

    def backward(self, gradient, learning_rate):
        self.dweights = np.dot(self.input.T, gradient) / self.input.shape[0]
        self.dbiases = np.sum(gradient, axis=0, keepdims=True) / self.input.shape[0]
        self.weights -= learning_rate * self.dweights
        self.biases -= learning_rate * self.dbiases
        self.dinput = np.dot(gradient, self.weights.T)

# Funções de ativação
class ReLUActivation:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

    def backward(self, gradient):
        self.dinput = gradient.copy()
        self.dinput[self.output <= 0] = 0

class SigmoidActivation:
    def forward(self, inputs):
        self.output = expit(inputs)
        
    def backward(self, gradient):
        self.dinput = gradient * (self.output * (1 - self.output))

# Função de perda
class BinaryCrossEntropyLoss:
    def calculate(self, predictions, targets):
        predictions = np.clip(predictions, 1e-7, 1 - 1e-7)
        return -np.mean(targets * np.log(predictions) + (1 - targets) * np.log(1 - predictions))

    def backward(self, predictions, targets):
        predictions = np.clip(predictions, 1e-7, 1 - 1e-7)
        return (predictions - targets) / (predictions * (1 - predictions))
    
# Carregar e preparar os dados
def load_and_prepare_data(file_path):
    data_frame = pd.read_csv(file_path)
    features = data_frame.drop('Class', axis=1)
    labels = data_frame['Class']
    return features, labels

# Normalizar as variáveis independentes
def normalize_features(features):
    scaler = StandardScaler()
    return scaler.fit_transform(features)

# Aplicar o SMOTE para balancear as classes
def balance_classes(features, labels, strategy=0.3):
    smote = SMOTE(sampling_strategy=strategy, random_state=42)
    return smote.fit_resample(features, labels)


# Função de treinamento e avaliação
def train_and_evaluate_model(X_train, y_train, X_val, y_val, learning_rate, epochs, batch_size):
    layer1 = NeuralLayer(X_train.shape[1], 124)
    activation1 = ReLUActivation()
    layer2 = NeuralLayer(124, 2)
    activation2 = ReLUActivation()
    layer3 = NeuralLayer(2, 1)
    activation3 = SigmoidActivation()
    loss_function = BinaryCrossEntropyLoss()

    for epoch in range(epochs):
        for start in range(0, X_train.shape[0], batch_size):
            batch_X = X_train[start:start + batch_size]
            batch_y = y_train.iloc[start:start + batch_size].values.reshape(-1, 1)

            # Forward pass
            layer1.forward(batch_X)
            activation1.forward(layer1.output)
            layer2.forward(activation1.output)
            activation2.forward(layer2.output)
            layer3.forward(activation2.output)
            activation3.forward(layer3.output)

            # Calcula a perda
            loss_value = loss_function.calculate(activation3.output, batch_y)

            # Backward pass
            gradient = loss_function.backward(activation3.output, batch_y)
            activation3.backward(gradient)
            layer3.backward(activation3.dinput, learning_rate)
            activation2.backward(layer3.dinput)
            layer2.backward(activation2.dinput, learning_rate)
            activation1.backward(layer2.dinput)
            layer1.backward(activation1.dinput, learning_rate)

        # Avaliação no conjunto de validação
        layer1.forward(X_val)
        activation1.forward(layer1.output)
        layer2.forward(activation1.output)
        activation2.forward(layer2.output)
        layer3.forward(activation2.output)
        activation3.forward(layer3.output)

        val_loss = loss_function.calculate(activation3.output, y_val.values.reshape(-1, 1))

        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {val_loss:.4f}")

    return layer1, activation1, layer2, activation2, layer3, activation3

# Configuração de hiperparâmetros
def main():
    features, labels = load_and_prepare_data('creditcard.csv')
    normalized_features = normalize_features(features)
    X_train, X_test, y_train, y_test = train_test_split(normalized_features, labels, test_size=0.5, random_state=42)
    X_resampled, y_resampled = balance_classes(normalized_features, labels)

    X_train_resampled, X_val_resampled, y_train_resampled, y_val_resampled = train_test_split(
        X_resampled, y_resampled, test_size=0.25, random_state=42)

    learning_rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.15, 0.2]
    epochs = 400
    batch_size = 32
    best_model = None
    best_f1_score = 0

    for lr in learning_rates:
        print(f"\nTraining with learning_rate={lr}")
        model = train_and_evaluate_model(X_train_resampled, y_train_resampled, X_val_resampled, y_val_resampled, lr, epochs, batch_size)

        layer1, activation1, layer2, activation2, layer3, activation3 = model

        # Avaliação no conjunto de validação
        layer1.forward(X_val_resampled)
        activation1.forward(layer1.output)
        layer2.forward(activation1.output)
        activation2.forward(layer2.output)
        layer3.forward(activation2.output)
        activation3.forward(layer3.output)

        y_pred_val = (activation3.output >= 0.5).astype(int)
        accuracy_val = accuracy_score(y_val_resampled, y_pred_val)
        precision_val = precision_score(y_val_resampled, y_pred_val)
        recall_val = recall_score(y_val_resampled, y_pred_val)
        f1_val = f1_score(y_val_resampled, y_pred_val)

        print(f"Validation: Accuracy = {accuracy_val:.4f}, Precision = {precision_val:.4f}, Recall = {recall_val:.4f}, F1 = {f1_val:.4f}")

        # Selecionar o melhor modelo
        if f1_val > best_f1_score:
            best_f1_score = f1_val
            best_model = model

    # Previsão no conjunto de teste
    layer1, activation1, layer2, activation2, layer3, activation3 = best_model

    layer1.forward(X_test)
    activation1.forward(layer1.output)
    layer2.forward(activation1.output)
    activation2.forward(layer2.output)
    layer3.forward(activation2.output)
    activation3.forward(layer3.output)

    y_pred_test = (activation3.output >= 0.5).astype(int)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    precision_test = precision_score(y_test, y_pred_test)
    recall_test = recall_score(y_test, y_pred_test)
    f1_test = f1_score(y_test, y_pred_test)

    # Resultados finais
    print("\nResultados finais no conjunto de teste:")
    print(f"Accuracy = {accuracy_test:.4f}, Precision = {precision_test:.4f}, Recall = {recall_test:.4f}, F1 = {f1_test:.4f}")

main()