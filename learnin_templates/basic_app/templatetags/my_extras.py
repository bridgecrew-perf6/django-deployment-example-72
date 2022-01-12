#creating your own filters

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter(name='cut')
def cut(value, arg):
    #this cuts out all values of arg from the string    
    return value.replace(arg, '')

# register.filtere('cut', cut)
