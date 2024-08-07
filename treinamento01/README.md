# Dataset Description
No Airbnb, qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertar o seu imóvel para ser alugado por diária.

Você cria o seu perfil de host (pessoa que disponibiliza um imóvel para aluguel por diária) e cria o anúncio do seu imóvel.

Nesse anúncio, o host deve descrever as características do imóvel da forma mais completa possível, de forma a ajudar os locadores/viajantes a escolherem o melhor imóvel para eles (e de forma a tornar o seu anúncio mais atrativo).

Existem dezenas de personalizações possíveis no seu anúncio, desde quantidade mínima de diária, preço, quantidade de quartos, até regras de cancelamento, taxa extra para hóspedes extras, exigência de verificação de identidade do locador, etc.

Com base nessas informações, podemos tentar criar modelos preditivos em relação ao preço de aluguel dos imóveis ofertados, visando a identificação de preços competitivos com base em ofertas semelhantes.

Files: train.csv - the training set
test.csv - the test set
sample_submission.csv - a sample submission file in the correct format

Columns: id: Identificador único da listagem.

listing_url: URL da página da listagem na plataforma.

scrape_id: Identificador único da operação de coleta de dados (scrape).

last_scraped: Data da última vez que os dados foram coletados.

name: Nome da propriedade.

summary: Resumo curto da propriedade.

space: Descrição do espaço da propriedade, incluindo áreas comuns e privadas.

description: Descrição detalhada da propriedade, incluindo comodidades e características.

experiences_offered: Indica se experiências (atividades) são oferecidas juntamente com a estadia.

neighborhood_overview: Visão geral do bairro onde a propriedade está localizada.

minimum_minimum_nights: Número mínimo de noites exigido pela reserva mínima mais baixa permitida.

maximum_minimum_nights: Número máximo de noites exigido pela reserva mínima mais baixa permitida.

minimum_maximum_nights: Número mínimo de noites exigido pela reserva máxima mais alta permitida.

maximum_maximum_nights: Número máximo de noites exigido pela reserva máxima mais alta permitida.

minimum_nights_avg_ntm: Média do número mínimo de noites exigido para reservas no próximo mês.

maximum_nights_avg_ntm: Média do número máximo de noites permitido para reservas no próximo mês.

number_of_reviews_ltm: Número de avaliações recebidas nos últimos doze meses.

calculated_host_listings_count_entire_homes: Número de propriedades inteiras listadas pelo anfitrião.

calculated_host_listings_count_private_rooms: Número de quartos privados listados pelo anfitrião.

calculated_host_listings_count_shared_rooms: Número de quartos compartilhados listados pelo anfitrião.

host_is_superhost: Indica se o anfitrião é um "superhost" ou não. Um superhost é um anfitrião experiente e altamente avaliado que proporciona estadias excepcionais para seus hóspedes.

host_listings_count: Número total de listagens (propriedades) que o anfitrião possui na plataforma.

latitude: Latitude da localização da propriedade.

longitude: Longitude da localização da propriedade.

accommodates: Número de hóspedes que a propriedade pode acomodar.

bathrooms: Número de banheiros na propriedade.

bedrooms: Número de quartos na propriedade.

beds: Número de camas na propriedade.

extra_people: Custo adicional por hóspede extra acima do número de hóspedes permitido.

minimum_nights: Número mínimo de noites que um hóspede deve reservar.

number_of_reviews: Número total de avaliações recebidas pela propriedade.

instant_bookable: Indica se a propriedade pode ser reservada instantaneamente, sem a necessidade de aprovação prévia do anfitrião.

amenities: Amenidades disponíveis na propriedade.

property_type - Indica o tipo de propriedade.

room_type - Indica o tipo de quarto.

cancellation_policy: Indica o tipo de política de cancelamento.

price: Preço da propriedade por noite (target).