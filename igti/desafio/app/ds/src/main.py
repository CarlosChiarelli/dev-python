"""Pré-processa os daods, treina e salva o modelo."""
from .experimentos import Experimentos
from .treinamento_modelo import TreinamentoModelo
from .inferencia_modelo import InferenciaModelo


def main():
    # exprimentos (escolha modelo principal)
    exp = Experimentos()
    metricas_modelos = exp.exec_experimentos()

    # treinamento modelo principal
    modelo = TreinamentoModelo().treinamento_modelo()

    # inferência (teste) modelo principal
    inferencia = InferenciaModelo()
    y_pred = inferencia.predicao()


if __name__ == '__main__':
    main()
