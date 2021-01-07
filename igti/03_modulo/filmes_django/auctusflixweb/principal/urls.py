"""Arquivo de URLs onde vou configurar minhas URLs."""
from django.urls import path
from . import views

# dizer quais pattners podem ser respondidos aqui dentro
"""
Quando for a view principal (root / "") é pra carregar a
views.index (que será criada).
Quando cair nesse caso é pra chamar views.index com o nome "index"
"""
urlpatterns = [
    path('', views.index, name='index')
]
