"""Teste de exemplo."""
from httpx import get

url_base = 'http://127.0.0.1:5000/'

request = get(url_base)

print(request)

# request.status_code
# request.content
