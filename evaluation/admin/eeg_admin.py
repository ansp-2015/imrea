from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
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
        (_(u'File'), {
            'fields': ('eegtitle', 'eegfile',),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u''), {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )


admin.site.register(Eeg, EegAdmin)
# Registrando no reversion-compare
patch_admin(Eeg)