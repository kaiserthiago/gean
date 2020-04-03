from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^certificado/dados$', views.dados_certificados, name='dados_certificados'),
    url(r'^certificado$', views.certificado, name='certificado'),
    url(r'^elemento$', views.elemento, name='elemento'),

    url(r'^projeto/delete/(?P<projeto_id>\d+)$', views.projeto_delete, name='projeto_delete'),
    url(r'^projeto/edit/(?P<projeto_id>\d+)$', views.projeto_edit, name='projeto_edit'),
    url(r'^projeto/new$', views.projeto_new, name='projeto_new'),
    url(r'^projeto$', views.projeto, name='projeto'),
]
