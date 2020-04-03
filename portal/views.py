from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from portal.forms import ProjetoForm
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
def projeto_new(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            projeto = Projeto()

            projeto.descricao = form.cleaned_data['descricao']
            projeto.situacao = form.cleaned_data['situacao']
            projeto.data_inicio = form.cleaned_data['data_inicio']
            projeto.autor = form.cleaned_data['autor']
            projeto.user = request.user
            projeto.save()

            messages.success(request, 'Projeto registrado.')

            return redirect('projeto')

    form = ProjetoForm()

    context = {
        'form': form,
    }

    return render(request, 'portal/projeto_new_edit.html', context)


@login_required
def projeto_edit(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            projeto.descricao = form.cleaned_data['descricao']
            projeto.situacao = form.cleaned_data['situacao']
            projeto.data_inicio = form.cleaned_data['data_inicio']
            projeto.autor = form.cleaned_data['autor']
            projeto.user = request.user

            projeto.save()

            messages.success(request, 'Projeto atualizado.')

            return redirect('projeto')

    form = ProjetoForm(instance=projeto)

    context = {
        'form': form,
    }

    return render(request, 'portal/projeto_new_edit.html', context)


@login_required
def projeto_delete(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído.')

    return redirect('projeto')


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
