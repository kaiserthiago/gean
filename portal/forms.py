from django import forms
from django.core.exceptions import ValidationError

from portal.models import Projeto, Elemento, Certificado, CertificadoElemento, Medicao


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
                'required': 'True'
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

    # def clean_data_inicio(self):
    #     data_inicio = self.cleaned_data['data_inicio']
    #
    #     if not data_inicio:
    #         raise ValidationError('Você precisa informar a data de início do projeto.')

    def save(self, *args, **kwargs):
        registro = super(ProjetoForm, self).save(*args, **kwargs)
        registro.user = self.request.user
        return registro

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        exclude = ('user',)

    def save(self, *args, **kwargs):
        registro = super(ElementoForm, self).save(*args, **kwargs)
        registro.user = self.request.user
        return registro

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        exclude = ('user',)

    def save(self, *args, **kwargs):
        registro = super(CertificadoForm, self).save(*args, **kwargs)
        registro.user = self.request.user
        return registro

class CertificadoElementoForm(forms.ModelForm):
    class Meta:
        model = CertificadoElemento
        exclude = ('user',)

    def save(self, *args, **kwargs):
        registro = super(CertificadoElementoForm, self).save(*args, **kwargs)
        registro.user = self.request.user
        return registro

class MedicaoForm(forms.ModelForm):
    class Meta:
        model = Medicao
        exclude = ('user',)

    def save(self, *args, **kwargs):
        registro = super(MedicaoForm, self).save(*args, **kwargs)
        registro.user = self.request.user
        return registro


