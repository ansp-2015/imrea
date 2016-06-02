# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect
from ..models.clin import Clin, CLIN_NEGLECT_CHOICES

class ClinForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClinForm, self).__init__(*args, **kwargs)
        self.fields['neglect_1a'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_1b'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_1c'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_1d'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_2a'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_2b'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_2c'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_2d'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_3a'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_3b'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_3c'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_3d'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_4a'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_4b'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_4c'].choices = CLIN_NEGLECT_CHOICES
        self.fields['neglect_4d'].choices = CLIN_NEGLECT_CHOICES

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }

    class Meta:
        model = Clin
        fields = ['neglect_1a', 'neglect_1b', 'neglect_1c', 'neglect_1d',
               'neglect_2a', 'neglect_2b', 'neglect_2c', 'neglect_2d',
               'neglect_3a', 'neglect_3b', 'neglect_3c', 'neglect_3d',
               'neglect_4a', 'neglect_4b', 'neglect_4c', 'neglect_4d', 'obs']
        widgets = {
            'neglect_1a': ButtonRadioHorizontalLabelSelect(),
            'neglect_1b': ButtonRadioHorizontalLabelSelect(),
            'neglect_1c': ButtonRadioHorizontalLabelSelect(),
            'neglect_1d': ButtonRadioHorizontalLabelSelect(),
            'neglect_2a': ButtonRadioHorizontalLabelSelect(),
            'neglect_2b': ButtonRadioHorizontalLabelSelect(),
            'neglect_2c': ButtonRadioHorizontalLabelSelect(),
            'neglect_2d': ButtonRadioHorizontalLabelSelect(),
            'neglect_3a': ButtonRadioHorizontalLabelSelect(),
            'neglect_3b': ButtonRadioHorizontalLabelSelect(),
            'neglect_3c': ButtonRadioHorizontalLabelSelect(),
            'neglect_3d': ButtonRadioHorizontalLabelSelect(),
            'neglect_4a': ButtonRadioHorizontalLabelSelect(),
            'neglect_4b': ButtonRadioHorizontalLabelSelect(),
            'neglect_4c': ButtonRadioHorizontalLabelSelect(),
            'neglect_4d': ButtonRadioHorizontalLabelSelect(),
        }
