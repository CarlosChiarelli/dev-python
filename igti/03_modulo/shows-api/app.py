"""Programa/Aplicação principal."""
from flask import Flask

# É o nome do programa (análogo ao .self das classes).
# Instancia o Flask
app = Flask(__name__)


# criar uma rota/endpoint para raiz utilizando método GET
# utilizando a função abaixo
@app.route('/', methods=['GET'])
def home():
    """Função executa quando aplico o Get rota da raiz."""
    return 'API Funcionando', 200


# rodar/executar aplicação Flask
# debug=True em ambiente de teste, em produção debug=False
# port=5000 é a porta padrão (editável)
app.run(port=5000, debug=True)
