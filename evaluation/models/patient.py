# -*- coding: utf-8 -*-
from django.db import models
from django.forms import extras
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from .period import Period


class Patient(models.Model):

    name = models.CharField(_('Name'), max_length=50)
    birthdate = models.DateField(_('Date of birth'), blank=True, null=True)
    # Caracterização social do paciente:
    age = models.IntegerField(pgettext('Patient', u'Age'), blank=True, null=True)
    gender = models.CharField(pgettext('Patient', u'Gender'), max_length=100, blank=True, null=True)
    marital_status = models.CharField(pgettext('Patient', u'Marital status'), max_length=100, blank=True, null=True)
    profession = models.CharField(pgettext('Patient', u'Profession'), max_length=100, blank=True, null=True)
    occupation = models.CharField(pgettext('Patient', u'Occupation/work'), max_length=100, blank=True, null=True)
    schooling_level = models.CharField(pgettext('Patient', u'Schooling level'), max_length=100, blank=True, null=True)
    social_insurance_status = models.CharField(pgettext('Patient', u'Social insurance status'), max_length=100, blank=True, null=True)
    transportation_status = models.CharField(pgettext('Patient', u'Social insurance status'), max_length=100, blank=True, null=True)
    # Apoio familiar:
    fammily_ref_therapy = models.CharField(pgettext('Patient', u'Family member reference for therapy frequency'), max_length=100, blank=True, null=True)
    fammily_ref_home = models.CharField(pgettext('Patient', u'Family member reference at home'), max_length=100, blank=True, null=True)
    fammily_composition = models.CharField(pgettext('Patient', u'Family composition'), max_length=255, blank=True, null=True)
    quantity_ppl_home = models.IntegerField(pgettext('Patient', u'Number of people at home'), blank=True, null=True)
    # Aspectos econômicos:
    family_income = models.IntegerField(pgettext('Patient', u'Family income'), blank=True, null=True)
    family_income_average = models.IntegerField(pgettext('Patient', u'Average family income'), blank=True, null=True)
    # Dados demográficos:
    origin_city = models.CharField(pgettext('Patient', u'City of origin'), max_length=100, blank=True, null=True)
    conducting_source = models.CharField(pgettext('Patient', u'Conducting source'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.initials

    @property
    def initials(self):
        return ''.join(self.name.split()).upper()

    class Meta:
        ordering = ['name']
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')