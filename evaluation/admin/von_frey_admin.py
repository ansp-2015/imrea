# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.von_frey import VonFrey
from evaluation.forms.von_frey_form import VonFreyForm


class VonFreyAdmin(BaseAdmin):
    """
    Visual Analog Scale
    """

    form = VonFreyForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
            }
        }),
        ('', {
            'fields': (('sensibility1_forearm_right', 'sensibility1_forearm_left', 
                        'sensibility1_thenar_right', 'sensibility1_thenar_left'),
                       ('sensibility2_forearm_right', 'sensibility2_forearm_left', 
                        'sensibility2_thenar_right', 'sensibility2_thenar_left'),
                       ('algometer1_forearm_right', 'algometer1_forearm_left',
                        'algometer1_thenar_right', 'algometer1_thenar_left'),
                       ('algometer2_forearm_right', 'algometer2_forearm_left',
                        'algometer2_thenar_right', 'algometer2_thenar_left'),
                       ('algometer3_forearm_right', 'algometer3_forearm_left',
                        'algometer3_thenar_right', 'algometer3_thenar_left',),
                       ),
            'description': {
                'fieldset': '_table_alg',
                'columns': ((0, _('Sequence')), (1, _('Paretic hand')), (2, _('Healthy hand'))),
            }
        }),
        ('', {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(VonFrey, VonFreyAdmin)

