from django import forms
from django.core.exceptions import ValidationError

from portal.models import Projeto, Elemento


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        exclude = ('user',)

        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'autofocus': '',
                'required': ''
            }),
            'data_inicio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' ',
                'type': 'date',
                'required': ''
            }),
            'situacao': forms.Select(attrs={
                'class': 'mdb-select md-form md-outline colorful-select dropdown-primary',
                'searchable': 'Pesquisar...',
                'required': ''
            }),
            'autor': forms.Select(attrs={
                'class': 'mdb-select md-outline colorful-select dropdown-primary md-form',
                'searchable': 'Pesquisar...',
                'required': ''
            }),
        }

        labels = {
            'descricao': 'Descrição',
            'data_inicio': 'Data de início',
            'situacao': 'Situação'
        }

    def clean_data_inicio(self):
        data_inicio = self.get_entered_data('data_inicio')

        if not data_inicio:
            raise ValidationError('Você precisa informar a data de início do projeto.')

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ()

    def __init__(self, *args, **kwargs):
        super(ElementoForm, self).__init__(*args, **kwargs)
        self.fields['user'] = self.request.user