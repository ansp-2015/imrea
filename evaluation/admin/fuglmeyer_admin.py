# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from django.contrib.admin.utils import (unquote,)
from django.utils.safestring import mark_safe
from ..models.fuglmeyer import FuglMeyer
from ..forms import FuglMeyerForm
from .base_admin import BaseAdmin
import logging

logger = logging.getLogger(__name__)


class FuglMeyerAdmin(BaseAdmin):
    form = FuglMeyerForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Reflex activity'), {
            'fields': ('ue_reflex_activity_flex', 'ue_reflex_activity_ext',),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_01_ue_reflex_activity',
                'fieldset_total_points': 4,
                'fieldset_total_addend_fields': ('ue_reflex_activity_flex', 'ue_reflex_activity_ext',),
                'fieldset_total_field': 'ue_reflex_activity_total',
            }
        }),
        (_(u'Volitional movement within synergies'), {
            'fields': (  # flexor
                        'ue_vol_mov_syn_flex_shoulder_retrac', 'ue_vol_mov_syn_flex_shoulder_elev',
                        'ue_vol_mov_syn_flex_shoulder_abd', 'ue_vol_mov_syn_flex_shoulder_rot', 'ue_vol_mov_syn_flex_elbow_flex',
                        'ue_vol_mov_syn_flex_forearm_sup', 'ue_vol_mov_syn_flex_obs',
                        # extensor
                        'ue_vol_mov_syn_ext_shoulder', 'ue_vol_mov_syn_ext_elbow',
                        'ue_vol_mov_syn_ext_forearm', 'ue_vol_mov_syn_ext_obs',
                       ),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_02_ue_vol_mov_syn',
                'fieldset_total_points': 18,
                'fieldset_total_addend_fields': ('ue_vol_mov_syn_flex_shoulder_retrac', 'ue_vol_mov_syn_flex_shoulder_elev',
                        'ue_vol_mov_syn_flex_shoulder_abd', 'ue_vol_mov_syn_flex_shoulder_rot', 'ue_vol_mov_syn_flex_elbow_flex',
                        'ue_vol_mov_syn_flex_forearm_sup',
                        'ue_vol_mov_syn_ext_shoulder', 'ue_vol_mov_syn_ext_elbow',
                        'ue_vol_mov_syn_ext_forearm',),
                'fieldset_total_field': 'ue_vol_mov_syn_total',
            }
        }),
        (_(u'Volitional movement mixing synergies, without compensation'), {
            'fields': ('ue_vol_mov_mix_hand_spine', 'ue_vol_mov_mix_shoulder_flex', 'ue_vol_mov_mix_pron_sup'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('ue_vol_mov_mix_hand_spine', 'ue_vol_mov_mix_shoulder_flex', 'ue_vol_mov_mix_pron_sup'),
                'fieldset_total_field': 'ue_vol_mov_mix_total',
            }
        }),
        (_(u'Volitional movement with little or no synergy'), {
            'fields': ('ue_vol_mov_no_syn_shoulder_abd', 'ue_vol_mov_no_syn_shoulder_flex', 'ue_vol_mov_no_syn_pron_sup'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('ue_vol_mov_no_syn_shoulder_abd', 'ue_vol_mov_no_syn_shoulder_flex', 'ue_vol_mov_no_syn_pron_sup'),
                'fieldset_total_field': 'ue_vol_mov_no_syn_total',
            }
        }),
        (_(u'Normal reflex activity'), {
            'fields': ('ue_normal_reflex_activity', 'ue_normal_reflex_obs'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_total_points': 2,
                'fieldset_total_addend_fields': ('ue_normal_reflex_activity', ),
                'fieldset_total_field': 'ue_normal_reflex_total',
            }
        }),
        (_(u'Wrist'), {
            'fields': ('ue_wrist_stab_elbow_90', 'ue_wrist_flex_elbow_90', 'ue_wrist_stab_elbow_0',
                       'ue_wrist_flex_elbow_0', 'ue_wrist_circumduction',),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_helptext': _(u'Support may be provided at the elbow'),
                'fieldset_total_points':10,
                'fieldset_total_addend_fields': ('ue_wrist_stab_elbow_90', 'ue_wrist_flex_elbow_90', 'ue_wrist_stab_elbow_0',
                       'ue_wrist_flex_elbow_0', 'ue_wrist_circumduction',),
                'fieldset_total_field': 'ue_wrist_total',
            }
        }),
        (_(u'Hand'), {
            'fields': ('ue_hand_mass_flex', 'ue_hand_mass_ext', 'ue_hand_flex_pip_dip', 'ue_hand_thumb_adduction',
                       'ue_hand_thumb_opposition', 'ue_hand_cylinder_grip', 'ue_hand_spherical_grip'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_helptext': _(u'Support may be provided at the elbow to keep 90 flexion, no support at the wrist, compare with unaffected hand, the objects are interposed, active grasp'),
                'fieldset_total_points': 10,
                'fieldset_total_addend_fields': ('ue_hand_mass_flex', 'ue_hand_mass_ext', 'ue_hand_flex_pip_dip', 'ue_hand_thumb_adduction',
                       'ue_hand_thumb_opposition', 'ue_hand_cylinder_grip', 'ue_hand_spherical_grip'),
                'fieldset_total_field': 'ue_hand_total',
            }
        }),
        (_(u'Coordination/Speed'), {
            'fields': ('ue_coord_speed_tremor', 'ue_coord_speed_dysmetria', 'ue_coord_speed_time'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_helptext': _(
                    u'After one trial with both arms, blind-folded, tip of the index finger from knee to nose, 5 times as fast as possible'),
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('ue_coord_speed_tremor', 'ue_coord_speed_dysmetria', 'ue_coord_speed_time'),
                'fieldset_total_field': 'ue_coord_speed_total',
            }
        }),
        (_(u'Reflex activity (supine or sitting)'), {
            'fields': ('le_reflex_activity_achilles', 'le_reflex_activity_pattelar', 'le_reflex_activity_obs',),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_06_le_reflex_activity',
                'fieldset_total_points': 4,
                'fieldset_total_addend_fields': ('le_reflex_activity_achilles', 'le_reflex_activity_pattelar',),
                'fieldset_total_field': 'le_reflex_activity_total',
            }
        }),
        (_(u'Reflex activity (supine or sitting)'), {
            'fields': ('le_reflex_activity_achilles_pattelar', 'le_reflex_activity_achilles_pattelar_obs',),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_total_points': 2,
                'fieldset_total_addend_fields': ('le_reflex_activity_achilles_pattelar', ),
                'fieldset_total_field': 'le_reflex_activity_achilles_pattelar_total',
            }
        }),
        (_(u'Flexor synergy'), {
            'fields': ('le_vol_mov_syn_hip_flexion', 'le_vol_mov_syn_knee_flexion', 'le_vol_mov_syn_ankle_dorsiflexion', 'le_vol_mov_syn_flexion_obs'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_07_le_vol_mov_syn',
                'fieldset_helptext': _(
                    u'Start with leg fully extended at hip, knee, and ankle.Instruct the subject to “bring your knee to your chest”'),
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('le_vol_mov_syn_hip_flexion', 'le_vol_mov_syn_knee_flexion', 'le_vol_mov_syn_ankle_dorsiflexion', ),
                'fieldset_total_field': 'le_vol_mov_syn_flexion_total',
            }
        }),
        (_(u'Extensor synergy'), {
            'fields': ('le_vol_mov_syn_hip_extension', 'le_vol_mov_syn_hip_adduction', 'le_vol_mov_syn_knee_extension',
                       'le_vol_mov_syn_ankle_flexion', 'le_vol_mov_syn_extension_obs'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_08_le_vol_mov_syn_ext',
                'fieldset_helptext': _(
                    u'Start in 90 degrees hip flexion, 90 degrees knee flexion and ankle dorsiflexion. Slight resistance should be applied in adduction to ensure subject is actively doing it. Instruct the subject to "push your foot down and kick down and back”.'),
                'fieldset_total_points': 8,
                'fieldset_total_addend_fields': ('le_vol_mov_syn_hip_extension', 'le_vol_mov_syn_hip_adduction', 'le_vol_mov_syn_knee_extension',
                       'le_vol_mov_syn_ankle_flexion',),
                'fieldset_total_field': 'le_vol_mov_syn_extension_total',
            }
        }),
        (_(u'Movement combining synergies '), {
            'fields': ('le_vol_mov_mix_syn_knee', 'le_vol_mov_mix_syn_knee_obs',
                       'le_vol_mov_mix_syn_ankle', 'le_vol_mov_mix_syn_ankle_obs',
                       'le_vol_mov_no_syn_knee', 'le_vol_mov_no_syn_knee_obs',
                       'le_vol_mov_no_syn_ankle', 'le_vol_mov_no_syn_ankle_obs'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_total_points': 8,
                'fieldset_total_addend_fields': ('le_vol_mov_mix_syn_knee', 'le_vol_mov_mix_syn_ankle',
                       'le_vol_mov_no_syn_knee', 'le_vol_mov_no_syn_ankle', ),
                'fieldset_total_field': 'le_vol_mov_mix_syn_total',
            }
        }),
        (_(u'Coordination/speed of lower extremities'), {
            'fields': ('le_coord_speed_tremor', 'le_coord_speed_dysmetria', 'le_coord_speed_time', 'le_coord_speed_obs'),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_00_title_and_fields',
                'fieldset_helptext': _(
                    u'Sittings position, both limbis, eyes closed, ankle to knee to ankle, 5 times  move as fast as possible'),
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('le_coord_speed_tremor', 'le_coord_speed_dysmetria', 'le_coord_speed_time', ),
                'fieldset_total_field': 'le_coord_speed_total',
            }
        }),

    (_(u''), {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )

    def _add_context_variables(self, extra_context=None):
        extra_context = extra_context or {}

        extra_context['UE_VOL_MOV_SYN_FLEX_TEXT'] = self.UE_VOL_MOV_SYN_FLEX_TEXT
        extra_context['UE_VOL_MOV_SYN_EXT_TEXT'] = self.UE_VOL_MOV_SYN_EXT_TEXT

        return extra_context

    def add_view(self, request, form_url='', extra_context=None):
        """
        Override da view de adição para adicionar algumas variáveis extras de contexto
        """
        extra_context = self._add_context_variables(extra_context)

        return super(FuglMeyerAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Override da view de modificação para adicionar algumas variáveis extras de contexto
        """
        extra_context = self._add_context_variables(extra_context)

        # Campo read-only com a data de nascimento do paciente
        obj = self.get_object(request, unquote(object_id))
        extra_context['patient__birthdate'] = obj.patient.birthdate

        return super(FuglMeyerAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)


    UE_VOL_MOV_SYN_FLEX_TEXT = '%s' % pgettext('UE_VOL_MOV_SYN_FLEX_TEXT', u"Flexor synergy - Instruct the patient to fully supinate his/her forearm, flex the elbow, and bring the hand to the ear of the affected side. The shoulder should be abducted at least 90 degrees. The starting position should be that of full extensor synergy. If the patient cannot actively achieve the starting position, the limb may be passively placed extended towards opposite knee in shoulder adduction/internal rotation, elbow extension, and forearm pronation. Test 3x on the affected side and score best movement at each joint.")
    UE_VOL_MOV_SYN_EXT_TEXT = '%s' % pgettext('UE_VOL_MOV_SYN_EXT_TEXT', u"Extensor synergy - Instruct the patient to adduct & internally rotate the shoulder, extend his arm towards the unaffected knee with the forearm pronated. The starting position should be that the limb is passively placed at patient’s side in elbow flexion and supination. The examiner must ensure that the patient does not rotate and flex the trunk forward, thereby allowing gravity to assist with the movement. The pectoralis major and triceps brachii tendons may be palpated to assess active movement. Test 3x on the affected side and score best movement at each joint.")



admin.site.register(FuglMeyer, FuglMeyerAdmin)

