"""Testes organizados.

Aqui contém testes segmentados e organizados para testar a API.
"""
from httpx import get, post, delete
from data import dic_got

url_base = 'http://127.0.0.1:5000/show'

# TESTE GET
request = get(url_base+'/Game of Thrones')

assert request.status_code == 200, 'Código de resposta diferente de 200'
assert request.json() == dic_got, 'Algo errado no conteúdo'

# TESTE POST
bad_serie = {'name': 'the 100'}

request = post(url_base, json=bad_serie)
assert request.status_code == 201, 'Código diferente de 201'

# TESTE DELETE
request = delete(url_base + '/8')
assert request.status_code == 204, 'Código diferente de 204'
