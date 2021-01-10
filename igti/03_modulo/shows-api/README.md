# REST API: Flask

Esse projeto cria uma **API** que permite **incluir** e **listar séries** e **episódios dessas séries**.

Flask já possui um *Web Server* rodando por trás da API, logo ele atua como um *Web Service* (camada conexão + *Web Server*).

## Passos para início da construção

1) criar arquivo ```app.py``` e nele criar as rotas.  

2) testar a aplicação ```python app.py```.

3) criar o modelo da API (só é possível testar quando os verbos estão criados).

4) criado diretório de testes (```tests```), é possível rodar um teste simples ```ipython -i tests/exemplo_1.py``` usando python interativo.

## Criação dos modelos

O modelo é um conjunto de classes que vão espelhar o banco de dados.

Ao utilizar essas classes no Flask elas vão criar o banco de dados.

Então é criado um módulo ```model```.

É necessário a criação do arquivo ```data.py``` para fazer a configuração do SQLAlchemy do projeto.

Então serão criadas as classes de modelos, iniciando com ```model/show.py```.

Abaixo vemos a sequência de passos:

* criar ```model/episodes.py```.
