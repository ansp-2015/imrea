# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
from .base_admin import BaseAdmin
import logging
from evaluation.models.hamilton import Hamilton
from ..forms import HamiltonForm

logger = logging.getLogger(__name__)


class HamiltonAdmin(BaseAdmin):

    form = HamiltonForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (None, {
            'fields': (('mood',),
                       ('guilt',),
                       ('suicide',),
                       ('insomnia_early',),
                       ('insomnia_middle',),
                       ('insomnia_late',),
                       ('work',),
                       ('retardation',),
                       ('agitation',),
                       ('anxiety_psychic',),
                       ('anxiety_somatic',),
                       ('gastro',),
                       ('general',),
                       ('genital',),
                       ('hypochondriasis',),
                       ('weight_history', 'weight_weekly',),
                       ('insight',)),

            'description': {
                'fieldset': '_1col_with_choices',
                'fieldset_column_width': '12',
            },
        }),
        (_(u'Total'), {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col',
                'fieldset_total_points': '56',
                'fieldset_total_addend_fields': ('mood', 'guilt', 'suicide', 'insomnia_early',
                                                 'insomnia_middle', 'insomnia_late', 'work',
                                                 'retardation', 'agitation', 'anxiety_psychic', 'anxiety_somatic',
                                                 'gastro', 'general', 'genital', 'hypochondriasis', 'weight_history', 'weight_weekly',
                                                 'insight',),
                'fieldset_total_field': 'hamilton_total',
            }
        }),
    )


admin.site.register(Hamilton, HamiltonAdmin)
# Registrando no reversion-compare
#patch_admin(Hamilton)
