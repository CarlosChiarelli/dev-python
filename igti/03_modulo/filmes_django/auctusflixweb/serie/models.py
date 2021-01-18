from django.db import models


# Create your models here.
class Serie(models.Model):
    """Linkando o genêro da série (um gênero pode conter várias séries)."""

    # on_delete para não permitir delatar um gênero que exista série associada
    idGenero = models.ForeignKey('genero.Genero', on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    def __str__(self):
        """Construtor do modelo que retorna o nome."""
        return self.name
