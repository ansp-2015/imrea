# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html, mark_safe, escape
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging

from evaluation.models.fim import FIM
from evaluation.forms import FIMAdminForm

logger = logging.getLogger(__name__)


class FIMAdmin(admin.ModelAdmin):

    form = FIMAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Self Care'), {
            'fields': ('self_care_eating', 'self_care_grooming', 'self_care_bathing', \
                       'self_care_dressing_upper_body', 'self_care_dressing_lower_body', \
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
    )
    list_display = ('patient', 'get_patient_birthdate', 'period', 'date')
    ordering = ('patient', 'period', 'date')

    # Exibição do birthdate na lista de registros
    def get_patient_birthdate(self, obj):
        return obj.patient.birthdate
    get_patient_birthdate.short_description = _('Birthdate')
    get_patient_birthdate.admin_order_field = 'patient__birthdate'

    def add_view(self, request, form_url='', extra_context=None):
        """
        Override da view de adição para adicionar algumas variáveis extras de contexto
        """
        extra_context = extra_context or {}

        sorted_choices = sorted(FIM.FIM_CHOICES_CATEGORY, key=lambda x: x[0], reverse=False)
        extra_context['FIM_CHOICES_CATEGORY'] = sorted_choices

        return super(FIMAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Override da view de modificação para adicionar algumas variáveis extras de contexto
        """
        extra_context = extra_context or {}
        sorted_choices = sorted(FIM.FIM_CHOICES_CATEGORY, key=lambda x: x[0], reverse=False)
        extra_context['FIM_CHOICES_CATEGORY'] = sorted_choices

        # Campo read-only com a data de nascimento do paciente
        obj = self.get_object(request, unquote(object_id))
        extra_context['patient__birthdate'] = obj.patient.birthdate

        return super(FIMAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        """
        :return: Retorna somente o patient e period como read-only na modificação
        """
        if obj:
            return ['patient', 'period']
        else:
            return []

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
