import numpy as np
import joblib
from os.path import isfile
from flask import Flask, request, jsonify, render_template
from ds.src.inferencia_modelo import InferenciaModelo
from ds.src.run_pipeline import main as run_pipeline_data

app = Flask(__name__)


def previsao_diabetes(valores_list):
    """Realiza a predição dos dados inseridos no formulário."""
    resultado = InferenciaModelo(valores_list).predicao()

    return resultado


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':

        # converte dados recebidos para dicionário
        lista_formulario = request.form.to_dict()

        # converte dados recebidos para lista
        lista_formulario = list(lista_formulario.values())

        resultado = previsao_diabetes(lista_formulario)

        if int(resultado) == 1:
            previsao = 'Possui diabetes'
        else:
            previsao = 'Nao possui diabetes'

        # retorna o resultado para uma página html
        return render_template('resultado.html', previsao=previsao)


if __name__ == '__main__':

    # se o modelo de produção não foi gerado, então todo pipeline é executado
    if not isfile('ds/output/modelo.pkl'):
        run_pipeline_data()

    app.run(debug=True)
