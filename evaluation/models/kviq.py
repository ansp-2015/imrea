# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient
from . import BaseEvaluation

CHOICES_VISUAL_IMAGES = (
    (5, _(u'Image as clear as seeing')),
    (4, _(u'Clear image')),
    (3, _(u'Moderately clear image')),
    (2, _(u'Blurred image')),
    (1, _(u'No image'))
) + BaseEvaluation.UN

CHOICES_CINE_IMAGES = (
    (5, _(u'As intense as performing the action')),
    (4, _(u'Intense')),
    (3, _(u'Moderately intense')),
    (2, _(u'Slightly intense')),
    (1, _(u'No sensation'))
) + BaseEvaluation.UN

CHOICES_DOMINANT_LIMB = (
    (0, _(u'Left')),
    (1, _(u'Right'))
)

class KVIQ(BaseEvaluation):
    dominant_limb = models.IntegerField(_('Dominant limb'), choices=CHOICES_DOMINANT_LIMB)
    neck_visual_images = models.IntegerField(_('Neck visual images'), choices=CHOICES_VISUAL_IMAGES)
    neck_cine_images = models.IntegerField(_('Neck cine images'), choices=CHOICES_CINE_IMAGES)
    shoulder_elevation_visual_images = models.IntegerField(_('Shoulder elevation visual images'), choices=CHOICES_VISUAL_IMAGES)
    shoulder_elevation_cine_images = models.IntegerField(_('Shoulder elevation cine images'), choices=CHOICES_CINE_IMAGES)
    shoulder_flexion_dom_visual_images = models.IntegerField(_('Shoulder flexion dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    shoulder_flexion_dom_cine_images = models.IntegerField(_('Shoulder flexion dominant cine images'), choices=CHOICES_CINE_IMAGES)
    shoulder_flexion_not_dom_visual_images = models.IntegerField(_('Shoulder flexion not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    shoulder_flexion_not_dom_cine_images = models.IntegerField(_('Shoulder flexion not dominant cine images'), choices=CHOICES_CINE_IMAGES)
    elbow_dom_visual_images = models.IntegerField(_('Elbow dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    elbow_dom_cine_images = models.IntegerField(_('Elbow dominant cine images'), choices=CHOICES_CINE_IMAGES)
    elbow_not_dom_visual_images = models.IntegerField(_('Elbow not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    elbow_not_dom_cine_images = models.IntegerField(_('Elbow not dominant cine images'), choices=CHOICES_CINE_IMAGES)
    thumb_dom_visual_images = models.IntegerField(_('Thumb dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    thumb_dom_cine_images = models.IntegerField(_('Thumb dominant cine images'), choices=CHOICES_CINE_IMAGES)
    thumb_not_dom_visual_images = models.IntegerField(_('Thumb not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    thumb_not_dom_cine_images = models.IntegerField(_('Thumb not dominant cine images'), choices=CHOICES_CINE_IMAGES)
    trunk_visual_images = models.IntegerField(_('Trunk visual images'), choices=CHOICES_VISUAL_IMAGES)
    trunk_cine_images = models.IntegerField(_('Trunk cine images'), choices=CHOICES_CINE_IMAGES)
    knee_dom_visual_images = models.IntegerField(_('Knee dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    knee_dom_cine_images = models.IntegerField(_('Knee dominant cine images'), choices=CHOICES_CINE_IMAGES)
    knee_not_dom_visual_images = models.IntegerField(_('Knee not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    knee_not_dom_cine_images = models.IntegerField(_('Knee not dominant cine images'), choices=CHOICES_CINE_IMAGES)
    hip_dom_visual_images = models.IntegerField(_('Hip dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    hip_dom_cine_images = models.IntegerField(_('Hip dominant cine images'), choices=CHOICES_CINE_IMAGES)
    hip_not_dom_visual_images = models.IntegerField(_('Hip not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    hip_not_dom_cine_images = models.IntegerField(_('Hip not dominant cine images'), choices=CHOICES_CINE_IMAGES)
    foot_tapping_dom_visual_images = models.IntegerField(_('Foot tapping dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    foot_tapping_dom_cine_images = models.IntegerField(_('Foot tapping dominant cine images'), choices=CHOICES_CINE_IMAGES)
    foot_tapping_not_dom_visual_images = models.IntegerField(_('Foot tapping not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    foot_tapping_not_dom_cine_images = models.IntegerField(_('Foot tapping not dominant cine images'), choices=CHOICES_CINE_IMAGES)
    foot_rotation_dom_visual_images = models.IntegerField(_('Foot rotation dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    foot_rotation_dom_cine_images = models.IntegerField(_('Foot rotation dominant cine images'), choices=CHOICES_CINE_IMAGES)
    foot_rotation_not_dom_visual_images = models.IntegerField(_('Foot rotation not dominant visual images'), choices=CHOICES_VISUAL_IMAGES)
    foot_rotation_not_dom_cine_images = models.IntegerField(_('Foot rotation not dominant cine images'), choices=CHOICES_CINE_IMAGES)

    def __unicode__(self):
        return 'KVIQ: %s at %s' % (self.patient, self.period)