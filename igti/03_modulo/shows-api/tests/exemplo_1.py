"""Teste de exemplo."""
from httpx import get, post, delete
from json import loads

url_base = 'http://127.0.0.1:5000/'

request = get(url_base)

print(request)

# testando GET
print(f'GET Status 200: {request.status_code==200}')
print(f'Conteúdo: {request.content}')

# testando POST (inclui série)
url_post = url_base + 'show'
request = post(url_post, json={"name": "Game of Thrones"})

print(request)
print(f'POST Status: {request.status_code}')
print(f'Conteúdo: {loads(request.content)}')

# testando GET de procura/obtém série
rota_get = url_base + 'show/'
request = get(rota_get+'Friends')
print(request)
print(loads(request.content))

request = get(rota_get+'Game of Thrones')
print(request)
print(loads(request.content))

# testando POST para incluir episódio
rota_add_ep = rota_get + 'Game of Thrones/episode'
request = post(rota_add_ep, json={'name': 'Casamento vermelho', 'season': 3})
print(f'{rota_add_ep}\n{request}\n{loads(request.content)}')

# testando DELETE de uma série (deletar ID 1)
rota_del = url_base + 'show/1'
request = delete(rota_del)
print(f'\nDELETE:{request}\n{loads(request.content)}')
