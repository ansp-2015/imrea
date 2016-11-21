# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class VerbalFluency(BaseEvaluation):
    """

    """
    fas_words = models.TextField('')
    fas_count = models.IntegerField(_('Word count'))
    fas_obs = models.TextField(_('Observation'))
    animals_words = models.TextField('')
    animals_count = models.IntegerField(_('Word count'))
    animals_obs = models.TextField(_('Observation'))

    class Meta:
        verbose_name = _('Verbal Fluency Test')
        verbose_name_plural = _('Verbal Fluency Tests')