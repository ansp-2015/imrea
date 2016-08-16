# -*- coding: utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from django.contrib.staticfiles import finders
from django.utils.translation import ugettext_lazy as _
from ..models.patient import Patient

register = template.Library()


#@register.simple_tag(takes_context=True)
def list_patients(context):
    patients = []

    user = context['user']

    patients = Patient.objects.all()

    retorno = {'evaluation_home_patients': []}
    if len(patients) > 0:
        for p in patients:
            retorno['evaluation_home_patients'].append(p)

    return retorno

# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('admin/tag_patients.html', takes_context=True)(list_patients)


@register.filter
@stringfilter
def translate_static(value, language):

    # Split language and country code
    codes = language.split('-')
    if len(codes) > 1:
        codes[1] = codes[1].upper()
        language = '_'.join(codes)
    base = codes[0]

    if finders.find('locale/%s/%s' % (language, value)):  # Looks for language and country code
        return 'locale/%s/%s' % (language, value)
    elif finders.find('locale/%s/%s' % (base, value)):  # Looks for language code
        return 'locale/%s/%s' % (base, value)
    else:
        return value
