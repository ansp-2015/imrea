# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Period(models.Model):
    """
    Periods of evaluation
    """
    period = models.CharField(max_length=40)
    parent = models.ForeignKey('evaluation.Period', verbose_name=_(u'Parent'), related_name='child', blank=True, null=True)
    
    def __unicode__(self):
        return '%s' % self.period


    @staticmethod
    def _find_evaluated_period(patient):
        periods = Period.objects.filter(baseevaluation__patient__id=patient.pk).distinct()
        return periods

    @staticmethod
    def _find_not_evaluated_period(patient):
        periods_evaluated = Period.objects.filter(baseevaluation__patient__id=patient.pk).distinct()

        periods_not_evaluated = Period.objects.exclude(pk__in=periods_evaluated)

        return periods_not_evaluated
