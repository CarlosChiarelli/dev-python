"""Contém as URLs e pattners para o CRUD (cadastro, deleção e update)."""
from django.urls import path
from . import views

# '' é para estar na raiz do módulo (genero/)
# isso poderia ser uma expressão regular
urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('delete/<id>', views.delete, name='delete'),
    path('update/<id>', views.update, name='update')
]
