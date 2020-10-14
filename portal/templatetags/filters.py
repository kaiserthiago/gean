import datetime

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db.models import Count
from django.utils.formats import localize

register = template.Library()


@register.filter(name='format')
def format(my_value):
    if not my_value:
        return '-'
    return my_value


@register.filter(name='moeda')
def moeda(my_value):
    if my_value:
        a = '{:,.2f}'.format(float(my_value))
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        return 'R$ ' + c.replace('v', '.')


@register.simple_tag(name='timestamp_to_date')
def timestamp_to_date(timestamp):
    import datetime
    data = datetime.date.fromtimestamp(int(timestamp))
    return data.strftime("%d/%m/%Y")


@register.simple_tag(name='balanco')
def balanco(receita, despesa):
    if receita and despesa:
        return moeda(receita - despesa)
    else:
        return '-'


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
    resultado = float((((media_concentracao - referencia)/referencia) * 100))
    a = '{:,.4f}'.format(resultado)
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')

@register.simple_tag(name='z_score')
def z_score(media_concentracao, referencia_concentracao, referencia_incerteza):
    if referencia_incerteza:
        resultado = float(((media_concentracao - referencia_concentracao)/referencia_incerteza))
        a = '{:,.4f}'.format(resultado)
        b = a.replace(',', 'v')
        c = b.replace('.', ',')
        return c.replace('v', '.')
    else:
        return '-'

@register.filter(name='has_group')
def has_group(user, group_name):
    from django.contrib.auth.models import Group

    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


@register.simple_tag(name='percentual')
def percentual(total, valor):
    if valor:
        percentual = ((valor / total) * 100)
        return '{:0,.0f} %'.format(percentual).replace('.', ',')
    else:
        return '0 %'