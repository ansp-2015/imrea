# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from ..models.eeg import Eeg, EegFile


class EegForm(forms.ModelForm):

    class Meta:
        model = Eeg
        fields = ['patient', 'eegtitle']

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }


class EegFileInlineForm(forms.ModelForm):
    file = forms.FileField(label=_('File'))

    class Meta:
        model = EegFile
        fields = ('file', )