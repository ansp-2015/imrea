# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
import logging

logger = logging.getLogger(__name__)


"""
    Adicionar o seguinte código no fieldsets do Admin:
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
"""
class BaseAdmin(admin.ModelAdmin):
    list_display = ('patient', 'get_patient_birthdate', 'period', 'last_update')
    list_filter = ('patient__name', 'period__period')
    ordering = ('patient', 'period', 'last_update')

    # Exibição do birthdate na lista de registros
    def get_patient_birthdate(self, obj):
        return obj.patient.birthdate
    get_patient_birthdate.short_description = _('Birthdate')
    get_patient_birthdate.admin_order_field = 'patient__birthdate'


    def add_context_variables(self, extra_context=None):
        """
        Override this method to add context variables.
        :param extra_context:
        :return:
        """
        extra_context = extra_context or {}
        return extra_context

    def add_view(self, request, form_url='', extra_context=None):
        """
        Override da view de adição para adicionar algumas variáveis extras de contexto
        """
        extra_context = self.add_context_variables(extra_context)

        return super(BaseAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Override da view de modificação para adicionar algumas variáveis extras de contexto
        """
        extra_context = self.add_context_variables(extra_context)

        # Campo read-only com a data de nascimento do paciente
        obj = self.get_object(request, unquote(object_id))
        extra_context['patient__birthdate'] = obj.patient.birthdate

        return super(BaseAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        """
        :return: Retorna somente o patient e period como read-only na modificação
        """
        if obj:
            return ['patient', 'period']
        else:
            return []
