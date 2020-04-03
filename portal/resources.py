from import_export import resources

from portal.models import Projeto, Elemento, Medicao, Certificado


class ProjetoResource(resources.ModelResource):
    class Meta:
        model = Projeto


class ElementoResource(resources.ModelResource):
    class Meta:
        model = Elemento


class CertificadoResource(resources.ModelResource):
    class Meta:
        model = Certificado


class MedicaoResource(resources.ModelResource):
    class Meta:
        model = Medicao
