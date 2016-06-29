# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .patient import Patient
from .period import Period

class BaseEvaluation(models.Model):
    """
    Classe abstrata para os Models de questionários
    """

    # Utilizar esse valor para os casos em que o paciente não pode responder. "NAO TEM"
    NT = ((-10000, _(u'NT')),)
    # Utilizar esse valor nos casos em que o paciente faltou e não fez a avaliação. "MISSING DATA"
    MD = ((-100000, _(u'MD')),)

    patient = models.ForeignKey(Patient, verbose_name=_(u'Patient'))
    period = models.ForeignKey(Period, verbose_name=_(u'Period'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_(u'Last update'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Date'))
    obs = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['patient']

    def __unicode__(self):
        return '%s' % self.patient

