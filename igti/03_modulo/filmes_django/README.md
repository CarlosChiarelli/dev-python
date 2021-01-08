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

## Versão python

É utilizada a versão 3.7.9 no SO Ubuntu 20.04.
