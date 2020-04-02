from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from portal.models import Projeto, Elemento, Medicao


@admin.register(Projeto)
class ProjetoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Elemento)
class ElementoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Medicao)
class MedicaoAdmin(ImportExportModelAdmin):
    pass