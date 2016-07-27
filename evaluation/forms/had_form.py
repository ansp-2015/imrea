# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models.had import HAD


class HADForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HADForm, self).__init__(*args, **kwargs)
        self.fields['tension'].choices = HAD.HAD_TENSION
        self.fields['enjoy'].choices = HAD.HAD_ENJOY
        self.fields['frightened'].choices = HAD.HAD_FRIGHTENED
        self.fields['laugh'].choices = HAD.HAD_LAUGH
        self.fields['worry'].choices = HAD.HAD_WORRY
        self.fields['cheerful'].choices = HAD.HAD_CHEERFUL
        self.fields['ease'].choices = HAD.HAD_EASE
        self.fields['slowed'].choices = HAD.HAD_SLOWED
        self.fields['butterflies'].choices = HAD.HAD_BUTTERFLIES
        self.fields['appearance'].choices = HAD.HAD_APPEARANCE
        self.fields['restless'].choices = HAD.HAD_RESTLESS
        self.fields['forward'].choices = HAD.HAD_FORWARD
        self.fields['panic'].choices = HAD.HAD_PANIC
        self.fields['book'].choices = HAD.HAD_BOOK

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = HAD
        fields = ['tension', 'enjoy', 'frightened', 'laugh', 'worry', 'cheerful', 'ease', 'slowed', 'butterflies',
                  'appearance', 'restless', 'forward', 'panic', 'book']
        widgets = {
            'tension': ButtonRadioHorizontalValueSelect(),
            'enjoy': ButtonRadioHorizontalValueSelect(),
            'frightened': ButtonRadioHorizontalValueSelect(),
            'laugh': ButtonRadioHorizontalValueSelect(),
            'worry': ButtonRadioHorizontalValueSelect(),
            'cheerful': ButtonRadioHorizontalValueSelect(),
            'ease': ButtonRadioHorizontalValueSelect(),
            'slowed': ButtonRadioHorizontalValueSelect(),
            'butterflies': ButtonRadioHorizontalValueSelect(),
            'appearance': ButtonRadioHorizontalValueSelect(),
            'restless': ButtonRadioHorizontalValueSelect(),
            'forward': ButtonRadioHorizontalValueSelect(),
            'panic': ButtonRadioHorizontalValueSelect(),
            'book': ButtonRadioHorizontalValueSelect(),
        }
