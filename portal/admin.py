from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from portal.forms import ElementoForm
from portal.models import Projeto, Elemento, Medicao, Certificado, CertificadoElemento


@admin.register(Projeto)
class ProjetoAdmin(ImportExportModelAdmin):
    pass


@admin.register(Certificado)
class CertificadoAdmin(ImportExportModelAdmin):
    list_display = ('descricao', 'codigo')
    search_fields = ('descricao',)


@admin.register(Elemento)
class ElementoAdmin(ImportExportModelAdmin):
    list_display = ('descricao', 'simbolo')
    search_fields = ('descricao',)

    # form = ElementoForm


@admin.register(CertificadoElemento)
class CertificadoElementoAdmin(ImportExportModelAdmin):
    list_display = ('certificado', 'elemento', 'concentracao', 'incerteza_expandida', 'fracao_massa', 'tipo_fracao_massa')
    list_filter = ('certificado__descricao', 'elemento__simbolo')
    search_fields = ('certificado__descricao', 'elemento__simbolo')


@admin.register(Medicao)
class MedicaoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'projeto', 'dados_elemento', 'concentracao_medicao', 'data')
    list_filter = ('projeto', 'dados_elemento__elemento')

