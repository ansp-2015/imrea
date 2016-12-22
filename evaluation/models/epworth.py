# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class Epworth(BaseEvaluation):
    """
    Epworth Sleepniess Scale
    """


    EPWORTH_CHOICES = (
        (0, _(u'would never doze')),
        (1, _(u'slight chance of dozing')),
        (2, _(u'moderate chance of dozing')),
        (3, _(u'high chance of dozing')),
    ) + BaseEvaluation.UN

    sitting_reading = models.IntegerField(_('Sitting and reading'), choices=EPWORTH_CHOICES)
    watching_tv = models.IntegerField(_('Watching TV'), choices=EPWORTH_CHOICES)
    sitting_inactive_public = models.IntegerField(_('Sitting, inactive in a public place (e.g. a theatre or a meeting)'), choices=EPWORTH_CHOICES)
    car_passenger = models.IntegerField(_('As a passenger in a car for an hour without a break'), choices=EPWORTH_CHOICES)
    lying_down = models.IntegerField(_('Lying down to rest in the afternoon when circumstances permit'), choices=EPWORTH_CHOICES)
    sitting_talking = models.IntegerField(_('Sitting and talking to someone'), choices=EPWORTH_CHOICES)
    sitting_quietly_lunch = models.IntegerField(_('Sitting quietly after a lunch without alcohol'), choices=EPWORTH_CHOICES)
    car_traffic = models.IntegerField(_('In a car, while stopped for a few minutes in the traffic'), choices=EPWORTH_CHOICES)

    class Meta:
        verbose_name = _('Epworth Sleepiness')
        verbose_name_plural = _('Epwort Sleepiness')