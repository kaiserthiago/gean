from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^certificado/dados$', views.dados_certificados, name='dados_certificados'),
    url(r'^certificado$', views.certificado, name='certificado'),
    url(r'^elemento$', views.elemento, name='elemento'),
    url(r'^projeto$', views.projeto, name='projeto'),
]
