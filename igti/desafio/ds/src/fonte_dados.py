"""Classe 1.

Aqui faço o split TREINO/TESTE.
"""

from pandas import read_csv
from numpy import loadtxt
from sklearn.model_selection import train_test_split


class FonteDados:
    """Importa os dados."""

    def __init__(self):
        """Criando variáveis, definir os caminhos dados de treino e teste."""
        self.path_data = '../data/pima-indians-diabetes.csv'
        self.path_cols = '../data/nomes_colunas.txt'
        self.target = 'tem_diab'

    # definir se a etapa é dados de treino ou teste
    def leitura_dados(self, no_split=False, treino=True):
        """Lê os dados.

        :param no_split: Bool se True retorna os dados sem split.
        :param treino: Bool se True retorna Tuple de DataFrames ...
        :param treino: ... (X_train, y_train) senão Tuple com DFs de teste
        :return: pd.DataFrame se no_split=False então Tuple (df1,df2) senão df
        """

        # lendo dados
        df = read_csv(self.path_data, header=None)
        cols = loadtxt(self.path_cols, dtype=str).tolist()

        # nomeando colunas
        df.columns = cols

        if no_split:
            print('Retorno dados completos \n')
            print(f'Dimensão: {df.shape} \n')
            return df

        # split treino/teste (80% para treino)
        X = df.drop(self.target, axis=1)
        y = df[self.target]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # convertende de pd.Series para pd.DataFrame
        y_train = y_train.to_frame()
        y_test = y_test.to_frame()

        if treino:
            print('Retorno treino (X e y) \n')
            print(
                f'Dimensão X: {X_train.shape} \n'
                f'Dimensão y: {y_train.shape} \n'
            )

            return X_train, y_train

        else:
            print('Retorno teste (X e y) \n')
            print(
                f'Dimensão X: {X_test.shape} \n'
                f'Dimensão y: {y_test.shape} \n'
            )

            return X_test, y_test
