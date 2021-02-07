"""Experimentos de diferentes modelos e otimização de hiperparâmetros.

Aqui é executado todo pipeline: pré-processamento, treinamento e predição.
"""
from pandas import Series, DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from xgboost.sklearn import XGBClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from sklearn.neural_network import MLPClassifier
from pandas import DataFrame

from .preprocessamento import Preprocessamento
from .fonte_dados import FonteDados
from .metricas import Metricas


class Experimentos:
    def __init__(self):
        from numpy.random import seed

        seed(1)
        self.modelos_testados = {
            'logistica': LogisticRegression(),
            'knn': KNeighborsClassifier(),
            'decision_tree': DecisionTreeClassifier(),
            'random_forest': RandomForestClassifier(),
            'svm': SVC(),
            'adaboost': AdaBoostClassifier(),
            'xgb': XGBClassifier(),
            'catboost': CatBoostClassifier(verbose=False),
            'mlp': MLPClassifier(
                solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 10)
            ),
        }
        self.dic_modelos = None
        self.metricas_models = {}
        self.y_treino = None

    def treinamento_modelo(self, X_train, y_train):
        """
        Train the model with especified experiments
        :param X_train: pd.DataFrame with train data
        :param y_train: pd.Series with train labels
        :return: Dict with trained model
        """
        for alg in self.modelos_testados.keys():

            # treina cada modelo
            print('Treinando o modelo ', alg)
            modelo = self.modelos_testados[alg]

            print(modelo, '\n\n')
            modelo.fit(X_train, y_train)

            if self.dic_modelos is None:
                self.dic_modelos = {alg: modelo}
            else:
                self.dic_modelos.update({alg: modelo})

        return self.dic_modelos

    def exec_experimentos(self):
        """Executa todos experimentos.

        Todo pipeline - préprocessamento, treino, teste.
        :return: DataFrame com as métricas (resultados teste modelos).
        """

        pre_proc = Preprocessamento()

        print('Leitura dos dados', '\n\n')
        X_treino, y_treino = FonteDados().leitura_dados()
        X_teste, y_teste = FonteDados().leitura_dados(treino=False)

        print('Pré-processamento dados de treino', '\n\n')
        X_treino = pre_proc.processo(X_treino)

        print('Pré-processamento dados de teste', '\n\n')
        X_teste = pre_proc.processo(X_teste, etapa_treino=False)

        print('Balanceamento Oversampling', '\n\n')
        self.y_treino = y_treino
        X_treino, y_treino = pre_proc.balanceamento_oversampling(
            X_treino, y_treino
        )

        print('Treinamento dos modelos')
        modelos = self.treinamento_modelo(X_treino, y_treino)

        print('Executando métricas')
        for model in modelos.keys():

            print('\n', model)
            y_pred = modelos[model].predict(X_teste)

            # vejo as métricas (sempre calculadas no teste)
            metrics = Metricas().calcula_classif(y_teste, Series(y_pred))
            DataFrame.from_dict(metrics, orient='index').to_csv(
                'ds/output/metrica_' + model + '.csv'
            )

            self.metricas_models[model] = metrics

        return (
            DataFrame(self.metricas_models)
            .T.round(2)
            .sort_values(['f1'], ascending=False)
        )
