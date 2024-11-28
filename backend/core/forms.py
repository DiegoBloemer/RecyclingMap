# formulários para salvar dados no banco de dados

from django import forms
from .models import LocalReciclagem, Imagem

class LocalReciclagemForm(forms.ModelForm):
    class Meta:
        model = LocalReciclagem
        fields = ['nome', 'endereco', 'latitude', 'longitude', 'tipo_residuo']

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['imagem']