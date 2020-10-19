import math

from django import template

register = template.Library()


@register.filter(name='format')
def format(my_value):
    if not my_value:
        return '-'
    return my_value


@register.simple_tag(name='diferenca_absoluta')
def diferenca_absoluta(media, referencia):
    resultado = float((media - referencia))
    a = '{:,.4f}'.format(resultado)
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


@register.simple_tag(name='dpr')
def dpr(media_incerteza, media_concentracao):
    resultado = float(((media_incerteza / media_concentracao) * 100))
    a = '{:,.4f}'.format(resultado)
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


@register.simple_tag(name='er')
def er(media_concentracao, referencia):
    resultado = float((((media_concentracao - referencia) / referencia) * 100))
    a = '{:,.4f}'.format(resultado)
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


@register.simple_tag(name='en')
def en(media_concentracao, referencia_concentracao, media_incerteza, referencia_incerteza_expandida):
    if referencia_incerteza_expandida:
        resultado = float(
            (float(media_concentracao) - float(referencia_concentracao)) / math.sqrt(
                (float(media_incerteza) ** 2) + (float(referencia_incerteza_expandida) ** 2))
        )
        a = '{:,.4f}'.format(resultado)
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        return c.replace('v', '.')
    else:
        return '-'


@register.simple_tag(name='z_score')
def z_score(media_concentracao, referencia_concentracao, referencia_incerteza):
    if referencia_incerteza:
        resultado = float(((media_concentracao - referencia_concentracao) / referencia_incerteza))
        a = '{:,.4f}'.format(resultado)
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        return c.replace('v', '.')
    else:
        return '-'


@register.simple_tag(name='zeta_score')
def zeta_score(media_concentracao, referencia_concentracao, media_incerteza, referencia_incerteza_padrao):
    if referencia_incerteza_padrao:
        resultado = float(
            (float(media_concentracao) - float(referencia_concentracao)) / math.sqrt(
                (float(media_incerteza) ** 2) + (float(referencia_incerteza_padrao) ** 2))
        )
        a = '{:,.4f}'.format(resultado)
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        return c.replace('v', '.')
    else:
        return '-'


@register.simple_tag(name='z_horwitz')
def z_horwitz(media_concentracao, referencia_concentracao, fracao_massa_certificado, fracao_massa_medicao):
    if referencia_concentracao:
        if fracao_massa_medicao == 1 and fracao_massa_certificado == 0:  # MEDIÇÃO (PPM) E CERTIFICADO (%)
            media_concentracao = (media_concentracao / 10000) / 100
            referencia_concentracao = (referencia_concentracao / 10000) / 100

        elif fracao_massa_medicao == 2 and fracao_massa_certificado == 0:  # MEDIÇÃO (PPB) E CERTIFICADO (%)
            media_concentracao = (media_concentracao / 10000000) / 100
            referencia_concentracao = (referencia_concentracao / 10000000) / 100

        elif fracao_massa_medicao == 2 and fracao_massa_certificado == 2:  # MEDIÇÃO (PPB) E CERTIFICADO (PPM)
            media_concentracao = (media_concentracao / 1000) / 1000000000
            referencia_concentracao = (referencia_concentracao / 1000) / 1000000000

        elif fracao_massa_medicao == 2 and fracao_massa_certificado == 2:  # MEDIÇÃO (PPM) E CERTIFICADO (PPB)
            media_concentracao = (media_concentracao * 1000) / 1000000000000
            referencia_concentracao = (referencia_concentracao * 1000) / 1000000000000

        elif fracao_massa_medicao == 0 and fracao_massa_certificado == 0:  # MEDIÇÃO (%) CERTIFICADO (%)
            media_concentracao = media_concentracao / 100
            referencia_concentracao = referencia_concentracao / 100

        elif fracao_massa_medicao == 1 and fracao_massa_certificado == 1:  # MEDIÇÃO (PPM) CERTIFICADO (PPM)
            media_concentracao = media_concentracao / 1000000
            referencia_concentracao = referencia_concentracao / 1000000

        elif fracao_massa_medicao == 2 and fracao_massa_certificado == 2:  # MEDIÇÃO (PPB) E CERTIFICADO (PPB)
            media_concentracao = media_concentracao / 1000000000
            referencia_concentracao = referencia_concentracao / 1000000000

        # CÁLCULO DO DESVIO PADRÃO DE HORWITZ
        if media_concentracao > 0.138:
            dp_horwitz = 0.01 * math.sqrt(float(media_concentracao))
        elif media_concentracao >= 0.00000012:
            dp_horwitz = 0.022 * (float(media_concentracao) ** 0.8495)
        else:
            dp_horwitz = float(media_concentracao) * 0.022

        resultado = float(
            (float(media_concentracao) - float(referencia_concentracao)) / float(
                dp_horwitz)
        )

        a = '{:,.4f}'.format(resultado)
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        return c.replace('v', '.')
    else:
        return '-'