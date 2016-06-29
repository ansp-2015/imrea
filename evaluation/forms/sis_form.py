# -*- coding: utf-8 -*-
from django import forms


class SISForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
