from django import forms
from .models import Fichier


class Fichierform(forms.ModelForm):
    class Meta:
        model = Fichier
        fields = [
            'Titre',
            'Auteur',
            'nom_du_fichier',
            'dernier_contributeur',
            'date_de_creation',
            'date_de_modification',
            'sujet',
            'description',
            'document'
        ]
