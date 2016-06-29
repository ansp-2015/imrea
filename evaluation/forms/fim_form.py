# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models import FIM


class FIMForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FIMForm, self).__init__(*args, **kwargs)
        self.fields['self_care_eating'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['self_care_grooming'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['self_care_bathing'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['self_care_dressing_upper_body'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['self_care_dressing_lower_body'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['self_care_toileting'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['sphincter_bladder_mgt'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['sphincter_bowel_mgt'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['transfer_wheelchair'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['transfer_toilet'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['transfer_shower'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['locomotion_wheelchair'].choices = FIM.FIM_CHOICES_CATEGORY
        self.fields['locomotion_stairs'].choices = FIM.FIM_CHOICES_CATEGORY

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = FIM
        fields = ['self_care_eating', 'self_care_grooming', 'self_care_bathing', \
                       'self_care_dressing_upper_body', 'self_care_dressing_lower_body', \
                       'self_care_toileting', 'sphincter_bladder_mgt', 'sphincter_bowel_mgt', \
                       'transfer_wheelchair', 'transfer_toilet', 'transfer_shower', \
                       'locomotion_wheelchair', 'locomotion_stairs', 'obs']
        widgets = {
            'self_care_eating': ButtonRadioHorizontalValueSelect(),
            'self_care_grooming': ButtonRadioHorizontalValueSelect(),
            'self_care_bathing': ButtonRadioHorizontalValueSelect(),
            'self_care_dressing_upper_body': ButtonRadioHorizontalValueSelect(),
            'self_care_dressing_lower_body': ButtonRadioHorizontalValueSelect(),
            'self_care_toileting': ButtonRadioHorizontalValueSelect(),
            'sphincter_bladder_mgt': ButtonRadioHorizontalValueSelect(),
            'sphincter_bowel_mgt': ButtonRadioHorizontalValueSelect(),
            'transfer_wheelchair': ButtonRadioHorizontalValueSelect(),
            'transfer_toilet': ButtonRadioHorizontalValueSelect(),
            'transfer_shower': ButtonRadioHorizontalValueSelect(),
            'locomotion_wheelchair': ButtonRadioHorizontalValueSelect(),
            'locomotion_stairs': ButtonRadioHorizontalValueSelect(),
        }
