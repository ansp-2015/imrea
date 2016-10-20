# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class FTT(BaseEvaluation):
    """

    """

    paretic_hand_first = models.IntegerField(_('First'))
    healthy_hand_first = models.IntegerField()
    paretic_hand_second = models.IntegerField(_('Second'))
    healthy_hand_second = models.IntegerField()
    paretic_hand_third = models.IntegerField(_('Third'))
    healthy_hand_third = models.IntegerField()

    class Meta:
        verbose_name = _('FTT - Finger Tapping Test')
        verbose_name_plural = _('FTT - Finger Tapping Tests')