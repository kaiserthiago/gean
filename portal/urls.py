from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^projeto$', views.projeto, name='projeto'),
    url(r'^certificado$', views.certificado, name='certificado'),
    url(r'^elemento$', views.elemento, name='elemento'),
]
