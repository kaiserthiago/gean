from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from portal.forms import ElementoForm, CertificadoForm, CertificadoElementoForm, MedicaoForm, ProjetoForm
from portal.models import Projeto, Elemento, Medicao, Certificado, CertificadoElemento


@admin.register(Projeto)
class ProjetoAdmin(ImportExportModelAdmin):
    list_display = ('descricao', 'autor')
    form = ProjetoForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProjetoAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form


@admin.register(Certificado)
class CertificadoAdmin(ImportExportModelAdmin):
    list_display = ('descricao', 'codigo')
    search_fields = ('descricao',)

    form = CertificadoForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(CertificadoAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form

@admin.register(Elemento)
class ElementoAdmin(ImportExportModelAdmin):
    list_display = ('descricao', 'simbolo')
    search_fields = ('descricao',)

    form = ElementoForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(ElementoAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form

@admin.register(CertificadoElemento)
class CertificadoElementoAdmin(ImportExportModelAdmin):
    list_display = (
        'certificado',
        'elemento',
        'tipo_concentracao',
        'concentracao',
        'incerteza_expandida',
        'incerteza_padrao',
        'incerteza_confianca',
        'incerteza_combinada',
        'fracao_massa',
        'tipo_fracao_massa'
    )
    list_filter = ('certificado__descricao', 'elemento__simbolo')
    search_fields = ('certificado__descricao', 'elemento__simbolo')

    form = CertificadoElementoForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(CertificadoElementoAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form


@admin.register(Medicao)
class MedicaoAdmin(ImportExportModelAdmin):
    list_display = (
        'descricao',
        'projeto',
        'dados_elemento',
        'tipo_incerteza',
        'concentracao_medicao',
        'incerteza_padrao_medicao',
        'incerteza_expandida_medicao',
        'incerteza_expandida_combinada',
        'data'
    )

    list_filter = (
        'projeto',
        'dados_elemento__elemento',
        'dados_elemento__certificado__codigo'
    )

    search_fields = ['descricao', ]

    form = MedicaoForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(MedicaoAdmin, self).get_form(request, obj=obj, **kwargs)
        form.request = request
        return form