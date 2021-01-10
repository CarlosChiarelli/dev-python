"""Espelhamento do BD.

Vai conter as classes de modelos mas também poderia
ter as classes de serviços (processamento de dados.)
"""
from data import alchemy


class ShowModel(alchemy.Model):
    """Classe de modelo da tabela show."""

    # dizer qual tabela o modelo se refere (nome da tabela no BD)
    __tablename__ = 'show'

    # criando as colunas
    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(80))

    # episodes fazer algo para carregar automaticamente os episódios
    episodes = []

    def __init__(self, name):
        """Inicia o BD.

        Recebo name para inserir no BD já que ID é inserido automaticamente.
        :param name: String.
        """
        self.name = name

    def json(self):
        """Trafegar a ĩnformação no formato JSON."""
        return {'id': self.id,
                'name': self.name,
                'episodes': []}

    def save_to_db(self):
        """Salva os dados no BD após iniciar a sessão (cache)."""
        alchemy.session.add(self)
        alchemy.session.commit()

    # A API permite busca pelo nome, será visto aqui.
    # Para fazer essa busca será criado CLASSMETHOD.
    # A classe modelo permite que eu realize essa busca com método de classe
    @classmethod
    def find_by_name(cls, name):
        """Busca dentro do BD.

        :param cls: Class necessária para fazer chamada na Query.
        :param name: String que será buscada.
        """
        # retorna apenas primeiro o elemento encontrado e não uma lista inteira
        cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        """Busca dentro do BD.

        :param cls: Class necessária para fazer chamada na Query.
        :param id: String que será buscada.
        """
        cls.query.filter_by(id=id).first()
