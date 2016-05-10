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