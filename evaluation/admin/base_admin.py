# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from django.utils.html import mark_safe
from reversion_compare.compare import CompareObjects
from reversion_compare.helpers import patch_admin, html_diff, highlight_diff
from reversion_compare.admin import CompareVersionAdmin
import logging

logger = logging.getLogger(__name__)


"""
    Adicionar o seguinte código no fieldsets do Admin:
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
"""
class BaseAdmin(CompareVersionAdmin):
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


    def compare_inline_obj(self, model_class, obj_compare):
        """
        :param model_class: ex:  BostonAphasiaSentecesWrittenDictation model class
        :param obj_compare: reversion object
        :return: html string
        """
        result = ""

        # print ('****************')
        # for attr, value in obj_compare.__dict__.iteritems():
        #     print attr, value

        fields = [field for field in model_class._meta.fields]
        for field in fields:
            field_name = field.name
            field_verbose_name = field._verbose_name or ''

            # print ('****************')
            # print (obj_compare.M2O_CHANGE_INFO)
            # for attr, value in obj_compare.__dict__.iteritems():
            #     print attr, value

            if field_name not in ('id', 'bostonAphasia'):
                if obj_compare.M2O_CHANGE_INFO and 'changed_items' in obj_compare.M2O_CHANGE_INFO and len(obj_compare.M2O_CHANGE_INFO['changed_items']) > 0:

                    c = CompareObjects(field=obj_compare.field, field_name=field_name,
                                       obj=obj_compare.obj, version1=obj_compare.M2O_CHANGE_INFO['changed_items'][0][0],
                                       version2=obj_compare.M2O_CHANGE_INFO['changed_items'][0][1], is_reversed=False)

                    # if the object value changed, print the diff html
                    if c.changed() and c.value1 != c.value2:
                        result = u'%s<p>%s - %s<br>%s</p>' % (
                        result, field_name, field_verbose_name, html_diff(('- %s' % c.value1), ('+ %s' % c.value2)))
        if result:
            return mark_safe('<pre class="highlight">%s</pre>' % result)
        else:
            return
