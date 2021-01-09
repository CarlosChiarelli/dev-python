"""Contém o módulo com o forms."""
from django.db import models


# Create your models here.
class Genero(models.Model):
    """Contém o forms a ser apresentado no HTML."""

    descricao = models.CharField(max_length=50)

    def __str__(self):
        """Método utilizado para mostrar alguma classe string."""
        return self.descricao
