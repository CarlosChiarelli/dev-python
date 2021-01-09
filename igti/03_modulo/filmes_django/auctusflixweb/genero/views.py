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
        models.Genero.objects.filter(id=id).delete()
        # repete o código feito no cadastro
        form = forms.GeneroForm()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form, 'generos_records': generos_list}
        return render(request, 'genero/genero.html', data_dict)

    except:
        return HttpResponseNotAllowed()


def update(request, id):
    """Faz a alteração de um item.

    Ele carrega o ID no formulário chamado em genero.html pelo JS.
    Então é feito um GET na página do formulário "invocado".
    """
    # abaixo carrego o item do modelo que eu quero
    item = models.Genero.objects.get(id=id)

    if request.method == 'GET':
        # carrega o item com o campo descricao recebido
        form = forms.GeneroForm(initial={'descricao': item.descricao})
        data_dict = {'form': form}
        return render(request, 'genero/genero_upd.html', data_dict)
    else:
        # se não for GET eu preciso salvar o dado (POST)
        form = forms.GeneroForm(request.POST)
        # mudo a descricao do item que carreguei
        # com a descricao que veio do formulário e salvo no BD
        item.descricao = form.data['descricao']
        item.save()

        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {'form': form, 'generos_records': generos_list}
        return render(request, 'genero/genero.html', data_dict)
