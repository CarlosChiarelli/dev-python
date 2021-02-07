"""Classe responsável por fazer as previsões."""
import pandas as pd
import numpy as np
from joblib import dump, load
from .fonte_dados import FonteDados
from .preprocessamento import Preprocessamento
from .metricas import Metricas
from .experimentos import Experimentos
from .treinamento_modelo import TreinamentoModelo


class InferenciaModelo:
    def __init__(self, input_web=None):
        self.modelo = None
        self.dados_prever = None
        self.predito = None

        self.input_web = np.asarray(input_web).reshape(1, 8)
        self.input_web = FonteDados().input_web(self.input_web)

    def predicao(self):
        """
        Predict values using model trained.
        :return: pd.Series with predicted values.
        """

        # carregar o modelo treinado
        print('Carregando o modelo', '\n\n')
        self.modelo = load('ds/output/modelo.pkl')

        # ler os dados de TESTE
        print(f'Carregando dados: {self.input_web}\n\n')
        X_teste = self.input_web

        print('Pré-processamento', '\n\n')
        X_teste = self.modelo['preprocess'].processo(
            X_teste, etapa_treino=False
        )

        print('Predição', '\n\n')
        y_pred = self.modelo['model_obj'].predict(X_teste)

        return y_pred[0]
