from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.sis import SIS
from evaluation.models.patient import Patient
from evaluation.forms import SISAdminForm



class SISAdmin(admin.ModelAdmin):

    form = SISAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
        }),
        (_(u'Neck'), {
            'fields': ('strength_arm', 'strength_hand', 'strength_leg', 'strength_foot'),
        })
    )

admin.site.register(SIS, SISAdmin)

