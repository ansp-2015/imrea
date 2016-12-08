# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.verbal_fluency import VerbalFluency
from ..forms import VerbalFluencyForm


class VerbalFluencyAdmin(BaseAdmin):
    """
    Visual Analog Scale
    """

    form = VerbalFluencyForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
            }
        }),
        (_('FAS'), {
            'fields': (('fas_words'), ('fas_count'), ('fas_obs')),
            'description' : {
                'fieldset': '_1col_panel',
            }
        }),
        (_('Animals'), {
            'fields': (('animals_words'), ('animals_count'), ('animals_obs')),
            'description': {
                'fieldset': '_1col_panel',
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(VerbalFluency, VerbalFluencyAdmin)
