# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from . import BaseEvaluation


class FuglMeyer(BaseEvaluation):
    # I - Reflex activity
    FUGLM_UE_REFLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_REFLEX_ACTIVITY", u'No reflex activity can be elicited')),
        (2, pgettext("FUGLM_UE_REFLEX_ACTIVITY", u'Reflex activity can be elicited')),
    )
    # II - Volitional movement within synergies
    FUGLM_UE_VOL_MOV_SYN_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_SYN_ACTIVITY", u'Cannot be performed at all')),
        (1, pgettext("FUGLM_UE_VOL_MOV_SYN_ACTIVITY", u'Performed partly')),
        (2, pgettext("FUGLM_UE_VOL_MOV_SYN_ACTIVITY", u'Performed faultlessly')),
    )
    # III - Volitional movement mixing synergies, without compensation
    FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY", u'No specific action is performed (or patient moves but does not reach ASIS)')),
        (1, pgettext("FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY", u' Hand must pass anterior superior iliac spine (performed partly)')),
        (2, pgettext("FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY", u' Performed faultlessly (patient clears ASIS and can extend arm behind back towards sacrum')),
    )
    FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY", u'Immediate abduction or elbow flexion')),
        (1, pgettext("FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY", u'Abduction or elbow flexion during movement')),
        (2, pgettext("FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY", u'Complete flexion 90°, maintains 0° in elbow')),
    )
    FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY", u'No pronation/supination, starting position impossible')),
        (1, pgettext("FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY", u'Limited pronation/supination, maintains position')),
        (2, pgettext("FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY", u'Full pronation/supination, maintains elbow extension')),
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
        (0, pgettext("FUGLM_UE_HAND_MASS_FLEX_ACTIVITY", u'No flexion occurs')),
        (1, pgettext("FUGLM_UE_HAND_MASS_FLEX_ACTIVITY", u'Some flexion, but not full motion')),
        (2, pgettext("FUGLM_UE_HAND_MASS_FLEX_ACTIVITY", u'Completed active flexion ')),
    )
    FUGLM_UE_HAND_MASS_EXT_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_MASS_EXT_ACTIVITY", u'No extension occurs')),
        (1, pgettext("FUGLM_UE_HAND_MASS_EXT_ACTIVITY", u'Patient can release an active mass flexion grasp')),
        (2, pgettext("FUGLM_UE_HAND_MASS_EXT_ACTIVITY", u'Full active extension')),
    )
    FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY", u'Required position cannot be attained')),
        (1, pgettext("FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY", u'Grasp is weak')),
        (2, pgettext("FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY", u'Grasp can be maintained against relatively great resistance')),
    )
    FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY", u'Function cannot be performed')),
        (1, pgettext("FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY", u'Scrap of paper interposed between the thumb and index finger can be kept in place, but not against a slight tug')),
        (2, pgettext("FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY", u'Paper is held firmly against a tug')),
    )
    FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY", u'Function cannot be performed')),
        (1, pgettext("FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY", u'A pencil interposed between the thumb pad and the pad of the index finger can be kept in place, but not against a slight tug')),
        (2, pgettext("FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY", u'Pencil is held firmly against a tug')),
    )
    FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY", u'Function cannot be performed')),
        (1, pgettext("FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY", u'A can interposed between the thumb and index finger can be kept in place, but not against a slight tug')),
        (2, pgettext("FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY", u'Can is held firmly against a tug')),
    )
    FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY = (
        (0, pgettext("FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY", u'Function cannot be performed')),
        (1, pgettext("FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY", u'A tennis ball can be kept in place with a spherical grasp, but not against a slight tug')),
        (2, pgettext("FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY", u'Tennis ball is held firmly against a tug')),
    )

    # D. COORDINATION/SPEED
    FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY = (
        (0, pgettext("FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY", u'Marked tremor')),
        (1, pgettext("FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY", u'Slight tremor')),
        (2, pgettext("FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY", u'No tremor')),
    )
    FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY = (
        (0, pgettext("FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY", u'Pronounced or unsystematic dysmetria')),
        (1, pgettext("FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY", u'Slight or systematic dysmetria')),
        (2, pgettext("FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY", u'No dysmetria')),
    )
    FUGLM_UE_COORD_SPEED_TIME_ACTIVITY = (
        (0, pgettext("FUGLM_UE_COORD_SPEED_TIME_ACTIVITY", u'Activity is more than 5 seconds longer than unaffected hand')),
        (1, pgettext("FUGLM_UE_COORD_SPEED_TIME_ACTIVITY", u'(2-5) seconds longer than unaffected side')),
        (2, pgettext("FUGLM_UE_COORD_SPEED_TIME_ACTIVITY", u'Less than 2 seconds difference')),
    )
    # E. LOWER EXTREMITY
    # I. Reflex activity, supine position
    FUGLM_LE_REFLEX_ACTIVITY = (
        (0, pgettext("FUGLM_LE_REFLEX_ACTIVITY", u'No reflex activity can be elicited')),
        (2, pgettext("FUGLM_LE_REFLEX_ACTIVITY", u'Reflex activity can be elicited')),
    )
    FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY = (
        (0, pgettext("FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY", u'At least 2 of the 3 phasic reflexes are markedly hyperactive')),
        (1, pgettext("FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY", u'One reflex is markedly hyperactive or at least 2 reflexes are lively')),
        (2, pgettext("FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY", u'No more than one reflex is lively and none are hyperactive')),
    )

    # II. Volitional movement within synergies
    FUGLM_LE_VOL_MOV_SYN = (
        (0, pgettext("FUGLM_LE_VOL_MOV_SYN", u'Cannot be performed at all')),
        (1, pgettext("FUGLM_LE_VOL_MOV_SYN", u'Partial motion')),
        (2, pgettext("FUGLM_LE_VOL_MOV_SYN", u'Full motion')),
    )
    # III. Volitional movement mixing synergies
    FUGLM_LE_VOL_MOV_MIX_SYN_KNEE = (
        (0, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN_KNEE", u'No active motion')),
        (1, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN_KNEE", u'From slightly extended position, knee can be flexed but not beyond 90°')),
        (2, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN_KNEE", u'Knee flexion beyond 90°')),
    )
    FUGLM_LE_VOL_MOV_MIX_SYN_ANKLE = (
        (0, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN_ANKLE", u'No active motion')),
        (1, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN_ANKLE", u'Incomplete active flexion')),
        (2, pgettext("FUGLM_LE_VOL_MOV_MIX_SYN_ANKLE", u'Normal dorsiflexion')),
    )
    FUGLM_LE_VOL_MOV_NO_SYN_KNEE = (
        (0, pgettext("FUGLM_LE_VOL_MOV_NO_SYN_KNEE", u'Knee cannot flex without hip flexion')),
        (1, pgettext("FUGLM_LE_VOL_MOV_NO_SYN_KNEE", u'Knee flexion begins without hip flexion but does not reach to 90° or hip begins to flex in later phase of motion')),
        (2, pgettext("FUGLM_LE_VOL_MOV_NO_SYN_KNEE", u'Knee flexion beyond 90 degrees with hip maintained in extension')),
    )
    FUGLM_LE_VOL_MOV_NO_SYN_ANKLE = (
        (0, pgettext("FUGLM_LE_VOL_MOV_NO_SYN_ANKLE", u'No active motion')),
        (1, pgettext("FUGLM_LE_VOL_MOV_NO_SYN_ANKLE", u'Partial motion')),
        (2, pgettext("FUGLM_LE_VOL_MOV_NO_SYN_ANKLE", u'Full motion')),
    )
    # F. COORDINATION/SPEED
    FUGLM_LE_COORD_SPEED_TREMOR = (
        (0, pgettext("FUGLM_LE_COORD_SPEED_TREMOR", u'Marked tremor')),
        (1, pgettext("FUGLM_LE_COORD_SPEED_TREMOR", u'Slight tremor')),
        (2, pgettext("FUGLM_LE_COORD_SPEED_TREMOR", u'No tremor')),
    )
    FUGLM_LE_COORD_SPEED_DYSMETRIA = (
        (0, pgettext("FUGLM_LE_COORD_SPEED_DYSMETRIA", u'Pronounced or unsystematic dysmetria')),
        (1, pgettext("FUGLM_LE_COORD_SPEED_DYSMETRIA", u'Slight or systematic dysmetria')),
        (2, pgettext("FUGLM_LE_COORD_SPEED_DYSMETRIA", u'No dysmetria')),
    )
    FUGLM_LE_COORD_SPEED_TIME = (
        (0, pgettext("FUGLM_LE_COORD_SPEED_TIME", u'Activity is more than 6 seconds longer than unaffected leg')),
        (1, pgettext("FUGLM_LE_COORD_SPEED_TIME", u' 2-5.9 seconds longer than unaffected leg')),
        (2, pgettext("FUGLM_LE_COORD_SPEED_TIME", u'less than 2 seconds difference')),
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
    ue_vol_mov_mix_hand_spine = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Hand to lumbar spine'), choices=FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY)
    # Shoulder flexion 0-90
    ue_vol_mov_mix_shoulder_flex = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Shoulder flexion 0-90 elbow at 0 pronation-supination 0'), choices=FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY)
    # Pronation-supination
    ue_vol_mov_mix_pron_sup = models.IntegerField(verbose_name=pgettext('FuglMeyer', 'Pronation-supination elbow at 90 shoulder at 0'), choices=FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY)

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
    ue_hand_mass_flex = models.IntegerField(_(u'Mass flexion from full active or passive extension'), choices=FUGLM_UE_HAND_MASS_FLEX_ACTIVITY, help_text=_(u'Close your hand. The therapist can help get the starting position with your fingers in extension'))
    # Mass extension
    ue_hand_mass_ext = models.IntegerField(_(u'Mass flexion from full active or passive flexion'), choices=FUGLM_UE_HAND_MASS_EXT_ACTIVITY, help_text=_(u'Open your hand. The therapist can help get the starting position with your fingers in flexion'))
    # flexion in PIP and DIP (digits II-V)
    ue_hand_flex_pip_dip = models.IntegerField(_(u'Flexion in PIP and DIP (digits II-V)extension in MCP II-V'),choices=FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY, help_text=_(u'Hold my finger and keep it stuck between your fingers'))

    # thumb adduction
    ue_hand_thumb_adduction = models.IntegerField(_(u'Thumb adduction'),
                                                  choices=FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY,
                                                  help_text=_(u'Ask the patient to perform pure thumb adduction with the scrap of paper interposed between the thumb and first digit. Test this grip against resistance by asking the patient to hold as you attempt to pull the paper out with a slight tug. <strong>Hold the paper between the thumb and forefinger</strong>'))
    # opposition
    ue_hand_thumb_opposition = models.IntegerField(_(u'Opposition pulpa of the thumb against the pulpa of 2-nd finger,pencil, tug upward'), choices=FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY,
                                                   help_text=_(u'Subject is sitting with arm on bedside table. Instruct the patient to grasp a pen by opposing the thumb and index finger pads around the pen. The pen may not be stabilized by the therapist or the patient’s other hand. Test this grip against resistance by asking the patient to hold as you attempt to pull the pencil out with a slight tug. <strong>Hold the pen and keep it steady</strong>'))
    # cylinder grip
    ue_hand_cylinder_grip = models.IntegerField(_(u'Cylinder shaped object (small can)tug upward, opposition in digits I and II'),
                                                choices=FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY,
                                                help_text=_(u'Subject is sitting with arm on bedside table. Instruct the patient to grasp a small can (placed upright on a table without stabilization) by opening the fingers and opposing the volar surfaces of the thumb and digits. The arm may be supported but the tester may not assist with hand function. Test this grip against resistance by asking the patient to hold as you attempt to pull the can out with a slight tug.<strong>Hold the object and keep it steady</strong>'))
    # spherical grip
    ue_hand_spherical_grip = models.IntegerField(_(u'Fingers in abduction/flexion, thumb opposed, tennis ball'),
                                                 choices=FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY,
                                                 help_text=_(u'Subject is sitting with arm on bedside table. Instruct the patient to perform a spherical grasp by grasping a tennis ball The tester may support the patient’s arm but may not assist with the hand function required for the retrieval task. Test this grip against resistance by asking the patient to hold as you attempt to pull the ball out with a slight tug. <strong>Hold the ball and keep it steady</strong>'))

    # D. COORDINATION/SPEED
    ue_coord_speed_tremor = models.IntegerField(_(u'Tremor'), choices=FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY)
    ue_coord_speed_dysmetria = models.IntegerField(_(u'Dysmetria'), choices=FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY)
    ue_coord_speed_time = models.IntegerField(_(u'Speed'), choices=FUGLM_UE_COORD_SPEED_TIME_ACTIVITY)

    # E. LOWER EXTREMITY
    # I. Reflex activity, supine position
    le_reflex_activity_achilles = models.IntegerField(_(u'Achilles'), choices=FUGLM_LE_REFLEX_ACTIVITY)
    le_reflex_activity_pattelar = models.IntegerField(_(u'Patellar'), choices=FUGLM_LE_REFLEX_ACTIVITY)
    le_reflex_activity_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)
    # V. Normal reflex activity
    le_reflex_activity_achilles_pattelar = models.IntegerField(_(u'Achilles and patellar reflexes'), choices=FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY)
    le_reflex_activity_achilles_pattelar_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # II. Volitional movement within synergies
    # Flexor synergy
    le_vol_mov_syn_hip_flexion = models.IntegerField(_(u'Hip flexion'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_knee_flexion = models.IntegerField(_(u'Knee flexion'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_ankle_dorsiflexion = models.IntegerField(_(u'Ankle dorsiflexion'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_flexion_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)
    # Extensor synergy
    le_vol_mov_syn_hip_extension = models.IntegerField(_(u'Hip extension'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_hip_adduction = models.IntegerField(_(u'Hip adduction'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_knee_extension = models.IntegerField(_(u'Knee extension'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_ankle_flexion = models.IntegerField(_(u'Ankle plantarflexion'), choices=FUGLM_LE_VOL_MOV_SYN)
    le_vol_mov_syn_extension_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # III. Movement combining synergies
    le_vol_mov_mix_syn_knee = models.IntegerField(_(u'Knee Flexion sitting'), choices=FUGLM_LE_VOL_MOV_MIX_SYN_KNEE)
    le_vol_mov_mix_syn_knee_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)
    le_vol_mov_mix_syn_ankle = models.IntegerField(_(u'Ankle Dorsiflexion sitting'), choices=FUGLM_LE_VOL_MOV_MIX_SYN_ANKLE)
    le_vol_mov_mix_syn_ankle_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # IV. Volitional movement with little or no synergy
    le_vol_mov_no_syn_knee = models.IntegerField(_(u'Knee Flexion standing'), choices=FUGLM_LE_VOL_MOV_NO_SYN_KNEE)
    le_vol_mov_no_syn_knee_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)
    le_vol_mov_no_syn_ankle = models.IntegerField(_(u'Ankle Dorsiflexion standing'), choices=FUGLM_LE_VOL_MOV_NO_SYN_ANKLE)
    le_vol_mov_no_syn_ankle_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

    # F. COORDINATION/SPEED
    le_coord_speed_tremor = models.IntegerField(_(u'Scoring Tremor'), choices=FUGLM_LE_COORD_SPEED_TREMOR)
    le_coord_speed_dysmetria = models.IntegerField(_(u'Scoring Dysmetria'), choices=FUGLM_LE_COORD_SPEED_DYSMETRIA)
    le_coord_speed_time = models.IntegerField(_(u'Scoring Speed'), choices=FUGLM_LE_COORD_SPEED_TIME)
    le_coord_speed_obs = models.TextField(verbose_name=pgettext('FuglMeyer', 'Notes'), max_length=500, blank=True, null=True)

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

        if self.ue_vol_mov_mix_hand_spine and self.ue_vol_mov_mix_hand_spine > 0:
            result += self.ue_vol_mov_mix_hand_spine
        if self.ue_vol_mov_mix_shoulder_flex and self.ue_vol_mov_mix_shoulder_flex > 0:
            result += self.ue_vol_mov_mix_shoulder_flex
        if self.ue_vol_mov_mix_pron_sup and self.ue_vol_mov_mix_pron_sup > 0:
            result += self.ue_vol_mov_mix_pron_sup
        return result

    def ue_vol_mov_no_syn_total(self):
        """
        :return: Total of A.Upper extremity / IV. Volitional movement with little or no synergy
        """
        result = 0

        if self.ue_vol_mov_no_syn_shoulder_abd and self.ue_vol_mov_no_syn_shoulder_abd > 0:
            result += self.ue_vol_mov_no_syn_shoulder_abd
        if self.ue_vol_mov_no_syn_shoulder_flex and self.ue_vol_mov_no_syn_shoulder_flex > 0:
            result += self.ue_vol_mov_mix_shoulder_flex
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


