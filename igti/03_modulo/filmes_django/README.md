# Aplicação com filmes (django)

Projeto de uma **aplicação web que cadastra e visualiza filmes e séries**.

Sobre a arquitetura do Django podemos levantar alguns pontos importantes.

A princípio foi criado para **gerar páginas estáticas**, diferente do JavaScript que gera páginas dinâmicas.

O Django se baseia no modelo MTV:

* M - Model (modelo do banco de dados)
* T - Template (visualização, ela renderiza html css e js)
* V - View (faz a ligação do template com modelo)

Dentro de sua arquitetura existe um CRUD, acrônimo para :

- Create (Criação)
- Read (Consulta)
- Update (Atualização)
- Delete (Destruição)

Abaixo segue os passos para construção do projeto.

## 0) Ativar ambiente virtual

* ```source .venv/bin/activate```

## 1) Iniciando o projeto

* criando projeto (aplicação base): ```django-admin startproject auctusflixweb```

* ```cd auctusflixweb```

* iniciar projeto: ```python manage.py runserver```

* criar aplicação principal (chama outras aplicações): ```python manage.py startapp principal```


## 2) Configurações da aplicação principal

Configurar para que tudo que chegar na aplicação principal ele deve procurar/utilizar nas configurações de URL do "principal/". Será criada todas as URL que ele conhece.

*  no arquivo auctusflixweb/urls.py incluir ```from django.urls import path, include```

* adicionar o caminho do "principal/" no mesmo arquivo

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', view=include('principal.urls'))
]
```

Agora é necessário criar o arquivo de URL do principal: principal/urls.py

No arquivo principal/views é necessário criar a visualização (chamada de "index").

Dentro do auctusflixweb/settings.py é necessário dizer quais aplicações estão instaladas (já vem com várias instaladas). É necessário incluir a principal para ele saber que existe essa nova aplicação.

* incluir no arquivo: ```INSTALLED_APPS = ['principal']```


# 3) HTML e CSS

A grosso modo podemos ver uma aplicação web como um corpo humano:

* HTML - esqueleto (estrutura)
* Django - músculos (movimento, na verdade seria o JS com páginas dinâmicas)
* CSS - pele (beleza)

Este tópico é adicionado para completar o projeto.

Será criado um diretório na raiz para alguns testes e anotações que não farão parte da aplicação em sí.


# 4) Menu principal

Início do desenvolvimento do menu principal. Deve-se criar *static* e *templates* dentro do projeto **auctusflixweb**.

Dentro do arquivo *auctusflixweb/settings.py* é possível ver o BASE_DIR que é o diretório do projeto que dentro de **auctusflixweb**.

Após os diretórios criados eles devem ser configurados.

Adicionar dentro desse arquivo as linhas para indicar os locais:

```
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# adicionar linhas abaixo

TEMPLATES_DIR = join(BASE_DIR, 'templates')
STATIC_DIR = join(BASE_DIR, 'static')
```

E adicionar o local do template o *TEMPLATE_DIR* (vários podem ser adicionados se houver vários templates):

```
TEMPLATES = [
    {
      ...
        'DIRS': [TEMPLATE_DIR],
      ...
    },
]
```
Adicionar o *STATICFILES_DIR*:

```
STATIC_URL = '/static/'

# adicionar abaixo

STATICFILES_DIRS = [
    STATIC_DIR
]
```

## 5) Criar templates e css

Vamos criar os templates separados para cada módulo (principal, gêneros e séries) do projeto.

Dentro do diretório *templates*: ```mkdir principal```

Criado o *templates/principal/index.html* e *templates/menu.html* (menu compartilhado por toda aplicação). O menu vai conter todos os 3 módulos.

Por fim é necessário fazer a View do principal (index) mostrar/chamar o template do menu (alterar ```principal/views.py```).

Em seguida basta gerar o css para o template renderizado acima. Criar o diretório em *static*, nomeado como *css* e dentro criar os arquivos para os módulos.


## 6) Criar 2ª aplicação (gênero)

Uma aplicação (nome definido pela comunidade) se comporta como um módulo no Django. Já existem diversos módulos prontos que podem ser facilmente plugados no projeto.

Deve-se iniciar a construção dela dentro do projeto:

```python manage.py startapp genero```

Essa aplicação será longa porque quase todos os conceitos do **CRUD** estarão aqui.

Aqui será listado os mesmos passos iniciais criados no módulo principal:

* ```auctusflixweb/settings.py``` adicionar **genero** no ```INSTALLED_APPS```.

* ```auctusflixweb/urls.py``` incluir o caminho/rota do **genero**.

* criar ```genero/urls.py``` e adicionar as configurações.

* adicionar no arquivo ```genero/views.py``` o caminho para renderizar html.

* criar templates do **genero**: criar ```templates/genero/genero.html```. Nesse item será adicionado o *forms* para cadastro.

* editar ```templates/menu.html``` corrigindo a rota do genêro.

* criar arquivo ```genero/forms.py``` (gerar o formulário).

* importar e adicionar os formulários em ```genero/views.py```.

* adicionar token no ```templates/genero/genero.html```

* criar um ```static/css/crud.css``` para os gêneros e séries.

* criar o modelo do **gênero**. Ao invés de usar o arquivo forms.py separado ele será criado dentro de ```genero/models.py``` pois assim ele será um forms com ID.

* editar o ```genero/forms.py```.

* migra a tabela dos modelos, ou seja, migrar aplicações pro BD (sqllite). É necessário criar um super usuário e executar os comandos:

```
python manage.py migrate
python manage.py createsuperuser
carlos
meu_email@email.org
senhaSecreta
senhaSecreta
```

Agora acessando ```ip_rota/admin``` é possível ter acesso ao modo usuário. Em seguida vamos preparar (criar ddl da migração) o formulário e migrá-lo. Acontecerá dentro do diretório ```genero/migrations``` .

```
python manage.py makemigrations genero
python manage.py migrate
```

* registrar o modelo para que ele aparece no site "ip_rota/admin". Para isso editar o arquivo ```genero/admin.py``` (adicionar modelos).

* editar  ```genero/views.py``` para definir os métodos a serem utilizados.

* inserir uma tabela em ```templates/genero/genero.html``` e adicionar lista de gêneros para ser mostrada no formulário em ```genero/views.py```.

Aqui já é possível inserir um item com sucesso visualizando essa tabela na página de gênero.

* adicionar a funcionalidade do botão de excluir. Será necessário construir um javaScript inserindo em ```templates/genero/genero.html```.

* adicionar URL do método delete em ```genero/urls.py``` e em seguida adicionar o *delete* na view do genero.























## Versão python

É utilizada a versão 3.7.9 no SO Ubuntu 20.04.
