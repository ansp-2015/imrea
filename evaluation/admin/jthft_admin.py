# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.jthft import JTHFT
from evaluation.forms.jthft_form import JTHFTForm


class JTHFTAdmin(BaseAdmin):
    """
    Visual Analog Scale
    """

    form = JTHFTForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
            }
        }),
        ('', {
            'fields': (('paretic_hand_first', 'healthy_hand_first'),
                       ('paretic_hand_second', 'healthy_hand_second'),
                       ('paretic_hand_third', 'healthy_hand_third')
                       ),
            'description' : {
                'fieldset': '_table',
                'columns': ((0, _('Sequence')), (1, _('Paretic hand')), (2, _('Healthy hand'))),
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(JTHFT, JTHFTAdmin)
