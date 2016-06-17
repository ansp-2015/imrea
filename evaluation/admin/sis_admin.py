from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from ..models.sis import SIS, CHOICES_STRENGTH
from ..forms import SISForm
from .base_admin import BaseAdmin


class SISAdmin(BaseAdmin):

    form = SISForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'These questions are about the physical problems which may have occurred as a result of your stroke.'), {
            'fields': ('strength_arm', 'strength_hand', 'strength_leg', 'strength_foot'),
            'description': {
                'columns': ((0, _(u'1. In the past week, how would you rate the strength of your....')),) +
                CHOICES_STRENGTH,
                'fieldset': '_radio_grid'
            }
        })
    )

admin.site.register(SIS, SISAdmin)

