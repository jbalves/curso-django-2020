from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Cidade, Pais


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        # fields = ['nome', 'capital']
        fields = '__all__'

    def clean(self):
        nome = self.cleaned_data['nome']

        if nome == 'Itajubá':
            raise ValidationError({'nome': 'Não podemos cadastrar a cidade de Itajubá no sistema.'})


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

    def clean(self):
        nome = self.cleaned_data['nome']

        if nome == 'Brazil':
            raise ValidationError({'nome': 'Não podemos cadastrar o País Brazil no sistema.'})
