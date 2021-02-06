# REST API: Flask

Esse projeto cria uma **API** que permite **incluir** e **listar séries** e **episódios dessas séries**.

Flask já possui um *Web Server* rodando por trás da API, logo ele atua como um *Web Service* (camada conexão/processamento + *Web Server*).

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

## Configuração app Flask Alchemy

Alterações no arquivo ```app.py```:

* dizer qual é o BD adicionando ```app.config[...]``` e além de adicionar a criação do Banco antes da primeira solicitação.

* criar rota de **POST** (inserir um dado / *create_show*) e no ```app.py```.

* teste com arquivo ```tests.exemplo_1.py```.

* criar rota para buscar uma série pelo name ```get_show(name)``` alterando ```app.py```.

* agora será desenvolvido possibilidade de **inserir e buscar** um **episódio**: adicionar essas rotas no ```app.py```.

* será desenvolvida a exclusão de uma série.

* a atualização de uma série (update / PUT) foi iniciado mas não concluído (rota não foi criada, apenas método em ```show.py```).

## Documentação

É necessário 2 documentos:

1. desenvolvedores (devs)

2. cliente da API (consumidores)

O primeiro pode ser desenvolvido usando a lib ```mkdocs``` do python.

Já o segundo é para os consumidores da API, explicando quais são os verbos disponíveis e como deve ser feita as requisições. É utilizado o **Swagger** e o documento pode aparecer no url base para ser consumido.

O comando abaixo gera as dependências do projeto.

```pip freeze > requirements.txt```

Será iniciada a documentação com **mkdocs.**

```mkdocs new .```

Para colocar a documentação no ar basta:

```mkdocs serve```

Então é possível abas com pasta editando o arquivo `mkdocs.yaml` e editando também o `.css`.

Para hospedar numa página é possível gerando a pasta com `mkdocs build` que não será executado ou git pages.

Para obter a relação de dependências basta `pydeps -T png app.py`. É necessário que Graphviz esteja instalado na máquina (apt-get).

### Swagger e Flask



## Testes

Por fim são realizados testes com `pytest` e `pytest-sugar`.
