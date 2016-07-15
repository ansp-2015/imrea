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
    periods = Period.objects.filter(bostonaphasia__patient__id=patient.pk).distinct() | \
              Period.objects.filter(clin__patient__id=patient.pk).distinct() | \
              Period.objects.filter(eeg__patient__id=patient.pk).distinct() | \
              Period.objects.filter(fim__patient__id=patient.pk).distinct() | \
              Period.objects.filter(fuglmeyer__patient__id=patient.pk).distinct() | \
              Period.objects.filter(had__patient__id=patient.pk).distinct() | \
              Period.objects.filter(kviq__patient__id=patient.pk).distinct() | \
              Period.objects.filter(sis__patient__id=patient.pk).distinct()

    return periods

