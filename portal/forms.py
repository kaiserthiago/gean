from django import forms

from portal.models import Projeto


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
                'class': 'form-control datepicker',
                'required': ''
            }),
            'situacao': forms.Select(attrs={
                'class': 'mdb-select md-form md-outline colorful-select dropdown-primary',
                'searchable': 'Pesquisar...'
            }),
            'autor': forms.Select(attrs={
                'class': 'mdb-select md-outline colorful-select dropdown-primary md-form',
                'searchable': 'Pesquisar...',
            }),
        }

        labels = {
            'descricao': 'Descrição',
            'data_inicio': 'Data de início',
            'situacao': 'Situação'
        }