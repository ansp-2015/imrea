from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from ..models import Eeg
from ..forms import EegForm
from .base_admin import BaseAdmin


class EegAdmin(BaseAdmin):

    form = EegForm
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

