# -*- coding: utf-8 -*-

from django import template
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