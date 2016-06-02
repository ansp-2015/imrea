from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation

CLIN_NEGLECT_CHOICES = (
    (1, _(u'Yes')),
    (2, _(u'No')),
)


class Clin(BaseEvaluation):
    neglect_1a = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_1b = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_1c = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_1d = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_2a = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_2b = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_2c = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_2d = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_3a = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_3b = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_3c = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_3d = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_4a = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_4b = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_4c = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)
    neglect_4d = models.IntegerField(choices=CLIN_NEGLECT_CHOICES)

