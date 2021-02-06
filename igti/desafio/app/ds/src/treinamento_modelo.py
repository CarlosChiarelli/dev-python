"""Classe 2.

Parte final sem experimentos!
Uso essa classe quando já tiver o modelo consistente (modelo final).
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
from fonte_dados import FonteDados
from preprocessamento import Preprocessamento
from experimentos import Experimentos


class TreinamentoModelo:
    """Começo aqui chamando dataSource e preProcessamento como preProc não foi definido então."""

    def __init__(self):
        self.dados = FonteDados()
        self.pre_proc = None

    def treinamento_modelo(self):
        """
        Train the model.
        :return: Dict with trained model, preprocessing used and columns used in training
        """

        # chamo o prePocessamento
        self.pre_proc = Preprocessamento()

        # leio os dados
        print('Carregamento dos dados', '\n\n')
        X_treino, y_treino = self.dados.leitura_dados()

        # preProcessamento
        print('Treinamento do pré-processamento', '\n\n')
        # para treino
        X_treino = self.pre_proc.processo(X_treino)

        print('Balanceamento Oversampling', '\n\n')
        X_treino, y_treino = self.pre_proc.balanceamento_oversampling(
            X_treino, y_treino
        )

        print('Treinamento do modelo', '\n\n')
        np.random.seed(1)
        model_obj = RandomForestClassifier()
        model_obj.fit(X_treino, y_treino)

        # guardando informacoes no dicionario
        model = {
            'model_obj': model_obj,
            'preprocess': self.pre_proc,
            'colunas': self.pre_proc.df_nomes_tipos_treino,
        }
        print(model)

        # salvando modelo treinado com informacoes
        dump(model, '../output/modelo.pkl')

        # retorna o dicionario de modelo
        return model
