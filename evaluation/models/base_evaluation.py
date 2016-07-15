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
    date = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Date')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              )
    obs = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['patient']

    def __unicode__(self):
        return '%s' % self.patient


    @staticmethod
    def find_evaluated_period(patient):
        # Gets all evaluation objects (instances from subclasses of BaseEvaluation) for the given patient and period
        # that can be edit by the current user

        periods = []
        for p in Period.objects.all():
            for c in BaseEvaluation.__subclasses__():
                if c.objects.filter(patient_id=patient.pk, period_id=p.id).exists():
                    periods.append(p)
                    break;

        return periods


    @staticmethod
    def find_not_evaluated_period(patient):
        periods_evaluated = BaseEvaluation.find_evaluated_period(patient)

        periods_not_evaluated = Period.objects.exclude(pk__in=[o.id for o in periods_evaluated])

        return periods_not_evaluated



    @staticmethod
    def find_evaluated_objects(patient, period):

        # Gets all evaluation objects (instances from subclasses of BaseEvaluation) for the given patient and period
        # that can be edit by the current user
        evaluation_objects = [(c.__name__.lower(), c._meta.verbose_name.title(),
                               c.objects.filter(patient_id=patient.id, period_id=period.id).first())
                              for c in BaseEvaluation.__subclasses__()]

        result_evaluations = []
        for obj in evaluation_objects:
            if obj[2]:
                result_evaluations.append(obj[2])

        return result_evaluations
