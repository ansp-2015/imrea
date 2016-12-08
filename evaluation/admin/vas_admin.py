# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.vas import VAS
from ..forms import VASForm


class VASAdmin(BaseAdmin):
    """
    Visual Analog Scale
    """

    form = VASForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
            }
        }),
        ('', {
            'fields': ('side', ('pain', 'anxiety')),
            'description' : {
                'fieldset': '_1col_panel',
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(VAS, VASAdmin)
