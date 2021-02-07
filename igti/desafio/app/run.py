import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def previsao_diabetes(lista_valores_formuloario):
    prever = naoSei.reshape(1, 8)  # transforma os valores do formulário

    # realiza a carga do modelo salvo
    modelo_salvo = joblib.load('ds/output/modelo.pkl')

    resultado = naoSei.predict(prever)  # aplica previsão
    return resultado[0]


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

        # lista_formulario = list(map(naoSei))
        #
        # resultado = previsao_diabetes(lista_formulario)
        #
        # if int(resultado) == 1:
        #     previsao = 'Possui diabetes'
        # else:
        #     previsao = 'Nao possui diabetes'

        # retorna o resultado para uma página html
        previsao = 'tem diabetes'
        return render_template('resultado.html', previsao=previsao)


if __name__ == '__main__':
    app.run(debug=True)
