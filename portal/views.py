from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from tablib import Dataset

from portal.forms import ProjetoForm
from portal.models import Projeto, Elemento, Certificado, CertificadoElemento


def home(request):
    return render(request, 'portal/home.html', {})


@login_required
def projeto_importar(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    certificados = Certificado.objects.all()

    if request.method == 'POST':
        # BUSCA DOS DADOS DO CERTIFICADO
        dados = CertificadoElemento.objects.filter(certificado_id=request.POST['certificado'])

        # CARREGA OS DADOS DO XLS
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())

        # VERIFICA O ARQUIVO A PARTIR DA LINHA 1
        for n in imported_data[0:]:
            try:
                aluno = get_object_or_404(Aluno, data_resposta=n[0], campus=n[50])
            except:
                aluno = None

            if not aluno:
                aluno = Aluno()

                aluno.data_resposta = str(n[0])
                aluno.campus = str(n[50])
                aluno.acesso_internet = str(n[51])
                aluno.possui_pc = str(n[52])
                aluno.possui_celular = str(n[53])
                aluno.possui_tablet = str(n[54])
                aluno.possui_tv = str(n[55])
                aluno.nivel_curso = str(n[56])
                aluno.deficiencia = str(n[57])
                aluno.transtorno = str(n[58])
                aluno.orientacao_enviada = str(n[59])
                aluno.avaliacao_orientacoes = int(n[60])
                aluno.conteudo_enviada = str(n[61])
                aluno.avaliacao_conteudo = int(n[62])
                aluno.avaliacao_moodle = int(n[64])
                aluno.melhoria_ava = str(n[65])
                aluno.docente_melhorar = str(n[66])
                aluno.auxilio = str(n[67])
                aluno.posicao = str(n[68])

                aluno.save()

        messages.success(request, 'Dados importados com sucesso')

    context = {
        'projeto': projeto,
        'certificados': certificados
    }

    return render(request, 'portal/projeto_importar.html', context)


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
