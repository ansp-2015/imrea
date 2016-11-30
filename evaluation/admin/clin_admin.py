# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from evaluation.models.clin import Clin, CLIN_NEGLECT_CHOICES
from ..forms import ClinForm
from .base_admin import BaseAdmin


class ClinAdmin(BaseAdmin):
    form = ClinForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Line Crossing'), {
            'fields': ('neglect_1a', 'neglect_1b', 'neglect_1c', 'neglect_1d',
                       'neglect_2a', 'neglect_2b', 'neglect_2c', 'neglect_2d',
                       'neglect_3a', 'neglect_3b', 'neglect_3c', 'neglect_3d',
                       'neglect_4a', 'neglect_4b', 'neglect_4c', 'neglect_4d',
                       ),
            'description': {
                'fieldset': '_clin'
            }
        }),
        ('', {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )

admin.site.register(Clin, ClinAdmin)
# Registrando no reversion-compare
#patch_admin(Clin)
