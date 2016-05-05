# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .patient import Patient
from .period import Period

class BaseEvaluation(models.Model):
    """
    Classe abstrata para os Models de questionários                                            
    """
    patient = models.ForeignKey(Patient, verbose_name=_(u'Patient'))
    period = models.ForeignKey(Period, verbose_name=_(u'Period'))
    date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['patient']

    def __unicode__(self):
        return '%s' % self.patient
