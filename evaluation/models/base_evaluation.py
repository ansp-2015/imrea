# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient

class BaseEvaluation(models.Model):
    """
    Classe abstrata para os Models de questionários                                            
    """
    patient = models.ForeignKey(Patient)
    
    
    class Meta:
        abstract = True
        ordering = ['patient']

    def __unicode__(self):
        return '%s' % self.patient
