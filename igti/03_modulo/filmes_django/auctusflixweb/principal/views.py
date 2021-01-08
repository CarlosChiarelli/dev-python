"""Aqui criamos a visualização.

A função "render" renderiza o html.
"HttpResponse" será para testar a visualização.
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """Cria a visualização nomeada em principal/urls ("index").

    Esse index deve mostrar/renderizar o templates criado.
    """
    return render(request, 'principal/index.html')
