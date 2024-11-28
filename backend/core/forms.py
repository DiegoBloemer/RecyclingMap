# formulários para salvar dados no banco de dados
from django import forms
from .models import LocalReciclagem, Imagem
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LocalReciclagemForm(forms.ModelForm):
    class Meta:
        model = LocalReciclagem
        fields = ['nome', 'endereco', 'latitude', 'longitude', 'tipo_residuo']

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['imagem']


class RegisterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input-field',
            'placeholder': 'Seu melhor E-mail',
            'required': 'required'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Insira uma senha',
            'id': 'password',
            'required': 'required'
        })
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Repita sua senha',
            'id': 'repeat_password',
            'required': 'required'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise ValidationError("As senhas não coincidem!")

        return cleaned_data