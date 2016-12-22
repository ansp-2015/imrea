# -*- coding: utf-8 -*-
from ..widgets import StepNumberInput
from ..models.ftt import FTT
from .base_form import BaseForm


class FTTForm(BaseForm):

    def get_nt_fields(self):
        return ('paretic_hand_first', 'healthy_hand_first', 'paretic_hand_second', 'healthy_hand_second',
                'paretic_hand_third', 'healthy_hand_third')


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = FTT
        fields = ['paretic_hand_first', 'healthy_hand_first', 'paretic_hand_second', 'healthy_hand_second',
                  'paretic_hand_third', 'healthy_hand_third']

        widgets = {
            'paretic_hand_first': StepNumberInput(attrs={'min': 0}),
            'healthy_hand_first': StepNumberInput(attrs={'min': 0}),
            'paretic_hand_second': StepNumberInput(attrs={'min': 0}),
            'healthy_hand_second': StepNumberInput(attrs={'min': 0}),
            'paretic_hand_third': StepNumberInput(attrs={'min': 0}),
            'healthy_hand_third': StepNumberInput(attrs={'min': 0}),
        }