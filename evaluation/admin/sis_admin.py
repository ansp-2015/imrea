from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.sis import SIS, CHOICES_STRENGTH
from evaluation.forms import SISAdminForm


class SISAdmin(admin.ModelAdmin):

    form = SISAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
        }),
        (_(u'These questions are about the physical problems which may have occurred as a result of your stroke.'), {
            'fields': ('strength_arm', 'strength_hand', 'strength_leg', 'strength_foot'),
            'description': ((0, _(u'1. In the past week, how would you rate the strength of your....')),) +
            CHOICES_STRENGTH
        })
    )

admin.site.register(SIS, SISAdmin)

