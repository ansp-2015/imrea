# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models.fuglmeyer import FuglMeyer


class FuglMeyerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FuglMeyerForm, self).__init__(*args, **kwargs)
        self.fields['ue_reflex_activity_flex'].choices = FuglMeyer.FUGLM_UE_REFLEX_ACTIVITY
        self.fields['ue_reflex_activity_ext'].choices = FuglMeyer.FUGLM_UE_REFLEX_ACTIVITY
        # self.fields['neglect_1c'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_1d'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_2a'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_2b'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_2c'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_2d'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_3a'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_3b'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_3c'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_3d'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_4a'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_4b'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_4c'].choices = CLIN_NEGLECT_CHOICES
        # self.fields['neglect_4d'].choices = CLIN_NEGLECT_CHOICES

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
