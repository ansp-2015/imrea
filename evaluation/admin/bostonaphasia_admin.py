from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.bostonaphasia import BostonAphasia
from evaluation.forms import BostonAphasiaForm


class BostonAphasiaAdmin(admin.ModelAdmin):

    form = BostonAphasiaForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
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

