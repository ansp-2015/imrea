from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from ..models import BostonAphasia
from .base_admin import BaseAdmin


class BostonAphasiaAdmin(BaseAdmin):

    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Manual dominance.'), {
            'fields': (('write_or_distribute_card_deck_left_hand', 'write_or_distribute_card_deck_right_hand'),),
            'description': {
                'columns': ((0, _(u'Activity')), (1, _(u'Left hand')), (2, _(u'Right hand'))),
                'fieldset': '_table',
                'text': _(u'Instructions:...')
            }
        })
    )

admin.site.register(BostonAphasia, BostonAphasiaAdmin)
patch_admin(BostonAphasia)
