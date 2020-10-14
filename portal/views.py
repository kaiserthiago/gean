import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from tablib import Dataset

from portal.forms import ProjetoForm
from portal.models import Projeto, Elemento, Certificado, CertificadoElemento, Medicao


def home(request):
    return render(request, 'portal/home.html', {})


@login_required
def projeto_importar(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    certificados = Certificado.objects.all()
    inicio = '%s-%s-%s' % (
        datetime.datetime.today().strftime('%Y'),
        datetime.datetime.today().strftime('%m'),
        datetime.datetime.today().strftime('%d'),
    )
    data_inicial = inicio[8:10] + '/' + inicio[5:7] + '/' + inicio[0:4]


    if request.method == 'POST':
        # PEGA A DATA DO FORM
        data = request.POST['data']
        data = data[6:10] + '-' + data[3:5] + '-' + data[0:2]

        # PEGA O CERTIFICADO
        certificado = Certificado.objects.get(id=request.POST['certificado'])

        # CARREGA OS DADOS DO XLS
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())

        # VERIFICA O ARQUIVO A PARTIR DA LINHA 1
        for n in imported_data[0:]:
            try:
                # BUSCA DOS DADOS DO CERTIFICADO
                dado = CertificadoElemento.objects.get(elemento__simbolo=str(n[0]), certificado=certificado)

                medicao = Medicao()
                medicao.projeto = projeto
                medicao.concentracao_medicao = n[1]
                medicao.data = data
                medicao.dados_elemento = dado

                # INCERTEZA PADRÃO
                if n[2]:
                    medicao.incerteza_padrao_medicao = n[2]
                    medicao.tipo_incerteza = 1

                # INCERTEZA EXPANDIDA
                if n[3]:
                    medicao.incerteza_expandida_medicao = n[3]
                    medicao.tipo_incerteza = 0

                # INCERTEZA EXPANDIDA COMBINADA
                if n[4]:
                    medicao.incerteza_expandida_combinada = n[4]
                    medicao.tipo_incerteza = 3

                # INTERVALO DE CONFIANÇA
                if n[5]:
                    medicao.intervalo_confianca_medicao = n[5]
                    medicao.tipo_incerteza = 2

                medicao.user = request.user
                medicao.save()
            except:
                pass

        messages.success(request, 'Dados importados com sucesso')
        return redirect('projeto_visualizar', projeto_id)

    context = {
        'projeto': projeto,
        'certificados': certificados,
        'data_inicial': data_inicial
    }

    return render(request, 'portal/projeto_importar.html', context)


@login_required
def projeto_visualizar(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    context = {
        'projeto': projeto,
    }

    return render(request, 'portal/projeto_visualizar.html', context)

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
