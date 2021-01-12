"""Episódios."""
from data import alchemy


class EpisodeModel(alchemy.Model):
    """Classe que representa um episódio.

    Cada objeto dentro representa uma linha do BD.
    """

    __tablename__ = 'episode'

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    name = alchemy.Column(alchemy.String(80))
    season = alchemy.Column(alchemy.Integer)

    # coluna especial
    # criar esse campo ele vai ligá-lo ao ID da tabela shows
    # vai ajudar a carregar os episódios da tabela show
    show_id = alchemy.Column(alchemy.Integer, alchemy.ForeignKey('shows.id'))

    def __init__(self, name, season, show_id):
        """Inicia o BD.

        :param name: String.
        :param season: String.
        :param show_id: String.
        """
        self.name = name
        self.season = season
        self.show_id = show_id

    def json(self):
        """Trafegar a ĩnformação no formato JSON."""
        return {'name': self.name,
                'season': self.season}

    def save_to_db(self):
        """Salva os dados no BD após iniciar a sessão (cache)."""
        alchemy.session.add(self)
        alchemy.session.commit()

    def delete_from_db(self):
        """Usa primary_key (ID) para fazer deleção."""
        alchemy.session.delete(self)
        alchemy.session.commit()
