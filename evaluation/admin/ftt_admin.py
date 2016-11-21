from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from ..models.ftt import FTT
from ..forms.ftt_form import FTTForm
from .base_admin import BaseAdmin


class FTTAdmin(BaseAdmin):

    form = FTTForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        ('', {
            'fields': (('paretic_hand_first', 'healthy_hand_first'),
                       ('paretic_hand_second','healthy_hand_second'),
                       ('paretic_hand_third', 'healthy_hand_third')),
            'description': {
                'fieldset': '_table',
                'columns': ((0, ''), (1, u'Paretic hand'), (2, u'Healthy hand')),
            }
        }),
        ('', {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )


admin.site.register(FTT, FTTAdmin)
# Registrando no reversion-compare
patch_admin(FTT)

