# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.epworth import Epworth
from ..forms import EpworthForm


class EpworthAdmin(BaseAdmin):
    """
    Epworth Sleepniess Scale
    """
    HELP_TEXT = _(u'How likely are you to doze off or fall asleep in the following situations, in contrast to '
                  u'feeling just tired?<br />This refers to your usual way of life in recent times.<br />Even if'
                  u'you haven’t done some of these things recently try to work out how they would have affected you.')
    form = EpworthForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
                'choices': Epworth.EPWORTH_CHOICES,
                'help': HELP_TEXT
            }
        }),
        ('', {
            'fields': ('sitting_reading', 'watching_tv', 'sitting_inactive_public', 'car_passenger', 'lying_down',
                       'sitting_talking', 'sitting_quietly_lunch', 'car_traffic'),
            'description': {
                'fieldset': '_1col_panel',
                'fieldset_total_points': 24,
                'fieldset_total_addend_fields': ('sitting_reading', 'watching_tv', 'sitting_inactive_public',
                                                 'car_passenger', 'lying_down', 'sitting_talking',
                                                 'sitting_quietly_lunch', 'car_traffic'),
                'fieldset_total_field': 'epworth_total',
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(Epworth, EpworthAdmin)
