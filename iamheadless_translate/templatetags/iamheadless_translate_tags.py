from django import template

from ..translations import translate


register = template.Library()


@register.simple_tag
def translation_for(key, language):
    return translate(key, language)
