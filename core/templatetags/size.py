from django import template
from hurry.filesize import size

register = template.Library()


@register.filter(name='convert')
def convert_size(value):
    return size(value)