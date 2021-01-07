# Aplicação com filmes (django)

Projeto de uma aplicação web que cadastro e visualiza filmes.

## 1) Iniciando o projeto

É necessário ambiente virtual ativado para executar os comandos abaixo:

* criando projeto (aplicação base): django-admin startproject auctusflixweb

* cd auctusflixweb

* iniciar projeto: python manage.py runserver

* criar aplicação principal (chama outras aplicações): python manage.py startapp principal


## 2) Configurações da aplicação principal

Configurar para que tudo que chegar na aplicação principal ele deve procurar/utilizar nas configurações de URL do "principal/". Será criada todas as URL que ele conhece.

*  no arquivo auctusflixweb/urls.py incluir "from django.urls import path, include"

* adicionar o caminho do "principal/" no mesmo arquivo

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', view=include('principal.urls'))
]
"""

Agora é necessário criar o arquivo de URL do principal: principal/urls.py

No arquivo principal/views é necessário criar a visualização (chamada de "index").

Dentro do auctusflixweb/settings.py é necessário dizer quais aplicações estão instaladas (já vem com várias instaladas). É necessário incluir a principal para ele saber que existe essa nova aplicação.

* incluir no arquivo: INSTALLED_APPS = ['principal']




## Versão python

É utilizada a versão 3.7.9 no SO Ubuntu 20.04.
