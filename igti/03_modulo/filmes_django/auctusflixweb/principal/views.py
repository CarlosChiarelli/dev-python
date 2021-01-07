"""Aqui criamos a visualização.

A função "render" renderiza o html.
"HttpResponse" será para testar a visualização.
"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Cria a visualização nomeada em principal/urls ("index")."""
    return HttpResponse("Olá mundo!")
