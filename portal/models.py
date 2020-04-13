from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
def get_user_name(self):
    return self.first_name + ' ' + self.last_name


User.add_to_class("__str__", get_user_name)


class AuditoriaMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

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

    class Meta:
        ordering = ['descricao']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.descricao


class Elemento(AuditoriaMixin):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    simbolo = models.CharField(max_length=2, verbose_name='Símbolo')

    class Meta:
        ordering = ['simbolo']
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'

    def __str__(self):
        return self.simbolo + ' - ' + self.descricao


class Certificado(AuditoriaMixin):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    codigo = models.CharField(max_length=150, verbose_name='Código')

    class Meta:
        ordering = ['descricao']
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return self.descricao + ' - ' + self.codigo


class CertificadoElemento(AuditoriaMixin):
    PERCENTUAL = 0
    PPM = 1
    PPB = 2

    TIPO_FRACAO = [
        [PERCENTUAL, '%'],
        [PPM, 'PPM'],
        [PPB, 'PPB']
    ]

    certificado = models.ForeignKey(Certificado, on_delete=models.CASCADE)
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)
    concentracao = models.DecimalField(verbose_name='Concentração', decimal_places=5, max_digits=10,
                                       validators=[MinValueValidator(0)])
    incerteza_expandida = models.DecimalField(verbose_name='Incerteza Expandida', decimal_places=5, max_digits=10,
                                              validators=[MinValueValidator(0)], null=True, blank=True)
    incerteza_padrao = models.DecimalField(verbose_name='Incerteza Padrão', decimal_places=5,
                                           max_digits=10,
                                           validators=[MinValueValidator(0)], default=0, null=True, blank=True)
    incerteza_confianca = models.DecimalField(verbose_name='Incerteza Confiança', decimal_places=5,
                                              max_digits=10,
                                              validators=[MinValueValidator(0)], default=0, null=True, blank=True)
    incerteza_combinada = models.DecimalField(verbose_name='Incerteza Combinada', decimal_places=5,
                                              max_digits=10,
                                              validators=[MinValueValidator(0)], default=0, null=True, blank=True)
    fracao_massa = models.DecimalField(verbose_name='Fração de massa', decimal_places=10, max_digits=15,
                                       validators=[MinValueValidator(0)], default=0)
    tipo_fracao_massa = models.IntegerField(choices=TIPO_FRACAO, default=0)

    class Meta:
        verbose_name = 'Dado do Certificado'
        verbose_name_plural = 'Dados dos Certificados'
        ordering = ['elemento', 'certificado']

    def __str__(self):
        return str(self.elemento) + ' - ' + str(self.certificado)


class Medicao(AuditoriaMixin):
    EXPANDIDA = 0
    PADRAO = 1
    CONFIANCA = 2
    COMBINADA = 3

    TIPO_INCERTEZA = [
        [EXPANDIDA, 'Expandida'],
        [PADRAO, 'Padrão'],
        [CONFIANCA, 'Confiança'],
        [COMBINADA, 'Combinada']
    ]

    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    dados_elemento = models.ForeignKey(CertificadoElemento, on_delete=models.CASCADE)
    tipo_incerteza = models.IntegerField(choices=TIPO_INCERTEZA, default=0)
    data = models.DateField()
    concentracao_medicao = models.DecimalField(verbose_name='Concentração da Medição', decimal_places=5, max_digits=10,
                                               validators=[MinValueValidator(0)], default=0)
    incerteza_padrao_medicao = models.DecimalField(verbose_name='Incerteza Padrão da Medição', decimal_places=5,
                                                   max_digits=10,
                                                   validators=[MinValueValidator(0)], default=0, null=True, blank=True)
    incerteza_expandida_medicao = models.DecimalField(verbose_name='Incerteza Expandida da Medição', decimal_places=5,
                                                      max_digits=10,
                                                      validators=[MinValueValidator(0)], default=0, null=True,
                                                      blank=True)
    incerteza_expandida_combinada = models.DecimalField(verbose_name='Incerteza Expandida Combinada da Medição',
                                                        decimal_places=5,
                                                        max_digits=10,
                                                        validators=[MinValueValidator(0)], default=0, null=True,
                                                        blank=True)

    class Meta:
        verbose_name = 'Medição'
        verbose_name_plural = 'Medições'
        ordering = ['-data']

    def __str__(self):
        return self.projeto.descricao + ' - ' + self.dados_elemento.elemento.simbolo + ' - ' + self.dados_elemento.certificado.codigo
