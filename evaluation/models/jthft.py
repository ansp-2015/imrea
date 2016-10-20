# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class JTHFT(BaseEvaluation):
    """

    """

    paretic_hand_first = models.DurationField(_('First'))
    healthy_hand_first = models.DurationField()
    paretic_hand_second = models.DurationField(_('Second'))
    healthy_hand_second = models.DurationField()
    paretic_hand_third = models.DurationField(_('Third'))
    healthy_hand_third = models.DurationField()

    class Meta:
        verbose_name = _('JTHFT - Jebsen Taylor Hand Function Test')
        verbose_name_plural = _('JTHFT - Jebsen Taylor Hand Function Tests')