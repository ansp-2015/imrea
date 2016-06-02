# -*- coding: utf-8 -*-
from django import forms
from ..models import Eeg


class EegForm(forms.ModelForm):

    class Meta:
        model = Eeg
        fields = ['patient', 'eegfile', 'eegtitle']

