import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from tablib import Dataset

from portal.forms import ProjetoForm
from portal.models import Projeto, Elemento, Certificado, CertificadoElemento, Medicao
import statistics


def home(request):
    return render(request, 'portal/home.html', {})


@login_required
def medicao_delete(request, medicao_id, projeto_id):
    medicao = get_object_or_404(Medicao, pk=medicao_id)

    if request.method == 'POST':
        medicao.delete()
        messages.success(request, 'Medição excluída.')

    return redirect('projeto_visualizar', projeto_id)


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
        data1 = request.POST['data1']
        data1 = data1[6:10] + '-' + data1[3:5] + '-' + data1[0:2]

        # PEGA O CERTIFICADO
        certificado1 = Certificado.objects.get(id=request.POST['certificado1'])

        if not 'myfile1' in request.FILES:
            messages.error(request, 'É preciso selecionar um arquivo')
            return redirect('projeto_importar', projeto_id)

        if 'certificado2' in request.POST and not 'myfile2' in request.FILES:
            messages.error(request, 'É preciso selecionar um arquivo')
            return redirect('projeto_importar', projeto_id)

        if 'certificado3' in request.POST and not 'myfile3' in request.FILES:
            messages.error(request, 'É preciso selecionar um arquivo')
            return redirect('projeto_importar', projeto_id)

        # CARREGA OS DADOS DO XLS
        dataset1 = Dataset()
        arquivo1 = request.FILES['myfile1']

        imported_data1 = dataset1.load(arquivo1.read())

        # VERIFICA O ARQUIVO A PARTIR DA LINHA 1
        for n in imported_data1[0:]:
            try:
                # BUSCA DOS DADOS DO CERTIFICADO
                dado = CertificadoElemento.objects.get(elemento__simbolo=str(n[0]), certificado=certificado1)

                medicao = Medicao()
                medicao.projeto = projeto
                medicao.concentracao_medicao = n[1]
                medicao.data = data1
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

                # TIPO DE FRAÇÃO DE MASSA
                if n[6] == '%':
                    medicao.tipo_fracao_massa = 0
                elif n[6] == 'PPM':
                    medicao.tipo_fracao_massa = 1
                elif n[6] == 'PPB':
                    medicao.tipo_fracao_massa = 2

                medicao.user = request.user
                medicao.save()
            except:
                messages.error(request, 'Erro ao importar dados.')
                return redirect('projeto_visualizar', projeto_id)

        if 'certificado2' in request.POST:
            # PEGA A DATA DO FORM
            data2 = request.POST['data2']
            data2 = data2[6:10] + '-' + data2[3:5] + '-' + data2[0:2]

            # PEGA O CERTIFICADO
            certificado2 = Certificado.objects.get(id=request.POST['certificado2'])

            # CARREGA OS DADOS DO XLS
            dataset2 = Dataset()
            arquivo2 = request.FILES['myfile2']

            imported_data2 = dataset2.load(arquivo2.read())

            # VERIFICA O ARQUIVO A PARTIR DA LINHA 1
            for n in imported_data2[0:]:
                try:
                    # BUSCA DOS DADOS DO CERTIFICADO
                    dado = CertificadoElemento.objects.get(elemento__simbolo=str(n[0]), certificado=certificado2)

                    medicao = Medicao()
                    medicao.projeto = projeto
                    medicao.concentracao_medicao = n[1]
                    medicao.data = data2
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
                    messages.error(request, 'Erro ao importar dados.')
                    return redirect('projeto_visualizar', projeto_id)

        if 'certificado3' in request.POST:
            # PEGA A DATA DO FORM
            data3 = request.POST['data3']
            data3 = data3[6:10] + '-' + data3[3:5] + '-' + data3[0:2]

            # PEGA O CERTIFICADO
            certificado3 = Certificado.objects.get(id=request.POST['certificado3'])

            # CARREGA OS DADOS DO XLS
            dataset3 = Dataset()
            arquivo3 = request.FILES['myfile3']

            imported_data3 = dataset3.load(arquivo3.read())

            # VERIFICA O ARQUIVO A PARTIR DA LINHA 1
            for n in imported_data3[0:]:
                try:
                    # BUSCA DOS DADOS DO CERTIFICADO
                    dado = CertificadoElemento.objects.get(elemento__simbolo=str(n[0]), certificado=certificado3)

                    medicao = Medicao()
                    medicao.projeto = projeto
                    medicao.concentracao_medicao = n[1]
                    medicao.data = data3
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
                    messages.error(request, 'Erro ao importar dados.')
                    return redirect('projeto_visualizar', projeto_id)

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

    media_concentracao = Medicao.objects.filter(projeto=projeto).order_by(
        'dados_elemento__elemento__simbolo').values(
        'dados_elemento__elemento__simbolo', 'dados_elemento__concentracao', 'dados_elemento__incerteza_expandida',
        'dados_elemento__incerteza_padrao', 'dados_elemento__tipo_fracao_massa', 'dados_elemento__tipo_concentracao',
        'tipo_fracao_massa').annotate(
        concentracao=Avg('concentracao_medicao'),
        incerteza_padrao=Avg('incerteza_padrao_medicao'), total=Count('id')).distinct()

    elementos = Medicao.objects.filter(projeto=projeto).order_by(
        'dados_elemento__elemento__simbolo').values_list(
        'dados_elemento__elemento__simbolo').annotate().distinct()
    lista_elementos = []
    lista_concentracao_medicao = []
    mediana = {}
    desvio_padrao = {}
    variancia = {}

    for elemento in elementos:
        lista_elementos = [obj[0] for obj in elementos]

    for i in lista_elementos:
        valores = Medicao.objects.filter(dados_elemento__elemento__simbolo=i, projeto=projeto)

        for valor in valores:
            lista_concentracao_medicao.append(valor.concentracao_medicao)

        mediana[i] = float(statistics.median(lista_concentracao_medicao))
        desvio_padrao[i] = float(statistics.pstdev(lista_concentracao_medicao))
        variancia[i] = float(statistics.pvariance(lista_concentracao_medicao))
        lista_concentracao_medicao = []

    context = {
        'projeto': projeto,
        'media_concentracao': media_concentracao,
        'mediana': mediana,
        'desvio_padrao': desvio_padrao,
        'variancia': variancia,
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


@login_required
def dados_certificados_importar(request):
    certificados = Certificado.objects.all()

    if request.method == 'POST':
        if not 'myfile1' in request.FILES:
            messages.error(request, 'É preciso selecionar um arquivo')
            return redirect('dados_certificados_importar')

        if 'certificado2' in request.POST and not 'myfile2' in request.FILES:
            messages.error(request, 'É preciso selecionar um arquivo')
            return redirect('dados_certificados_importar')

        if 'certificado3' in request.POST and not 'myfile3' in request.FILES:
            messages.error(request, 'É preciso selecionar um arquivo')
            return redirect('dados_certificados_importar')

        # PEGA O CERTIFICADO
        certificado1 = Certificado.objects.get(id=request.POST['certificado1'])

        # CARREGA OS DADOS DO XLS
        dataset1 = Dataset()
        arquivo1 = request.FILES['myfile1']
        imported_data1 = dataset1.load(arquivo1.read())

        # VERIFICA O ARQUIVO 1 A PARTIR DA LINHA 1
        for n in imported_data1[0:]:
            try:
                # PEGA O ELEMENTO
                elemento = Elemento.objects.get(simbolo=n[0])

                dados = CertificadoElemento()

                dados.certificado = certificado1
                dados.elemento = elemento
                if n[2]:
                    dados.concentracao = n[2]
                if n[3]:
                    dados.incerteza_expandida = n[3]
                if n[4]:
                    dados.incerteza_padrao = n[4]
                if n[5]:
                    dados.incerteza_combinada = n[5]
                if n[6]:
                    dados.intervalo_confianca = n[6]
                if n[7]:
                    dados.fracao_massa = n[7]

                # TIPO DE CONCENTRAÇÃO
                if n[1] == 'Certificado':
                    dados.tipo_concentracao = 0
                elif n[1] == 'Informado':
                    dados.tipo_concentracao = 1
                elif n[1] == 'Referência':
                    dados.tipo_concentracao = 2

                # TIPO DE FRAÇÃO DE MASSA
                if n[8] == '%':
                    dados.tipo_fracao_massa = 0
                elif n[8] == 'PPM':
                    dados.tipo_fracao_massa = 1
                elif n[8] == 'PPB':
                    dados.tipo_fracao_massa = 2

                dados.user = request.user
                dados.save()
            except:
                messages.error(request, 'Erro ao importar dados.')
                return redirect('dados_certificados')

        if 'certificado2' in request.POST:
            # PEGA O CERTIFICADO
            certificado2 = Certificado.objects.get(id=request.POST['certificado2'])

            # CARREGA OS DADOS DO XLS
            dataset2 = Dataset()
            arquivo2 = request.FILES['myfile2']
            imported_data2 = dataset2.load(arquivo2.read())

            # VERIFICA O ARQUIVO 2 A PARTIR DA LINHA 1
            for n in imported_data2[0:]:
                try:
                    # PEGA O ELEMENTO
                    elemento = Elemento.objects.get(simbolo=n[0])

                    dados = CertificadoElemento()

                    dados.certificado = certificado2
                    dados.elemento = elemento

                    if n[2]:
                        dados.concentracao = n[2]
                    if n[3]:
                        dados.incerteza_expandida = n[3]
                    if n[4]:
                        dados.incerteza_padrao = n[4]
                    if n[5]:
                        dados.incerteza_combinada = n[5]
                    if n[6]:
                        dados.intervalo_confianca = n[6]
                    if n[7]:
                        dados.fracao_massa = n[7]

                    # TIPO DE CONCENTRAÇÃO
                    if n[1] == 'Certificado':
                        dados.tipo_concentracao = 0
                    elif n[1] == 'Informado':
                        dados.tipo_concentracao = 1

                    # TIPO DE FRAÇÃO DE MASSA
                    if n[8] == '%':
                        dados.tipo_fracao_massa = 0
                    elif n[8] == 'PPM':
                        dados.tipo_fracao_massa = 1
                    elif n[8] == 'PPB':
                        dados.tipo_fracao_massa = 2

                    dados.user = request.user
                    dados.save()
                except:
                    messages.error(request, 'Erro ao importar dados.')
                    return redirect('dados_certificados')

        if 'certificado3' in request.POST:
            # PEGA O CERTIFICADO
            certificado3 = Certificado.objects.get(id=request.POST['certificado3'])

            # CARREGA OS DADOS DO XLS
            dataset3 = Dataset()
            arquivo3 = request.FILES['myfile3']
            imported_data3 = dataset3.load(arquivo3.read())

            # VERIFICA O ARQUIVO 3 A PARTIR DA LINHA 1
            for n in imported_data3[0:]:
                try:
                    # PEGA O ELEMENTO
                    elemento = Elemento.objects.get(simbolo=n[0])

                    dados = CertificadoElemento()

                    dados.certificado = certificado3
                    dados.elemento = elemento

                    if n[2]:
                        dados.concentracao = n[2]
                    if n[3]:
                        dados.incerteza_expandida = n[3]
                    if n[4]:
                        dados.incerteza_padrao = n[4]
                    if n[5]:
                        dados.incerteza_combinada = n[5]
                    if n[6]:
                        dados.intervalo_confianca = n[6]
                    if n[7]:
                        dados.fracao_massa = n[7]

                    # TIPO DE CONCENTRAÇÃO
                    if n[1] == 'Certificado':
                        dados.tipo_concentracao = 0
                    elif n[1] == 'Informado':
                        dados.tipo_concentracao = 1

                    # TIPO DE FRAÇÃO DE MASSA
                    if n[8] == '%':
                        dados.tipo_fracao_massa = 0
                    elif n[8] == 'PPM':
                        dados.tipo_fracao_massa = 1
                    elif n[8] == 'PPB':
                        dados.tipo_fracao_massa = 2

                    dados.user = request.user
                    dados.save()
                except:
                    messages.error(request, 'Erro ao importar dados.')
                    return redirect('dados_certificados')

        messages.success(request, 'Dados importados com sucesso')
        return redirect('dados_certificados')

    context = {
        'certificados': certificados,
    }

    return render(request, 'portal/dados_certificados_importar.html', context)
