# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from . import BaseEvaluation


class FuglMeyer(BaseEvaluation):
    # I - Reflex activity
    FUGLM_UE_REFLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_REFLEX_ACTIVITY", u'None')),
        (2, pgettext("FUGLM_UE_REFLEX_ACTIVITY", u'Can be elicited')),
    )
    # II - Volitional movement within synergies
    FUGLM_UE_VOL_MOV_SYN_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_SYN_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_VOL_MOV_SYN_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_VOL_MOV_SYN_ACTIVITY", u'Full')),
    )
    # III - Volitional movement mixing synergies, without compensation
    FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY", u'Cannot be performed, hand in front of SIAS')),
        (1, pgettext("FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY", u'Hand behind of SIAS (without compensation)')),
        (2, pgettext("FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY", u'Hand to lumbar spine (without compensation)')),
    )
    FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY", u'Immediate abduction or elbow flexion')),
        (1, pgettext("FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY", u'Abduction or elbow flexion during movement')),
        (2, pgettext("FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY", u'Complete flexion 90°, maintains 0° in elbow')),
    )
    FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY", u'No pronation/supination, starting position impossible')),
        (1, pgettext("FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY", u'Limited pronation/supination, maintains position')),
        (2, pgettext("FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY", u'Mantém posição com ADM limitada de P/S')),
    )
    # IV. Volitional movement with little or no synergy
    FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY", u'Immediate supination or elbow flexion')),
        (1, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY", u'Supination or elbow flexion during movement')),
        (2, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY", u'Abduction 90°, maintains extension and pronation')),
    )
    FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY", u'Immediate abduction or elbow flexion')),
        (1, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY", u'Abduction or elbow flexion during movement')),
        (2, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY", u'Complete flexion, maintains 0° in elbow')),
    )
    FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY", u'No pronation/supination, starting position impossible')),
        (1, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY", u'Limited pronation/supination, maintains extension')),
        (2, pgettext("FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY", u'Full pronation/supination, maintains elbow extension')),
    )
    # V. Normal reflex activity evaluated
    FUGLM_UE_NORMAL_REFLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_NORMAL_REFLEX_ACTIVITY", u'2 of 3 reflexes markedly hyperactive')),
        (1, pgettext("FUGLM_UE_NORMAL_REFLEX_ACTIVITY", u'1 reflex markedly hyperactive or at least 2 reflexes lively')),
        (2, pgettext("FUGLM_UE_NORMAL_REFLEX_ACTIVITY", u'Maximum of 1 reflex lively, none hyperactive')),
    )
    # B. WRIST
    FUGLM_UE_WRIST_STAB_ELBOW_90_ACTIVITY = (
        (0, pgettext("FUGLM_UE_WRIST_STAB_ELBOW_90_ACTIVITY", u'Less than 15° active dorsiflexion')),
        (1, pgettext("FUGLM_UE_WRIST_STAB_ELBOW_90_ACTIVITY", u'Dorsiflexion 15°, no resistance is taken')),
        (2, pgettext("FUGLM_UE_WRIST_STAB_ELBOW_90_ACTIVITY", u'Maintains position against resistance')),
    )
    FUGLM_UE_WRIST_FLEX_ELBOW_90_ACTIVITY = (
        (0, pgettext("FUGLM_UE_WRIST_FLEX_ELBOW_90_ACTIVITY", u'Cannot be performed')),
        (1, pgettext("FUGLM_UE_WRIST_FLEX_ELBOW_90_ACTIVITY", u'Can hold position but weak')),
        (2, pgettext("FUGLM_UE_WRIST_FLEX_ELBOW_90_ACTIVITY", u'Maintains position against resistance')),
    )
    FUGLM_UE_WRIST_STAB_ELBOW_0_ACTIVITY = (
        (0, pgettext("FUGLM_UE_WRIST_STAB_ELBOW_0_ACTIVITY", u'Less than 15° active dorsiflexion')),
        (1, pgettext("FUGLM_UE_WRIST_STAB_ELBOW_0_ACTIVITY", u'Dorsiflexion 15°, no resistance is taken')),
        (2, pgettext("FUGLM_UE_WRIST_STAB_ELBOW_0_ACTIVITY", u'Maintains position against resistance')),
    )
    FUGLM_UE_WRIST_FLEX_ELBOW_0_ACTIVITY = (
        (0, pgettext("FUGLM_UE_WRIST_FLEX_ELBOW_0_ACTIVITY", u'Cannot perform volitionally')),
        (1, pgettext("FUGLM_UE_WRIST_FLEX_ELBOW_0_ACTIVITY", u'Limited active range of motion')),
        (2, pgettext("FUGLM_UE_WRIST_FLEX_ELBOW_0_ACTIVITY", u'Full active range of motion, smoothly')),
    )
    FUGLM_UE_WRIST_CIRCUMDUCTION_ACTIVITY = (
        (0, pgettext("FUGLM_UE_WRIST_CIRCUMDUCTION_ACTIVITY", u'Cannot perform volitionally')),
        (1, pgettext("FUGLM_UE_WRIST_CIRCUMDUCTION_ACTIVITY", u'Jerky movement or incomplete')),
        (2, pgettext("FUGLM_UE_WRIST_CIRCUMDUCTION_ACTIVITY", u'Complete and smooth circumduction')),
    )

    # C. HAND
    FUGLM_UE_HAND_MASS_FLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_MASS_FLEX_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_MASS_FLEX_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_MASS_FLEX_ACTIVITY", u'Full')),
    )
    FUGLM_UE_HAND_MASS_EXT_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_MASS_EXT_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_MASS_EXT_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_MASS_EXT_ACTIVITY", u'Full')),
    )
    FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY", u'Full')),
    )
    FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY", u'Full')),
    )
    FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY", u'Full')),
    )
    FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY", u'Full')),
    )
    FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY", u'Full')),
    )

    # D. COORDINATION/SPEED
    FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY = (
        (0, pgettext("FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY", u'Full')),
    )
    FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY = (
        (0, pgettext("FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY", u'Full')),
    )
    FUGLM_UE_COORD_SPEED_TIME_ACTIVITY = (
        (0, pgettext("FUGLM_UE_COORD_SPEED_TIME_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_UE_COORD_SPEED_TIME_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_UE_COORD_SPEED_TIME_ACTIVITY", u'Full')),
    )
    # E. LOWER EXTREMITY
    # I. Reflex activity, supine position
    FUGLM_LE_REFLEX_ACTIVITY = (
        (0, pgettext("FUGLM_LE_REFLEX_ACTIVITY", u'None')),
        (2, pgettext("FUGLM_LE_REFLEX_ACTIVITY", u'Full')),
    )
    FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY = (
        (0, pgettext("FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY", u'None')),
        (1, pgettext("FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY", u'Partial')),
        (2, pgettext("FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY", u'Full')),
    )

    # II. Volitional movement within synergies
    FUGLM_LE_VOL_MOV_SYN = (
        (0, pgettext("FUGLM_LE_VOL_MOV_SYN", u'None')),
        (1, pgettext("FUGLM_LE_VOL_MOV_SYN", u'Partial')),
        (2, pgettext("FUGLM_LE_VOL_MOV_SYN", u'Full')),
    )
    # III. Volitional movement mixing synergies
    FUGLM_LE_VOL_MOV_MIX_SYN = (
        (0, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN", u'None')),
        (1, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN", u'Partial')),
        (2, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN", u'Full')),
    )
    FUGLM_LE_VOL_MOV_NO_SYN = (
        (0, pgettext("FUGLM_LE_VOL_MOV_NO_SYN", u'None')),
        (1, pgettext("FUGLM_LE_VOL_MOV_NO_SYN", u'Partial')),
        (2, pgettext("FUGLM_LE_VOL_MOV_NO_SYN", u'Full')),
    )
    # F. COORDINATION/SPEED
    FUGLM_LE_COORD_SPEED = (
        (0, pgettext("FUGLM_LE_COORD_SPEED", u'None')),
        (1, pgettext("FUGLM_LE_COORD_SPEED", u'Partial')),
        (2, pgettext("FUGLM_LE_COORD_SPEED", u'Full')),
    )

    # A. UPPER EXTREMITY, sitting position
    # I - Reflex activity
    # Reflex activity - Flexors: biceps and finger flexors
    ue_reflex_activity_flex = models.IntegerField(_('Flexors: biceps and finger flexors'), choices=FUGLM_UE_REFLEX_ACTIVITY)
    # Reflex activity - Extensors: triceps
    ue_reflex_activity_ext = models.IntegerField(_('Extensors: triceps'), choices=FUGLM_UE_REFLEX_ACTIVITY)

    # II - Volitional movement within synergies
    # Flexor synergy - Shoulder retraction
    ue_vol_mov_syn_flex_shoulder_retrac = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder retraction'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    # Flexor synergy - Shoulder elevation
    ue_vol_mov_syn_flex_shoulder_elev = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder elevation'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    # Flexor synergy - Shoulder abduction (90)
    ue_vol_mov_syn_flex_shoulder_abd = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder abduction (90)'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY, )
    # Flexor synergy - Shoulder external rotation
    ue_vol_mov_syn_flex_shoulder_rot = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder external rotation'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY, )
    # Flexor synergy - Elbow flexion
    ue_vol_mov_syn_flex_elbow_flex = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Elbow flexion'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    # Flexor synergy - Forearm supination
    ue_vol_mov_syn_flex_forearm_sup = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Forearm supination'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    ue_vol_mov_syn_flex_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # Extensor synergy - shoulder adduction / internal rotation
    ue_vol_mov_syn_ext_shoulder = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'shoulder adduction / internal rotation'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    # Extensor synergy - elbow extension
    ue_vol_mov_syn_ext_elbow = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'elbow extension'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    # Extensor synergy - forearm pronation
    ue_vol_mov_syn_ext_forearm = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'forearm pronation'), choices=FUGLM_UE_VOL_MOV_SYN_ACTIVITY)
    ue_vol_mov_syn_ext_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # III - Volitional movement mixing synergies, without compensation
    # Hand to lumbar spine
    vol_mov_mix_hand_spine = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Hand to lumbar spine'), choices=FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY)
    # Shoulder flexion 0-90
    vol_mov_mix_shoulder_flex = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder flexion 0-90 elbow at 0 pronation-supination 0'), choices=FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY)
    # Pronation-supination
    vol_mov_mix_pron_sup = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Pronation-supination elbow at 90 shoulder at 0'), choices=FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY)

    # IV. Volitional movement with little or no synergy
    # Shoulder abduction 0 - 90
    ue_vol_mov_no_syn_shoulder_abd = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder abduction 0 - 90 elbow at 0 forearm pronated'), choices=FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY)
    # Shoulder flexion 90- 180
    ue_vol_mov_no_syn_shoulder_flex = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder flexion 90- 180 elbow at 0pronation-supination 0'), choices=FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY)
    # Pronation/supination
    ue_vol_mov_no_syn_pron_sup = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Pronation/supinationelbow at 0 shoulder at 30-90 flexion'), choices=FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY)

    # V. Normal reflex activity evaluated
    ue_normal_reflex_activity = models.IntegerField(verbose_name=_('Normal reflex activity'), choices=FUGLM_UE_NORMAL_REFLEX_ACTIVITY)
    ue_normal_reflex_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # B. WRIST
    ue_wrist_stab_elbow_90 = models.IntegerField(_('Stability at 15 dorsiflexion elbow at 90, forearm pronated shoulder at 0'), choices=FUGLM_UE_WRIST_STAB_ELBOW_90_ACTIVITY)
    ue_wrist_flex_elbow_90 = models.IntegerField(_('Repeated dorsifexion / volar flexion elbow at 90, forearm pronated shoulder at 0, slight finger flexion'), choices=FUGLM_UE_WRIST_FLEX_ELBOW_90_ACTIVITY)
    ue_wrist_stab_elbow_0 = models.IntegerField(_('Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction'), choices=FUGLM_UE_WRIST_STAB_ELBOW_0_ACTIVITY)
    ue_wrist_flex_elbow_0 = models.IntegerField(_('Repeated dorsifexion / volar flexion elbow at 0, forearm pronated slight shoulder flexion/abduction'), choices=FUGLM_UE_WRIST_FLEX_ELBOW_0_ACTIVITY)
    ue_wrist_circumduction = models.IntegerField(_('Circumduction'), choices=FUGLM_UE_WRIST_CIRCUMDUCTION_ACTIVITY)

    # C. HAND
    # Mass flexion
    ue_hand_mass_flex = models.IntegerField(choices=FUGLM_UE_HAND_MASS_FLEX_ACTIVITY)
    # Mass extension
    ue_hand_mass_ext = models.IntegerField(choices=FUGLM_UE_HAND_MASS_EXT_ACTIVITY)
    # flexion in PIP and DIP (digits II-V)
    ue_hand_flex_pip_dip = models.IntegerField(choices=FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY)
    # thumb adduction
    ue_hand_thumb_adduction = models.IntegerField(choices=FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY)
    # opposition
    ue_hand_thumb_opposition = models.IntegerField(choices=FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY)
    # cylinder grip
    ue_hand_cylinder_grip = models.IntegerField(choices=FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY)
    # spherical grip
    ue_hand_spherical_grip = models.IntegerField(choices=FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY)

    # D. COORDINATION/SPEED
    ue_coord_speed_tremor = models.IntegerField(choices=FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY)
    ue_coord_speed_dysmetria = models.IntegerField(choices=FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY)
    ue_coord_speed_time = models.IntegerField(choices=FUGLM_UE_COORD_SPEED_TIME_ACTIVITY)

    # E. LOWER EXTREMITY
    # I. Reflex activity, supine position
    le_reflex_activity_achilles = models.IntegerField(choices=FUGLM_LE_REFLEX_ACTIVITY)
    le_reflex_activity_pattelar = models.IntegerField(choices=FUGLM_LE_REFLEX_ACTIVITY)
    # V. Normal reflex activity
    le_reflex_activity_achilles_pattelar = models.IntegerField(choices=FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY)

    # II. Volitional movement within synergies
    # Flexor synergy
    le_vol_mov_syn_hip_flexion = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_knee_flexion = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_ankle_dorsiflexion = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)
    # Extensor synergy
    le_vol_mov_syn_hip_extension = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_hip_adduction = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_knee_extension = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_ankle_flexion = models.IntegerField(choices=FUGLM_LE_VOL_MOV_SYN)

    # III. Volitional movement mixing synergies
    le_vol_mov_mix_syn_knee = models.IntegerField(choices=FUGLM_LE_VOL_MOV_MIX_SYN)
    le_vol_mov_mix_syn_ankle = models.IntegerField(choices=FUGLM_LE_VOL_MOV_MIX_SYN)

    # IV. Volitional movement with little or no synergy
    le_vol_mov_no_syn_knee = models.IntegerField(choices=FUGLM_LE_VOL_MOV_NO_SYN)
    le_vol_mov_no_syn_ankle = models.IntegerField(choices=FUGLM_LE_VOL_MOV_NO_SYN)

    # F. COORDINATION/SPEED
    le_coord_speed_tremor = models.IntegerField(choices=FUGLM_LE_COORD_SPEED)
    le_coord_speed_dysmetria = models.IntegerField(choices=FUGLM_LE_COORD_SPEED)
    le_coord_speed_time = models.IntegerField(choices=FUGLM_LE_COORD_SPEED)

    def ue_reflex_activity_total(self):
        """
        :return: Total of A.Upper extremity / I.Reflex activity
        """
        result = 0
        if self.ue_reflex_activity_flex and self.ue_reflex_activity_flex > 0:
            result += self.ue_reflex_activity_flex
        if self.ue_reflex_activity_ext and self.ue_reflex_activity_ext > 0:
            result += self.ue_reflex_activity_ext
        return result

    def ue_vol_mov_syn_total(self):
        """
        :return: Total of A.Upper extremity / II - Volitional movement within synergies
        """
        result = 0

        # Flexor synergy
        if self.ue_vol_mov_syn_flex_shoulder_retrac and self.ue_vol_mov_syn_flex_shoulder_retrac > 0:
            result += self.ue_vol_mov_syn_flex_shoulder_retrac
        if self.ue_vol_mov_syn_flex_shoulder_elev and self.ue_vol_mov_syn_flex_shoulder_elev > 0:
            result += self.ue_vol_mov_syn_flex_shoulder_elev
        if self.ue_vol_mov_syn_flex_shoulder_abd and self.ue_vol_mov_syn_flex_shoulder_abd > 0:
            result += self.ue_vol_mov_syn_flex_shoulder_abd
        if self.ue_vol_mov_syn_flex_shoulder_rot and self.ue_vol_mov_syn_flex_shoulder_rot > 0:
            result += self.ue_vol_mov_syn_flex_shoulder_rot
        if self.ue_vol_mov_syn_flex_elbow_flex and self.ue_vol_mov_syn_flex_elbow_flex > 0:
            result += self.ue_vol_mov_syn_flex_elbow_flex
        if self.ue_vol_mov_syn_flex_forearm_sup and self.ue_vol_mov_syn_flex_forearm_sup > 0:
            result += self.ue_vol_mov_syn_flex_forearm_sup
        # Extensor synergy
        if self.ue_vol_mov_syn_ext_shoulder and self.ue_vol_mov_syn_ext_shoulder > 0:
            result += self.ue_vol_mov_syn_ext_shoulder
        if self.ue_vol_mov_syn_ext_elbow and self.ue_vol_mov_syn_ext_elbow > 0:
            result += self.ue_vol_mov_syn_ext_elbow
        if self.ue_vol_mov_syn_ext_forearm and self.ue_vol_mov_syn_ext_forearm > 0:
            result += self.ue_vol_mov_syn_ext_forearm

        return result

    def ue_vol_mov_mix_total(self):
        """
        :return: Total of A.Upper extremity / III - Volitional movement mixing synergies, without compensation
        """
        result = 0

        if self.vol_mov_mix_hand_spine and self.vol_mov_mix_hand_spine > 0:
            result += self.vol_mov_mix_hand_spine
        if self.vol_mov_mix_shoulder_flex and self.vol_mov_mix_shoulder_flex > 0:
            result += self.vol_mov_mix_shoulder_flex
        if self.vol_mov_mix_pron_sup and self.vol_mov_mix_pron_sup > 0:
            result += self.vol_mov_mix_pron_sup
        return result

    def ue_vol_mov_no_syn_total(self):
        """
        :return: Total of A.Upper extremity / IV. Volitional movement with little or no synergy
        """
        result = 0

        if self.ue_vol_mov_no_syn_shoulder_abd and self.ue_vol_mov_no_syn_shoulder_abd > 0:
            result += self.ue_vol_mov_no_syn_shoulder_abd
        if self.ue_vol_mov_no_syn_shoulder_flex and self.ue_vol_mov_no_syn_shoulder_flex > 0:
            result += self.vol_mov_mix_shoulder_flex
        if self.ue_vol_mov_no_syn_pron_sup and self.ue_vol_mov_no_syn_pron_sup > 0:
            result += self.ue_vol_mov_no_syn_pron_sup
        return result

    def ue_normal_reflex_total(self):
        """
        :return: Total of A.Upper extremity / V. Normal reflex activity evaluated
        """
        result = 0

        if self.ue_normal_reflex_activity and self.ue_normal_reflex_activity > 0:
            result += self.ue_normal_reflex_activity

        return result

    def upper_extremity_total(self):
        """
        :return: A. UPPER EXTREMITY total
        """
        return self.ue_reflex_activity_total() + self.ue_vol_mov_syn_total() + self.ue_vol_mov_mix_total() + self.ue_vol_mov_no_syn_total() + self.ue_normal_reflex_total()

    def ue_wrist_total(self):
        """
        :return: B. WRIST total
        """
        result = 0

        if self.ue_wrist_stab_elbow_90 and self.ue_wrist_stab_elbow_90 > 0:
            result += self.ue_wrist_stab_elbow_90
        if self.ue_wrist_flex_elbow_90 and self.ue_wrist_flex_elbow_90 > 0:
            result += self.ue_wrist_flex_elbow_90
        if self.ue_wrist_stab_elbow_0 and self.ue_wrist_stab_elbow_0 > 0:
            result += self.ue_wrist_stab_elbow_0
        if self.ue_wrist_flex_elbow_0 and self.ue_wrist_flex_elbow_0 > 0:
            result += self.ue_wrist_flex_elbow_0
        if self.ue_wrist_circumduction and self.ue_wrist_circumduction > 0:
            result += self.ue_wrist_stab_elbow_90

        return result

    def ue_hand_total(self):
        """
        :return: C. HAND total
        """
        result = 0

        if self.ue_hand_mass_flex and self.ue_hand_mass_flex > 0:
            result += self.ue_hand_mass_flex
        if self.ue_hand_mass_ext and self.ue_hand_mass_ext > 0:
            result += self.ue_hand_mass_ext
        if self.ue_hand_flex_pip_dip and self.ue_hand_flex_pip_dip > 0:
            result += self.ue_hand_flex_pip_dip
        if self.ue_hand_thumb_adduction and self.ue_hand_thumb_adduction > 0:
            result += self.ue_hand_thumb_adduction
        if self.ue_hand_thumb_opposition and self.ue_hand_thumb_opposition > 0:
            result += self.ue_hand_thumb_opposition
        if self.ue_hand_cylinder_grip and self.ue_hand_cylinder_grip > 0:
            result += self.ue_hand_cylinder_grip
        if self.ue_hand_spherical_grip and self.ue_hand_spherical_grip > 0:
            result += self.ue_hand_spherical_grip

        return result

    def ue_coordination_speed_total(self):
        """
        :return: D. COORDINATION/SPEED
        """
        result = 0

        if self.ue_coord_speed_tremor and self.ue_coord_speed_tremor > 0:
            result += self.ue_coord_speed_tremor
        if self.ue_coord_speed_dysmetria and self.ue_coord_speed_dysmetria > 0:
            result += self.ue_coord_speed_dysmetria
        if self.ue_coord_speed_time and self.ue_coord_speed_time > 0:
            result += self.ue_coord_speed_time

        return result

    # E. LOWER EXTREMITY
    def le_reflex_activity_total(self):
        """
        :return: E. LOWER EXTREMITY / I. Reflex activity
        """
        result = 0

        if self.le_reflex_activity_achilles and self.le_reflex_activity_achilles > 0:
            result += self.le_reflex_activity_achilles
        if self.le_reflex_activity_pattelar and self.le_reflex_activity_pattelar > 0:
            result += self.le_reflex_activity_pattelar
        if self.le_reflex_activity_achilles_pattelar and self.le_reflex_activity_achilles_pattelar > 0:
            result += self.le_reflex_activity_achilles_pattelar

        return result

    def le_vol_mov_syn_flex_total(self):
        """
        :return: E. LOWER EXTREMITY / II. Volitional movement within synergies / Flexor synergy
        """
        result = 0

        if self.le_vol_mov_syn_hip_flexion and self.le_vol_mov_syn_hip_flexion > 0:
            result += self.le_vol_mov_syn_hip_flexion
        if self.le_vol_mov_syn_knee_flexion and self.le_vol_mov_syn_knee_flexion > 0:
            result += self.le_vol_mov_syn_knee_flexion
        if self.le_vol_mov_syn_ankle_dorsiflexion and self.le_vol_mov_syn_ankle_dorsiflexion > 0:
            result += self.le_vol_mov_syn_ankle_dorsiflexion

        return result

    def le_vol_mov_syn_ext_total(self):
        """
        :return: E. LOWER EXTREMITY / II. Volitional movement within synergies / Extensor synergy
        """
        result = 0

        if self.le_vol_mov_syn_hip_extension and self.le_vol_mov_syn_hip_extension > 0:
            result += self.le_vol_mov_syn_hip_extension
        if self.le_vol_mov_syn_hip_adduction and self.le_vol_mov_syn_hip_adduction > 0:
            result += self.le_vol_mov_syn_hip_adduction
        if self.le_vol_mov_syn_knee_extension and self.le_vol_mov_syn_knee_extension > 0:
            result += self.le_vol_mov_syn_knee_extension
        if self.le_vol_mov_syn_ankle_flexion and self.le_vol_mov_syn_ankle_flexion > 0:
            result += self.le_vol_mov_syn_ankle_flexion

        return result

    def le_vol_mov_mix_syn_total(self):
        """
        :return: E. LOWER EXTREMITY / III. Volitional movement mixing synergies +
                 E. LOWER EXTREMITY / IV. Volitional movement with little or no synergy
        """
        result = 0

        if self.le_vol_mov_mix_syn_knee and self.le_vol_mov_mix_syn_knee > 0:
            result += self.le_vol_mov_mix_syn_knee
        if self.le_vol_mov_mix_syn_ankle and self.le_vol_mov_mix_syn_ankle > 0:
            result += self.le_vol_mov_mix_syn_ankle
        if self.le_vol_mov_no_syn_knee and self.le_vol_mov_no_syn_knee > 0:
            result += self.le_vol_mov_no_syn_knee
        if self.le_vol_mov_no_syn_ankle and self.le_vol_mov_no_syn_ankle > 0:
            result += self.le_vol_mov_no_syn_ankle

        return result

    def le_coord_speed_total(self):
        """
        :return: E. LOWER EXTREMITY / F. COORDINATION/SPEED
        """
        result = 0

        if self.le_coord_speed_tremor and self.le_coord_speed_tremor > 0:
            result += self.le_coord_speed_tremor
        if self.le_coord_speed_dysmetria and self.le_coord_speed_dysmetria > 0:
            result += self.le_coord_speed_dysmetria
        if self.le_coord_speed_time and self.le_coord_speed_time > 0:
            result += self.le_coord_speed_time

        return result


