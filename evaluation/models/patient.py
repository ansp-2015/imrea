# -*- coding: utf-8 -*-
from django.db import models
from django.forms import extras
from django.utils.translation import ugettext_lazy as _
from .period import Period


class Patient(models.Model):

    name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

    def find_evaluated_period(self):
        periods = Period._find_evaluated_period(self)
        return periods

    def find_not_evaluated_period(self):
        periods = Period._find_not_evaluated_period(self)
        return periods