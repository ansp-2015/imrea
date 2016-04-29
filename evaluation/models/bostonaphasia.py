from django.db import models
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient
from . import BaseEvaluation 

class BostonAphasia(BaseEvaluation ):
    write_or_distribute_card_deck_left_hand = models.IntegerField(_(u'Write or distribute a card deck'))
    write_or_distribute_card_deck_right_hand = models.IntegerField(_(u'Write or distribute a card deck'))

