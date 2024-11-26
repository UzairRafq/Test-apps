from django import template
from testapp.utils import CURRENCY_LIST, COUNTRY_LIST


register =  template.Library()


@register.simple_tag
def currency_list():
    return CURRENCY_LIST


@register.simple_tag
def country_list():
    return COUNTRY_LIST

