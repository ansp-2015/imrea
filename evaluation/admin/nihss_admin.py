# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.nihss import NIHSS
from evaluation.forms.nihss_form import NIHSSForm


logger = logging.getLogger(__name__)

class NIHSSAdmin(BaseAdmin):
    form = NIHSSForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (None, {
            'fields': ('loc', 'loc_questions', 'loc_commands', 'best_gaze', 'visual', 'facial_palsy', ('motor_arm_left',
                       'motor_arm_right'), ('motor_leg_left', 'motor_leg_right'), 'limb_ataxia', 'sensory',
                       'best_language', 'dysarthria', 'extinction'),
            'description': {
                'fieldset': '_table2',
                'fieldset_total_points': 39,
                'fieldset_total_addend_fields': ('loc', 'loc_questions', 'loc_commands', 'best_gaze', 'visual',
                                                 'facial_palsy', 'motor_arm_left', 'motor_arm_right', 'motor_leg_left',
                                                 'motor_leg_right', 'limb_ataxia', 'sensory', 'best_language',
                                                 'dysarthria', 'extinction'),
                'fieldset_total_field': 'nihss_total'
            }
        })
    )

admin.site.register(NIHSS, NIHSSAdmin)
# Registrando no reversion-compare
patch_admin(NIHSS)
