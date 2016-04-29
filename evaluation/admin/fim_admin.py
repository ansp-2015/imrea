from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.fim import FIM, FIM_CHOICES_CATEGORY
from evaluation.forms import FIMAdminForm


class FIMAdmin(admin.ModelAdmin):

    form = FIMAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
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
    

admin.site.register(FIM, FIMAdmin)
