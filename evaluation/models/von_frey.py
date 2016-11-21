# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class VonFrey(BaseEvaluation):
    """

    """

    sensibility1_forearm_right = models.DecimalField(_('Sensibility 1'), max_digits=5, decimal_places=2)
    sensibility1_forearm_left = models.DecimalField(max_digits=5, decimal_places=2)
    sensibility1_thenar_right = models.DecimalField(max_digits=5, decimal_places=2)
    sensibility1_thenar_left = models.DecimalField(max_digits=5, decimal_places=2)
    sensibility2_forearm_right = models.DecimalField(_('Sensibility 2'), max_digits=5, decimal_places=2)
    sensibility2_forearm_left = models.DecimalField(max_digits=5, decimal_places=2)
    sensibility2_thenar_right = models.DecimalField(max_digits=5, decimal_places=2)
    sensibility2_thenar_left = models.DecimalField(max_digits=5, decimal_places=2)
    algometer1_forearm_right = models.DecimalField(_('(Pain) Algometer 1'), max_digits=5, decimal_places=1)
    algometer1_forearm_left = models.DecimalField(max_digits=5, decimal_places=1)
    algometer1_thenar_right = models.DecimalField(max_digits=5, decimal_places=1)
    algometer1_thenar_left = models.DecimalField(max_digits=5, decimal_places=1)
    algometer2_forearm_right = models.DecimalField(_('(Pain) Algometer 2'), max_digits=5, decimal_places=1)
    algometer2_forearm_left = models.DecimalField(max_digits=5, decimal_places=1)
    algometer2_thenar_right = models.DecimalField(max_digits=5, decimal_places=1)
    algometer2_thenar_left = models.DecimalField(max_digits=5, decimal_places=1)
    algometer3_forearm_right = models.DecimalField(_('(Pain) Algometer 3'), max_digits=5, decimal_places=1)
    algometer3_forearm_left = models.DecimalField(max_digits=5, decimal_places=1)
    algometer3_thenar_right = models.DecimalField(max_digits=5, decimal_places=1)
    algometer3_thenar_left = models.DecimalField(max_digits=5, decimal_places=1)

    def __unicode__(self):
        return '%s - %s - Von Frey' % (self.patient, self.period)

    class Meta:
        verbose_name = _('Von Frey - Algometer')
        verbose_name_plural = _('Von Frey - Algometer')