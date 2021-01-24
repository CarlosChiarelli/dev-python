"""Realiza manipulação de dados com Pandas."""
import pandas as pd


class Processamento:
    """Processa os dados."""

    def __init__(self):
        """Lê os dados."""
        self.df = pd.read_csv('data/temperature.csv')

    def get_describe(self):
        """Retorna a descrição."""
        return self.df.describe()

    def get_list_temp(self):
        """Retorna a temperatura em lista."""
        return self.df['temperatura'].values.tolist()

    def get_list_date(self):
        """Retorna datas em lista."""
        return (
            pd.to_datetime(self.df['date'])
            .dt.strftime('%m/%d/%Y')
            .values.tolist()
        )

    def get_head(self, qtd):
        """Retorna primeiras linha em dataframe recebendo quantidade de linhas."""
        return self.df.head(qtd)
