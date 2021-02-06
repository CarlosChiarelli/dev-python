"""Demanda muito tempo são muitos testes para ver ganho de performance nas métricas do modelo."""
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from pandas import Series, DataFrame


class Preprocessamento:
    def __init__(self):
        """Criando objetos que quero salvar com a classe para aproveitá-los depois."""
        self.df_nomes_tipos_treino = None
        self.perc_miss_rm = None
        self.cols_rem = None
        self.cols_alteradas = None
        self.categ_ordinal = []
        self.vars_categ_ord = None
        self.vars_num = None
        self.input_miss = None
        self.input_miss_Y = None
        self.normalizador = None

    def dfExploracao(self, df):
        """Retorna df com nomes, tipos, percentual de NAs e contagem unicos da coluna.

        :param df: pd.Dataframe com os dados tabulares principais.
        :return: pd.Dataframe é a tabela com dados resumidos."""

        explora = DataFrame(
            data={
                'colunas': list(df.columns),
                'tipos': list(df.dtypes),
                'na_perct': df.isna().sum() / df.shape[0],
                'quantUnicos': df.nunique(),
            }
        )

        # removendo indice
        explora.reset_index(inplace=True)
        explora.drop('index', axis=1, inplace=True)
        return explora

    def processo(
        self, df_input, etapa_treino=True, perc_miss=0.5, target=False
    ):
        """
        Processo para treinamento do modelo
        1. Discretiza e corrige variaveis: tipo_escola, Q025, sexo, ano_de_conclusao, raça
        2. Remove colunas por completude e significado
        3. Rotula categóricas ordinais

        :param df: Pandas DataFrame
        :param etapa_treino: Boolean
        :return: Pandas Data Frame processado

        """

        # diferenciar etapa TREINO/TESTE
        # pois fit_transform Treino e apenas transform no Teste

        df = df_input.copy()

        # se quero processar o Y (target)
        if target:
            if etapa_treino:
                print('Preenchendo missings Y treino')
                self.input_miss_Y = SimpleImputer(
                    strategy='constant', fill_value=0
                )
                df = self.input_miss_Y.fit_transform(df)
            else:
                print('Preenchendo missings Y teste', '\n\n')
                df = self.input_miss_Y.transform(df)

            return df

        if etapa_treino:
            # CALCULO tudo se for etapa de TREINO

            # salvando colunas e tipos do treino
            print('Salvando tipos e nomes das colunas de treino', '\n')
            self.df_nomes_tipos_treino = self.dfExploracao(df)[
                ['colunas', 'tipos']
            ]

            # tipos categóricas ordinais
            mask = self.df_nomes_tipos_treino['tipos'] == 'object'
            self.vars_categ_ord = self.df_nomes_tipos_treino[mask]['colunas']

            mask = self.df_nomes_tipos_treino['tipos'] != 'object'
            self.vars_num = self.df_nomes_tipos_treino[mask]['colunas']

            print('Preenchimento dos missings das numéricas', '\n')
            self.input_miss = SimpleImputer(strategy='constant', fill_value=0)

            df[self.vars_num] = self.input_miss.fit_transform(
                df[self.vars_num]
            )

            print('Normalização dos dados (mínimo e máximo)', '\n')
            self.normalizador = MinMaxScaler()
            df[self.vars_num] = self.normalizador.fit_transform(
                df[self.vars_num]
            )

        else:
            # APLICO tudo se for etapa de TESTE

            print('Preenchimento dos missings das numéricas', '\n')
            df[self.vars_num] = self.input_miss.transform(df[self.vars_num])

            print('Normalização dos dados (mínimo e máximo)', '\n')
            df[self.vars_num] = self.normalizador.transform(df[self.vars_num])

        return df

    def reducao_dim(self, x_treino, n_dim=2, metodo='pca'):
        """
        : ações: redução de dimensionalidade com TSNE
        : param x_treino: Dataframe para converter
        : return: DF reduzido
        """
        from sklearn.manifold import TSNE
        from sklearn.decomposition import PCA

        if metodo == 'pca':
            pca = PCA(n_components=n_dim, random_state=42)
            pca.fit_transform(x_treino)
            x_reduzido = pca.transform(x_treino)
            return x_reduzido

        else:
            tsne = TSNE(n_components=n_dim, random_state=42)
            tsne_results = tsne.fit_transform(x_treino)
            return tsne_results

    def balanceamento_oversampling(self, x_treino, y_treino):
        """
        : ações: transforma dados desbalanceados em balanceados (aumenta classe minoritaria)
        : param x_treino: Dataframe para converter
        : return: DF balanceado
        """
        from imblearn.over_sampling import SMOTE

        smote = SMOTE(sampling_strategy="minority")

        X_smote, y_smote = smote.fit_resample(x_treino, y_treino['tem_diab'])

        print(
            'Dimensões antes:',
            (x_treino.shape, y_treino.shape),
            ' |  Dimensões depois:',
            (X_smote.shape, y_smote.shape),
        )
        return X_smote, y_smote
