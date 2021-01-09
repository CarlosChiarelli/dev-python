"""Contém a ligação entre template e model."""
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

# Create your views here.


def cadastro(request):
    """Mandar retornar a renderização do html."""
    form = forms.GeneroForm()

    if request.method == 'POST':
        # carregando os dados do POST dentro do form
        form = forms.GeneroForm(request.POST)

        # saber se o formulário está válido (usuário inseriu OK)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERRO')

    # adicionar lista de gêneros para mostrar na tela
    generos_list = models.Genero.objects.order_by('descricao')

    # é aqui que relaciono o elemento criado (form) com nome no elemento HTML
    data_dict = {'form': form, 'generos_records': generos_list}

    return render(request, 'genero/genero.html', data_dict)


def delete(request, id):
    """Deleta um registro."""
    try:
        # deleta apenas o id alvo
        models.Genero.filter(id=id).delete()
        # repete o código feito no cadastro
        form = forms.GeneroForm()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form, 'generos_records': generos_list}
        return render(request, 'genero/genero.html', data_dict)

    except:
        return HttpResponseNotAllowed()
