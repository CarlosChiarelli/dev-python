"""Testa pelo comportamento."""
from httpx import get, post
from behave import then, when, given
from json import loads

url_base = 'http://127.0.0.1:5000/show'

url_get = url_base + '/Game of Thrones'


@given('que existe uma série')
def inserir_tarefa(context):
    """Dados que existe uma série... (primeiro garantir a existência dela)."""
    feature_table = context.table[0]
    serie = {}
    serie['name'] = feature_table['name']
    # serie['episodes'] = feature_table['episodes']

    assert post(url_base, json=serie).status_code == 201


@when('verificar minha série em "{endpoint}"')
def get_minha_serie(context, endpoint):
    """Obtém uma série pelo endpoint."""
    context.request = get(url_get)


@then("não devo ter nenhuma série guardada")
def checando_se_nao_tenho_serie(context):
    """Verifica se a série existe."""
    assert context.request.json() != []


@then('devo ter a seguinte série armazenada')
def checar_se_serie_existe(context):
    """Deve verifica uma série registrada. Esse está falhando."""
    feature_table = context.table[0]
    serie = {}
    serie['name'] = feature_table['name']
    response = context.request.json()

    assert response == [serie], f'{response}'
