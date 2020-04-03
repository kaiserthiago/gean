from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class AuditoriaMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class Projeto(AuditoriaMixin):
    EM_ANDAMENTO = 1
    SUSPENSO = 2
    FINALIZADO = 3

    SITUACAO_CHOICES = [
        [EM_ANDAMENTO, 'Em Andamento'],
        [SUSPENSO, 'Suspenso'],
        [FINALIZADO, 'Finalizado']
    ]

    situacao = models.IntegerField(choices=SITUACAO_CHOICES, default=1)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_set')
    data_inicio = models.DateField()


class Elemento(AuditoriaMixin):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    simbolo = models.CharField(max_length=2, verbose_name='Símbolo')

    class Meta:
        ordering = ['simbolo']

    def __str__(self):
        return self.simbolo + ' - ' + self.descricao


class Certificado(AuditoriaMixin):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    codigo = models.CharField(max_length=150, verbose_name='Código')

    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao + ' - ' + self.codigo


class CertificadoElemento(AuditoriaMixin):
    certificado = models.ForeignKey(Certificado, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    concentracao = models.DecimalField(decimal_places=5, max_digits=10, validators=[MinValueValidator(0)])
    incerteza_expandida = models.DecimalField(decimal_places=5, max_digits=10, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name_plural = 'Dados dos Certificados'
        ordering = ['certificado', 'elemento']


class Medicao(AuditoriaMixin):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    data = models.DateField()

    class Meta:
        verbose_name_plural = 'Medições'
        ordering = ['-data']
