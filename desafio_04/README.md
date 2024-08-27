# Treinamento CIS - 3º Período (Redes Neurais)

## Conteúdos do Período

a. Introdução a Redes Neurais:

- Perceptron;
- Função de ativação;
- Vetor de Pesos e Bias;
- Operações vetoriais;
- Feed Forward;
- Backpropagation;
- Gradiente descendente;
- Ótimo local e global;
- Learning rate;
- Métricas de avaliação;
- Função de custo;
- Overfitting e underfitting;

b. Implementação de Regressão Linear com perceptron;

c. Problemas lineares e não lineares;

d. Implementação usando TensorFlow.

## Conteúdo Essenciais

a. [An Introduction to Perceptron](https://youtu.be/DhWp49VRCk4?si=qHdosGm-8RCANIG5) - Vídeo explicando o conceito do
Perceptron

b. [Playlist Redes Neurais Artificiais](https://www.youtube.com/watch?v=ebToEXQFCo4&list=PLQH6T1jnIb5J7vugBAauJsFU8Qgvuf-4X&ab_channel=MachineLearningparahumanos) (PT-BR) ou [Playlist Neural Networks 3blue1brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (EN - US) - Playlist que explica o que são
Redes Neurais, Gradiente descendente e Backpropagation. -
Playlist com os conceitos fundamentais sobre o perceptron e
redes neurais (Português)
- Vetor de Pesos
- Funções de ativação
- Backpropagation
- Gradiente descendente

c. [Neural Networks from Scratch in Python](https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3)
- Passo a passo para criar uma rede neural a partir do zero
em python

## Conteúdos Complementares

a. [Playlist Neural Networks StatQuest](https://www.youtube.com/watch?v=CqOfi41LfDw&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1&index=2&ab_channel=StatQuestwithJoshStarmer)

b. [MIT Introduction to Deep Learning](https://www.youtube.com/watch?v=njKP3FqW3Sk) - Aula do MIT sobre
fundamentos do Deep Learning.

c. [Neural Networks and Deep Learning](https://www.youtube.com/playlist?list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0) - Aulas do curso 1 da
especialização em Deep Learning do deeplearning.ai.

d. [Improving Deep Neural Networks: Hyperparameter Tuning,
Regularization and Optimization](https://www.youtube.com/playlist?list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc) - Aulas do curso 2 da especialização
em Deep Learning do deeplearning.ai.

e. [DeepLearning Book](http://deeplearningbook.com.br/) - Livro em português sobre Deep Learning.
Para o quarto período, recomenda-se os capítulos 1 ao 21.

f. [Neural Networks and Deep Learning Book](http://neuralnetworksanddeeplearning.com/)

g. [Hands-on Machine Learning with Scikit-Learn, Keras, and
TensorFlow](https://drive.google.com/file/d/1S4j5ivHtVArowR5TEFFQocjQDx4T07bG/view?usp=sharing) - Livro completo: Para o quartoperíodo recomenda-se
o capítulo 10.

## Tarefas

a. Base de Dados do Período - [Credit Card Fraud Detection](https://drive.google.com/file/d/15Ejc7ttoyHERT8pj_s7GSTdpQCJ-MHao/view?usp=sharing)

b. Atividade obrigatória:
-Criar uma rede neural “from scratch” de classificação binária
para prever fraudes nas transações com cartões de crédito. Use
como embasamento a playlist Neural Networks from Scratch in Python:

1. A rede deve conter uma camada oculta (quantidade de
neurônios a critério)

2. Separe a label das features e o dataset em subsets de
treinamento e teste;

3. Inicialização randômica dos pesos;

4. Defina a função de ativação e calcular sua derivada (Sinta-se
à vontade para experimentar mais de uma);

5. Treine o modelo testando diferentes valores de épocas e
learning rate, identificando quando acontece Overfitting e
Underfitting.