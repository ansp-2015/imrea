# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from ..models import HAD
from ..forms import HADForm

logger = logging.getLogger(__name__)


class HADAdmin(admin.ModelAdmin):

    form = HADForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (None, {
            'fields': (('tension',),
                       ('enjoy',),
                       ('frightened',),
                       ('laugh',),
                       ('worry',),
                       ('cheerful',),
                       ('ease',),
                       ('slowed',),
                       ('butterflies',),
                       ('appearance',),
                       ('restless',),
                       ('forward',),
                       ('panic',),
                       ('book',)),
            'description': {
                'fieldset': '_1col_with_choices'
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

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Override da view de modificação para adicionar algumas variáveis extras de contexto
        """
        extra_context = extra_context or {}

        # Campo read-only com a data de nascimento do paciente
        obj = self.get_object(request, unquote(object_id))
        extra_context['patient__birthdate'] = obj.patient.birthdate

        return super(HADAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        """
        :return: Retorna somente o patient e period como read-only na modificação
        """
        if obj:
            return ['patient', 'period']
        else:
            return []


admin.site.register(HAD, HADAdmin)
# Registrando no reversion-compare
patch_admin(HAD)
