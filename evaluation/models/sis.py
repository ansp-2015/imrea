from django.db import models
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient

CHOICES_STRENGTH = (
    (5, _(u'A lot of strength')),
    (4, _(u'Quite a bit of strength')),
    (3, _(u'Some strength')),
    (2, _(u'A little strength')),
    (1, _(u'No strength at all'))
)


class SIS(models.Model):
    patient = models.ForeignKey(Patient)
    strength_arm = models.IntegerField(choices=CHOICES_STRENGTH)
    strength_hand = models.IntegerField(choices=CHOICES_STRENGTH)
    strength_leg = models.IntegerField(choices=CHOICES_STRENGTH)
    strength_foot = models.IntegerField(choices=CHOICES_STRENGTH)

    def __unicode__(self):
        return '%s' % self.patient
