import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score, recall_score, accuracy_score


class Metricas:
    def __init__(self):
        pass

    def calcula_classif(self, y_true, y_pred):
        """
        Calculate the metrics from a regression problem
        :param y_true: Numpy.ndarray or Pandas.Series
        :param y_pred: Numpy.ndarray or Pandas.Series
        :return: Dict with metrics
        """
        # print('Cálculo das métricas')

        acuracia = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)

        print(classification_report(y_true, y_pred), '\n\n')
        print(
            'Matriz de confusão',
            '\n',
            confusion_matrix(y_true, y_pred),
            '\n\n',
            f'acuracia: {acuracia}, f1: {f1}, recall: {recall}\n\n',
        )

        return {
            'acuracia': acuracia,
            'f1': f1,
            'recall': recall,
        }
