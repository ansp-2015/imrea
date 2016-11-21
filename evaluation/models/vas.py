# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class VAS(BaseEvaluation):
    """

    """

    VAS_SIDE = (
        (0, _(u'Left')),
        (1, _(u'Right')),
    )

    side = models.IntegerField(_('More painful side'), choices=VAS_SIDE)
    pain = models.FloatField(_('Pain'))
    anxiety = models.FloatField(_('Anxiety'))

    class Meta:
        verbose_name = _('VAS - Visual Analog Scale')
        verbose_name_plural = _('VAS - Visual Analog Scales')