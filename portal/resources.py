from import_export import resources

from portal.models import Projeto, Elemento, Medicao


class ProjetoResource(resources.ModelResource):
    class Meta:
        model = Projeto


class ElementoResource(resources.ModelResource):
    class Meta:
        model = Elemento

class MedicaoResource(resources.ModelResource):
    class Meta:
        model = Medicao