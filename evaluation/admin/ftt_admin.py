from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from ..models.eeg import Eeg, EegFile
from ..forms.eeg_form import EegForm, EegFileInlineForm
from .base_admin import BaseAdmin


class EegFileAdminInline(admin.TabularInline):
    model = EegFile
    extra = 2
    form = EegFileInlineForm


class EegAdmin(BaseAdmin):

    form = EegForm
    inlines = [EegFileAdminInline]
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'File'), {
            'fields': ('eegtitle',),
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

