from django.db import models
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient
from . import BaseEvaluation 
 

NT = ((-10000, _(u'NT')),)

CHOICES_VISUAL_IMAGES = (
    (5, _(u'Image as clear as seeing')),
    (4, _(u'Clear image')),
    (3, _(u'Moderately clear image')),
    (2, _(u'Blurred image')),
    (1, _(u'No image'))
) + NT

CHOICES_CINE_IMAGES = (
    (5, _(u'As intense as performing the action')),
    (4, _(u'Intense')),
    (3, _(u'Moderately intense')),
    (2, _(u'Slightly intense')),
    (1, _(u'No sensation'))
) + NT

class KVIQ(BaseEvaluation):
    visual_images = models.IntegerField(choices=CHOICES_VISUAL_IMAGES)
    cine_images = models.IntegerField(choices=CHOICES_CINE_IMAGES)
