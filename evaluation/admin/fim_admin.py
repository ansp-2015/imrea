# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from ..models import FIM
from ..forms import FIMForm

logger = logging.getLogger(__name__)


class FIMAdmin(BaseAdmin):

    form = FIMForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Self Care'), {
            'fields': ('self_care_eating', 'self_care_grooming', 'self_care_bathing',
                       'self_care_dressing_upper_body', 'self_care_dressing_lower_body',
                       'self_care_toileting'),
            'description': {
                'fieldset': '_1col_panel'
            }
        }),
        (_(u'Sphincter'), {
            'fields': ('sphincter_bladder_mgt', 'sphincter_bowel_mgt'),
            'description': {
                'fieldset': '_1col_panel'
            }
        }),
        (_(u'Transfer'), {
            'fields': ('transfer_wheelchair', 'transfer_toilet', 'transfer_shower'),
            'description': {
                'fieldset': '_1col_panel'
            }
        }),
        (_(u'Locomotion'), {
            'fields': ('locomotion_wheelchair', 'locomotion_stairs',),
            'description': {
                'fieldset': '_1col_panel'
            }
        }),
        (_(u''), {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )

    def add_context_variables(self, extra_context=None):
        extra_context = extra_context or {}
        sorted_choices = sorted(FIM.FIM_CHOICES_CATEGORY, key=lambda x: x[0], reverse=False)
        extra_context['FIM_CHOICES_CATEGORY'] = sorted_choices

        return extra_context

    # Sobrescrevendo as comparações do restore
    def compare_self_care_eating(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_self_care_grooming(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_self_care_bathing(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_self_care_dressing_upper_body(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_self_care_dressing_lower_body(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_self_care_toileting(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_sphincter_bladder_mgt(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_sphincter_bowel_mgt(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_transfer_wheelchair(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_transfer_toilet(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_transfer_shower(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_locomotion_wheelchair(self, obj_compare):
        return self._compare_choice(obj_compare)

    def compare_locomotion_stairs(self, obj_compare):
        return self._compare_choice(obj_compare)

    def _compare_choice(self, obj_compare):
        value1 = ''
        value2 = ''
        for f in FIM.FIM_CHOICES_CATEGORY:
            if f[0] == obj_compare.value1:
                value1 = "%s - %s" % (f[0], f[1])
            if f[0] == obj_compare.value2:
                value2 = "%s - %s" % (f[0], f[1])
        ret = "<del style=\"background:#ffe6e6;\">%s</del> -> <ins style=\"background:#e6ffe6;\">%s</ins>" % (value1, value2)
        return mark_safe(ret)

admin.site.register(FIM, FIMAdmin)
# Registrando no reversion-compare
patch_admin(FIM)
