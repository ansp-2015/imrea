# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from evaluation.models.kviq import KVIQ
from ..forms import KVIQForm
from .base_admin import BaseAdmin


class KVIQAdmin(BaseAdmin):

    form = KVIQForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Dominant limb'), {
            'fields': (('dominant_limb'),),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Neck flexion/extension'), {
            'fields': (('neck_visual_images', 'neck_cine_images'),),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('Bend your head as far as possible, first forward and then backward'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement')
                ),
            }
        }),
        (_(u'Shoulder shrugging'), {
            'fields': (('shoulder_elevation_visual_images', 'shoulder_elevation_cine_images'),),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('Raise both shoulders as high as possible without moving your head'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement')
                ),
            }
        }),
        (_(u'Shoulder flexion'), {
            'fields': (('shoulder_flexion_dom_visual_images', 'shoulder_flexion_dom_cine_images'),
                       ('shoulder_flexion_not_dom_visual_images', 'shoulder_flexion_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('Lift your non-dominant arm straight out in front of you and keep lifting until it is straight up high'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement')
                ),
            }
        }),
        (_(u'Elbow flexion'), {
            'fields': (('elbow_dom_visual_images', 'elbow_dom_cine_images'),
                       ('elbow_not_dom_visual_images', 'elbow_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and with your dominant arm straight out in front of you with your hand open and palm up'),
                    _('Bend the elbow on your dominant side as though you were going to touch your shoulder on the same side'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement')
                ),
            }
        }),
        (_(u'Thumb to finger tips'), {
            'fields': (('thumb_dom_visual_images', 'thumb_dom_cine_images'),
                       ('thumb_not_dom_visual_images', 'thumb_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs with your palms up'),
                    _('With your dominant hand, touch the tip of each finger with your thumb, start with the index finger and move along the fingers at the rate of about one finger/second'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement')
                ),
            }
        }),
        (_(u'Forward trunk flexion'), {
            'fields': (('trunk_visual_images', 'trunk_cine_images'),),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('Bend at the waist moving your trunk forward as far as possible then straighten up again'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement'),
                ),
            }
        }),
        (_(u'Knee extension'), {
            'fields': (('knee_dom_visual_images', 'knee_dom_cine_images'),
                       ('knee_not_dom_visual_images', 'knee_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('Extend your knee to raise the lower leg of your non-dominant side as close as possible to the horizontal then lower it'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement'),
                ),
            }
        }),
        (_(u'Hip abduction'), {
            'fields': (('hip_dom_visual_images', 'hip_dom_cine_images'),
                       ('hip_not_dom_visual_images', 'hip_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('Move the foot on your dominant side sideways about 30 cm (12 inches) then bring it back'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement'),
                ),
            }
        }),
        (_(u'Foot tapping'), {
            'fields': (('foot_tapping_dom_visual_images', 'foot_tapping_dom_cine_images'),
                       ('foot_tapping_not_dom_visual_images', 'foot_tapping_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('With your non-dominant leg tap your forefoot on the floor three times; about once/second while keeping your heel on the floor'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement'),
                ),
            }
        }),
        (_(u'Foot rotation'), {
            'fields': (('foot_rotation_dom_visual_images', 'foot_rotation_dom_cine_images'),
                       ('foot_rotation_not_dom_visual_images', 'foot_rotation_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
                'text': '<ol class="ol-container"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ol>' % (
                    _('Sit upright with the head straight and hands resting on your thighs'),
                    _('With your dominant leg, turn your forefoot out to the side as far as possible without moving your heel'),
                    _('Return to the start position. Now imagine the movement, concentrate on the clarity of the image'),
                    _('Indicate on the scale the quality of the imagined movement'),
                ),
            }
        }),
    )

admin.site.register(KVIQ, KVIQAdmin)
# Registrando no reversion-compare
#patch_admin(KVIQ)
