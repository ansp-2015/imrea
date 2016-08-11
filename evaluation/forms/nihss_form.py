# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from ..models.nihss import NIHSS

class NIHSSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NIHSSForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            if f not in ['patient', 'period']:
                choices = self.fields[f].choices
                self.fields[f].choices = choices[1:]

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = NIHSS
        fields = ['loc', 'loc_questions', 'loc_commands', 'best_gaze', 'visual', 'facial_palsy', 'motor_arm_left',
                  'motor_arm_right', 'motor_leg_left', 'motor_leg_right', 'limb_ataxia', 'sensory', 'best_language',
                  'dysarthria', 'extinction']

        widgets = {
            'loc': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LOC)-1}),
            'loc_questions': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LOC_QUESTIONS) - 1}),
            'loc_commands': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LOC_COMMANDS) - 1}),
            'best_gaze': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_BEST_GAZE) - 1}),
            'visual': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_VISUAL) - 1}),
            'facial_palsy': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_FACIAL_PALSY) - 1}),
            'motor_arm_left': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_ARM) - 1}),
            'motor_arm_right': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_ARM) - 1}),
            'motor_leg_left': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_LEG) - 1}),
            'motor_leg_right': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_LEG) - 1}),
            'limb_ataxia': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LIMB_ATAXIA) - 1}),
            'sensory': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_SENSORY) -1}),
            'best_language': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_BEST_LANGUAGE) -1}),
            'dysarthria': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_DYSARTHRIA) -1}),
            'extinction': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_EXTINCTION)})
        }
