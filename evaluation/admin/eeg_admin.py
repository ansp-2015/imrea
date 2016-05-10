from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.eeg import Eeg
from evaluation.forms import EegAdminForm


class EegAdmin(admin.ModelAdmin):

    form = EegAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Arquivo'), {
            'fields': ('eegfile',),
            'description': {
                'fieldset': '_1col',
            }
        })
    )


admin.site.register(Eeg, EegAdmin)

