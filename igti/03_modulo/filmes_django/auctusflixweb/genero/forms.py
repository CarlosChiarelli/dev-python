"""Contém o formulário que será apresentado dinamicamente no HTML."""
from django import forms
from genero.models import Genero


class GeneroForm(forms.ModelForm):
    """Cria o formulário do HTML."""

    class Meta(object):
        """Classe de meta-dados, será o formulário genêro."""

        model = Genero

        # usado para mostrar todos os campos do forms (editável)
        fields = '__all__'
