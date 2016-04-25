from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.kviq import KVIQ
from evaluation.forms import KVIQAdminForm



class KVIQAdmin(admin.ModelAdmin):

    form = KVIQAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Neck'), {
            'fields': ('visual_images', 'cine_images'),
            'description': {
                'fieldset': '_1col',
            }
        })
    )

admin.site.register(KVIQ, KVIQAdmin)

