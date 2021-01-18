"""Construção do formulário."""
from django import forms
from serie.models import Serie


class SerieForm(forms.ModelForm):
    """Transforma o model em forms."""

    class Meta:
        """Define quais campos do model quero utilizar."""

        model = Serie
        fields = '__all__'
