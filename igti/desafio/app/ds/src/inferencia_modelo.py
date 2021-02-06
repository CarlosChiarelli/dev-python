"""Classe responsável por fazer as previsões."""
import pandas as pd
import numpy as np
from joblib import dump, load
from fonte_dados import FonteDados
from preprocessamento import Preprocessamento
from metricas import Metricas
from experimentos import Experimentos
from treinamento_modelo import TreinamentoModelo


class InferenciaModelo:
    def __init__(self):
        self.modelo = None
        self.dados_prever = None
        self.predito = None

    def predicao(self):
        """
        Predict values using model trained.
        :return: pd.Series with predicted values.
        """

        # carregar o modelo treinado
        print('Carregando o modelo', '\n\n')
        self.modelo = load('../output/modelo.pkl')

        # ler os dados de TESTE
        print('Carregando dados', '\n\n')
        X_teste, y_teste = FonteDados().leitura_dados(treino=False)

        print('Pré-processamento', '\n\n')
        X_teste = self.modelo['preprocess'].processo(
            X_teste, etapa_treino=False
        )

        print('Predição', '\n\n')
        y_pred = self.modelo['model_obj'].predict(X_teste)

        # salvando resultado predito
        print('Salvando arquivos', '\n\n')
        self.dados_prever = X_teste
        self.predito = pd.DataFrame(y_pred)

        submeter = self.predito.copy()
        submeter.to_csv('../output/predito.csv', index=False)

        return submeter
