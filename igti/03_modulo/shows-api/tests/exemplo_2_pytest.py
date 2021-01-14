"""Teste com pytest."""
from httpx import get, post

url_base = 'http://127.0.0.1:5000/show'


class TestShow:
    """Classe contendo testes."""

    def test_show_deve_retornar_200_quando_receber_um_get(self):
        """Testar o verbo GET."""
        request = get(url_base + '/Game of Thrones')
        assert request.status_code == 200

    def test_show_deve_retornar_uma_lista_vazia_no_primeiro_request(self):
        """Garantir que primeiro request não deve existir recursos em /show."""
        request = get(url_base + '/Game of Thrones')
        assert request.json() == []

    def test_show_deve_retornar_400_quando_receber_json_serie_invalida(self):
        """Testa enviando um json errado."""
        bad_serie = {'id': 25}
        request = post(url_base, json=bad_serie)
        assert request.status_code == 400
