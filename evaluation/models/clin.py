# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation

CLIN_NEGLECT_CHOICES = (
    (1, _(u'Yes')),
    (2, _(u'No')),
) + BaseEvaluation.UN


class Clin(BaseEvaluation):
    neglect_1a = models.IntegerField(_('Neglect 1a'), choices=CLIN_NEGLECT_CHOICES)
    neglect_1b = models.IntegerField(_('Neglect 1b'), choices=CLIN_NEGLECT_CHOICES)
    neglect_1c = models.IntegerField(_('Neglect 1c'), choices=CLIN_NEGLECT_CHOICES)
    neglect_1d = models.IntegerField(_('Neglect 1d'), choices=CLIN_NEGLECT_CHOICES)
    neglect_2a = models.IntegerField(_('Neglect 2a'), choices=CLIN_NEGLECT_CHOICES)
    neglect_2b = models.IntegerField(_('Neglect 2b'), choices=CLIN_NEGLECT_CHOICES)
    neglect_2c = models.IntegerField(_('Neglect 2c'), choices=CLIN_NEGLECT_CHOICES)
    neglect_2d = models.IntegerField(_('Neglect 2d'), choices=CLIN_NEGLECT_CHOICES)
    neglect_3a = models.IntegerField(_('Neglect 3a'), choices=CLIN_NEGLECT_CHOICES)
    neglect_3b = models.IntegerField(_('Neglect 3b'), choices=CLIN_NEGLECT_CHOICES)
    neglect_3c = models.IntegerField(_('Neglect 3c'), choices=CLIN_NEGLECT_CHOICES)
    neglect_3d = models.IntegerField(_('Neglect 3d'), choices=CLIN_NEGLECT_CHOICES)
    neglect_4a = models.IntegerField(_('Neglect 4a'), choices=CLIN_NEGLECT_CHOICES)
    neglect_4b = models.IntegerField(_('Neglect 4b'), choices=CLIN_NEGLECT_CHOICES)
    neglect_4c = models.IntegerField(_('Neglect 4c'), choices=CLIN_NEGLECT_CHOICES)
    neglect_4d = models.IntegerField(_('Neglect 4d'), choices=CLIN_NEGLECT_CHOICES)

