from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from portal.models import Projeto, Elemento, Certificado, CertificadoElemento


def home(request):
    return render(request, 'portal/home.html', {})


@login_required
def projeto(request):
    projetos = Projeto.objects.all()

    context = {
        'projetos': projetos
    }

    return render(request, 'portal/projeto.html', context)


@login_required
def elemento(request):
    elementos = Elemento.objects.all()

    context = {
        'elementos': elementos
    }

    return render(request, 'portal/elemento.html', context)


@login_required
def certificado(request):
    certificados = Certificado.objects.all()

    context = {
        'certificados': certificados
    }

    return render(request, 'portal/certificado.html', context)

@login_required
def dados_certificados(request):
    dados_certificados = CertificadoElemento.objects.all()

    context = {
        'dados_certificados': dados_certificados
    }

    return render(request, 'portal/dados_certificados.html', context)