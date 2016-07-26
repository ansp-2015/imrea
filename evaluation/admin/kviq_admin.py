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
            }
        }),
        (_(u'Shoulder elevation'), {
            'fields': (('shoulder_elevation_visual_images', 'shoulder_elevation_cine_images'),),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Shoulder flexion'), {
            'fields': (('shoulder_flexion_dom_visual_images', 'shoulder_flexion_dom_cine_images'),
                       ('shoulder_flexion_not_dom_visual_images', 'shoulder_flexion_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Elbow'), {
            'fields': (('elbow_dom_visual_images', 'elbow_dom_cine_images'),
                       ('elbow_not_dom_visual_images', 'elbow_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Thumb'), {
            'fields': (('thumb_dom_visual_images', 'thumb_dom_cine_images'),
                       ('thumb_not_dom_visual_images', 'thumb_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Trunk'), {
            'fields': (('trunk_visual_images', 'trunk_cine_images'),),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Knee'), {
            'fields': (('knee_dom_visual_images', 'knee_dom_cine_images'),
                       ('knee_not_dom_visual_images', 'knee_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Hip'), {
            'fields': (('hip_dom_visual_images', 'hip_dom_cine_images'),
                       ('hip_not_dom_visual_images', 'hip_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Foot tapping'), {
            'fields': (('foot_tapping_dom_visual_images', 'foot_tapping_dom_cine_images'),
                       ('foot_tapping_not_dom_visual_images', 'foot_tapping_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_(u'Foot rotation'), {
            'fields': (('foot_rotation_dom_visual_images', 'foot_rotation_dom_cine_images'),
                       ('foot_rotation_not_dom_visual_images', 'foot_rotation_not_dom_cine_images')),
            'description': {
                'fieldset': '_1col',
            }
        }),
    )

admin.site.register(KVIQ, KVIQAdmin)
# Registrando no reversion-compare
patch_admin(KVIQ)
