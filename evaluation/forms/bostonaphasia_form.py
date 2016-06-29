# -*- coding: utf-8 -*-
from django import forms
from ..widgets import StepNumberInput


class BostonAphasiaForm(forms.ModelForm):
    write_or_distribute_card_deck_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    write_or_distribute_card_deck_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)
