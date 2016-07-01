# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from ..models import MMSE
from ..forms import MMSEForm

logger = logging.getLogger(__name__)


class MMSEAdmin(BaseAdmin):

    form = MMSEForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (pgettext('MMSEAdmin', u'Orientation'), {
            'fields': ('orientation_day_week', 'orientation_day_month', 'orientation_month', 'orientation_year',
                       'orientation_time', 'orientation_place', 'orientation_institution', 'orientation_district',
                       'orientation_city', 'orientation_state',),
            'description': {
                'fieldset': '_1col_panel',
                'fieldset_label_col_width': '5',
                'fieldset_data_col_width': '7',
            }
        }),
        (pgettext('MMSEAdmin', u'Registration'), {
            'fields': ('registration_words',),
            'description': {
                'fieldset': '_1col_panel',
            }
        }),
        (pgettext('MMSEAdmin', u'Attention and Calculation'), {
            'fields': ('attention_calc',),
            'description': {
                'fieldset': '_1col_panel',
            }
        }),
        (pgettext('MMSEAdmin', u'Recall'), {
            'fields': ('recall_words',),
            'description': {
                'fieldset': '_1col_panel',
            }
        }),
        (pgettext('MMSEAdmin', u'Language'), {
            'fields': ('language_watch_pen', 'language_repeat', 'language_command',
                       'language_read', 'language_write', 'language_copy',),
            'description': {
                'fieldset': '_1col_panel',
                'fieldset_label_col_width': '5',
                'fieldset_data_col_width': '7',
            }
        }),
        (_(u''), {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col_panel'
            }
        }),
    )

admin.site.register(MMSE, MMSEAdmin)
# Registrando no reversion-compare
patch_admin(MMSE)
