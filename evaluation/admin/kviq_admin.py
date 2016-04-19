from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.kviq import KVIQ
from evaluation.models.patient import Patient
from evaluation.forms import KVIQAdminForm



class KVIQAdmin(admin.ModelAdmin):

    form = KVIQAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
        }),
        (_(u'Neck'), {
            'fields': ('visual_images', 'cine_images'),
        })
    )

admin.site.register(KVIQ, KVIQAdmin)
admin.site.register(Patient)

