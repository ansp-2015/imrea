from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.fim import FIM
from evaluation.forms import FIMAdminForm
import logging

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
    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['FIM_CHOICES_CATEGORY'] = FIM.FIM_CHOICES_CATEGORY

        return super(FIMAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['FIM_CHOICES_CATEGORY'] = FIM.FIM_CHOICES_CATEGORY
        
        return super(FIMAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)
    

admin.site.register(FIM, FIMAdmin)
