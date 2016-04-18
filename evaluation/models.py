# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
CHOICES_VISUAL_IMAGES = (
    (5, _(u'Image as clear as seeing')),
    (4, _(u'Clear image')),
    (3, _(u'Moderately clear image')),
    (2, _(u'Blurred image')),
    (1, _(u'No image'))
)

CHOICES_CINE_IMAGES = (
    (5, _(u'As intense as performing the action')),
    (4, _(u'Intense')),
    (3, _(u'Moderately intense')),
    (2, _(u'Slightly intense')),
    (1, _(u'No sensation'))
)


class Patient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        names = self.name.split()
        return ''.join([n[0] for n in names if n[0].isupper()])

class KVIQ(models.Model):
    patient = models.ForeignKey(Patient)
    visual_images = models.IntegerField(choices=CHOICES_VISUAL_IMAGES)
    cine_images = models.IntegerField(choices=CHOICES_CINE_IMAGES)

    def __unicode__(self):
        return '%s' % self.patient
