# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient

class BaseEvaluation(models.Model):
    """
    Classe abstrata para os Models de questionários                                            
    """

    # Utilizar esse valor para os casos em que o paciente não pode responder. "NAO TEM"
    NT = ((-10000, _(u'NT')),)
    # Utilizar esse valor nos casos em que o paciente faltou e não fez a avaliação. "MISSING DATA"
    MD = ((-100000, _(u'MD')),)

    
    patient = models.ForeignKey(Patient)
    
    class Meta:
        abstract = True
        ordering = ['patient']

    def __unicode__(self):
        return '%s' % self.patient
