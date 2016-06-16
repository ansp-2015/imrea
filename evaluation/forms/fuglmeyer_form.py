# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models.fuglmeyer import FuglMeyer


class FuglMeyerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FuglMeyerForm, self).__init__(*args, **kwargs)
        self.fields['ue_reflex_activity_flex'].choices = FuglMeyer.FUGLM_UE_REFLEX_ACTIVITY
        self.fields['ue_reflex_activity_ext'].choices = FuglMeyer.FUGLM_UE_REFLEX_ACTIVITY

        self.fields['ue_vol_mov_syn_flex_shoulder_retrac'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_flex_shoulder_elev'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_flex_shoulder_abd'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_flex_shoulder_rot'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_flex_elbow_flex'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_flex_forearm_sup'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY

        self.fields['ue_vol_mov_syn_ext_shoulder'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_ext_elbow'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY
        self.fields['ue_vol_mov_syn_ext_forearm'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY

        self.fields['vol_mov_mix_hand_spine'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY
        self.fields['vol_mov_mix_shoulder_flex'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY

        self.fields['vol_mov_mix_pron_sup'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY

        self.fields['ue_vol_mov_no_syn_shoulder_abd'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY
        self.fields['ue_vol_mov_no_syn_shoulder_flex'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY
        self.fields['ue_vol_mov_no_syn_pron_sup'].choices = FuglMeyer.FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY

        self.fields['ue_normal_reflex_activity'].choices = FuglMeyer.FUGLM_UE_NORMAL_REFLEX_ACTIVITY

        self.fields['ue_wrist_stab_elbow_90'].choices = FuglMeyer.FUGLM_UE_WRIST_STAB_ELBOW_90_ACTIVITY
        self.fields['ue_wrist_flex_elbow_90'].choices = FuglMeyer.FUGLM_UE_WRIST_FLEX_ELBOW_90_ACTIVITY
        self.fields['ue_wrist_stab_elbow_0'].choices = FuglMeyer.FUGLM_UE_WRIST_STAB_ELBOW_0_ACTIVITY
        self.fields['ue_wrist_flex_elbow_0'].choices = FuglMeyer.FUGLM_UE_WRIST_FLEX_ELBOW_0_ACTIVITY

        self.fields['ue_wrist_circumduction'].choices = FuglMeyer.FUGLM_UE_WRIST_CIRCUMDUCTION_ACTIVITY

        self.fields['ue_hand_mass_flex'].choices = FuglMeyer.FUGLM_UE_HAND_MASS_FLEX_ACTIVITY
        self.fields['ue_hand_mass_ext'].choices = FuglMeyer.FUGLM_UE_HAND_MASS_EXT_ACTIVITY
        self.fields['ue_hand_flex_pip_dip'].choices = FuglMeyer.FUGLM_UE_HAND_FLEX_PIP_DIP_ACTIVITY
        self.fields['ue_hand_thumb_adduction'].choices = FuglMeyer.FUGLM_UE_HAND_THUMB_ADDUCTION_ACTIVITY
        self.fields['ue_hand_thumb_opposition'].choices = FuglMeyer.FUGLM_UE_HAND_THUMB_OPPOSITION_ACTIVITY
        self.fields['ue_hand_cylinder_grip'].choices = FuglMeyer.FUGLM_UE_HAND_CYLINDER_GRIP_ACTIVITY
        self.fields['ue_hand_spherical_grip'].choices = FuglMeyer.FUGLM_UE_HAND_SPHERICAL_GRIP_ACTIVITY

        self.fields['ue_coord_speed_tremor'].choices = FuglMeyer.FUGLM_UE_COORD_SPEED_TREMOR_ACTIVITY
        self.fields['ue_coord_speed_dysmetria'].choices = FuglMeyer.FUGLM_UE_COORD_SPEED_DYSMETRIA_ACTIVITY
        self.fields['ue_coord_speed_time'].choices = FuglMeyer.FUGLM_UE_COORD_SPEED_TIME_ACTIVITY

        self.fields['le_reflex_activity_achilles'].choices = FuglMeyer.FUGLM_LE_REFLEX_ACTIVITY
        self.fields['le_reflex_activity_pattelar'].choices = FuglMeyer.FUGLM_LE_REFLEX_ACTIVITY
        self.fields['le_reflex_activity_achilles_pattelar'].choices = FuglMeyer.FUGLM_LE_REFLEX_ACTIVITY_ACHILLES_PATTELAR_ACTIVITY

        self.fields['le_vol_mov_syn_hip_flexion'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN
        self.fields['le_vol_mov_syn_knee_flexion'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN
        self.fields['le_vol_mov_syn_ankle_dorsiflexion'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN
        self.fields['le_vol_mov_syn_hip_extension'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN
        self.fields['le_vol_mov_syn_hip_adduction'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN
        self.fields['le_vol_mov_syn_knee_extension'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN
        self.fields['le_vol_mov_syn_ankle_flexion'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_SYN

        self.fields['le_vol_mov_mix_syn_knee'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_MIX_SYN_KNEE
        self.fields['le_vol_mov_mix_syn_ankle'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_MIX_SYN_ANKLE

        self.fields['le_vol_mov_no_syn_knee'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_NO_SYN_KNEE
        self.fields['le_vol_mov_no_syn_ankle'].choices = FuglMeyer.FUGLM_LE_VOL_MOV_NO_SYN_ANKLE

        self.fields['le_coord_speed_tremor'].choices = FuglMeyer.FUGLM_LE_COORD_SPEED_TREMOR
        self.fields['le_coord_speed_dysmetria'].choices = FuglMeyer.FUGLM_LE_COORD_SPEED_DYSMETRIA
        self.fields['le_coord_speed_time'].choices = FuglMeyer.FUGLM_LE_COORD_SPEED_TIME

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }

    class Meta:
        model = FuglMeyer
        fields = ['patient', 'period', 'ue_reflex_activity_flex', 'ue_reflex_activity_ext',]
        # fields = ['neglect_1a', 'neglect_1b', 'neglect_1c', 'neglect_1d',
        #        'neglect_2a', 'neglect_2b', 'neglect_2c', 'neglect_2d',
        #        'neglect_3a', 'neglect_3b', 'neglect_3c', 'neglect_3d',
        #        'neglect_4a', 'neglect_4b', 'neglect_4c', 'neglect_4d', 'obs']
        widgets = {
            'ue_reflex_activity_flex': ButtonRadioHorizontalValueSelect(),
            'ue_reflex_activity_ext': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_flex_shoulder_retrac': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_flex_shoulder_elev': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_flex_shoulder_abd': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_flex_shoulder_rot': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_flex_elbow_flex': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_flex_forearm_sup': ButtonRadioHorizontalValueSelect(),

            'ue_vol_mov_syn_ext_shoulder': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_ext_elbow': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_syn_ext_forearm': ButtonRadioHorizontalValueSelect(),

            'vol_mov_mix_hand_spine': ButtonRadioHorizontalValueSelect(),
            'vol_mov_mix_shoulder_flex': ButtonRadioHorizontalValueSelect(),
            'vol_mov_mix_pron_sup': ButtonRadioHorizontalValueSelect(),

            'ue_vol_mov_no_syn_shoulder_abd': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_no_syn_shoulder_flex': ButtonRadioHorizontalValueSelect(),
            'ue_vol_mov_no_syn_pron_sup': ButtonRadioHorizontalValueSelect(),

            'ue_normal_reflex_activity': ButtonRadioHorizontalValueSelect(),

            'ue_wrist_stab_elbow_90': ButtonRadioHorizontalValueSelect(),
            'ue_wrist_flex_elbow_90': ButtonRadioHorizontalValueSelect(),
            'ue_wrist_stab_elbow_0': ButtonRadioHorizontalValueSelect(),
            'ue_wrist_flex_elbow_0': ButtonRadioHorizontalValueSelect(),
            'ue_wrist_circumduction': ButtonRadioHorizontalValueSelect(),

            'ue_hand_mass_flex': ButtonRadioHorizontalValueSelect(),
            'ue_hand_mass_ext': ButtonRadioHorizontalValueSelect(),
            'ue_hand_flex_pip_dip': ButtonRadioHorizontalValueSelect(),
            'ue_hand_thumb_adduction': ButtonRadioHorizontalValueSelect(),
            'ue_hand_thumb_opposition': ButtonRadioHorizontalValueSelect(),
            'ue_hand_cylinder_grip': ButtonRadioHorizontalValueSelect(),
            'ue_hand_spherical_grip': ButtonRadioHorizontalValueSelect(),

            'ue_coord_speed_tremor': ButtonRadioHorizontalValueSelect(),
            'ue_coord_speed_dysmetria': ButtonRadioHorizontalValueSelect(),
            'ue_coord_speed_time': ButtonRadioHorizontalValueSelect(),

            'le_reflex_activity_achilles': ButtonRadioHorizontalValueSelect(),
            'le_reflex_activity_pattelar': ButtonRadioHorizontalValueSelect(),

            'le_reflex_activity_achilles_pattelar': ButtonRadioHorizontalValueSelect(),

            'le_vol_mov_syn_hip_flexion': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_syn_knee_flexion': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_syn_ankle_dorsiflexion': ButtonRadioHorizontalValueSelect(),

            'le_vol_mov_syn_hip_extension': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_syn_hip_adduction': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_syn_knee_extension': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_syn_ankle_flexion': ButtonRadioHorizontalValueSelect(),

            'le_vol_mov_mix_syn_knee': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_mix_syn_ankle': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_no_syn_knee': ButtonRadioHorizontalValueSelect(),
            'le_vol_mov_no_syn_ankle': ButtonRadioHorizontalValueSelect(),

            'le_coord_speed_tremor': ButtonRadioHorizontalValueSelect(),
            'le_coord_speed_dysmetria': ButtonRadioHorizontalValueSelect(),
            'le_coord_speed_time': ButtonRadioHorizontalValueSelect(),


        }
        # widgets = {
        #     'neglect_1a': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_1b': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_1c': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_1d': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_2a': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_2b': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_2c': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_2d': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_3a': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_3b': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_3c': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_3d': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_4a': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_4b': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_4c': ButtonRadioHorizontalLabelSelect(),
        #     'neglect_4d': ButtonRadioHorizontalLabelSelect(),
        # }
