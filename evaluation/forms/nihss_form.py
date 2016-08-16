# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from ..models.nihss import NIHSS
from django.utils.translation import ugettext_lazy as _


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
            'loc': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LOC)-1,
                                          'description': NIHSS.NIH_LOC_DESCRIPTION}),
            'loc_questions': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LOC_QUESTIONS) - 1,
                                                    'description': NIHSS.NIH_LOC_QUESTIONS_DESCRIPTION}),
            'loc_commands': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LOC_COMMANDS) - 1,
                                                   'description': NIHSS.NIH_LOC_COMMANDS_DESCRIPTION}),
            'best_gaze': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_BEST_GAZE) - 1,
                                                'description': NIHSS.NIH_BEST_GAZE_DESCRIPTION}),
            'visual': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_VISUAL) - 1,
                                             'description': NIHSS.NIH_VISUAL_DESCRIPTION}),
            'facial_palsy': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_FACIAL_PALSY) - 1,
                                                   'description': NIHSS.NIH_FACIAL_PALSY_DESCRIPTION}),
            'motor_arm_left': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_ARM) - 1,
                                                     'label': _(u'Left arm'),
                                                     'description': NIHSS.NIH_MOTOR_ARM_DESCRIPTION}),
            'motor_arm_right': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_ARM) - 1,
                                                      'label': _(u'Right arm')}),
            'motor_leg_left': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_LEG) - 1,
                                                     'label': _('Left leg'),
                                                     'description': NIHSS.NIH_MOTOR_LEG_DESCRIPTION}),
            'motor_leg_right': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_MOTOR_LEG) - 1,
                                                      'label': _(u'Right leg')}),
            'limb_ataxia': StepNumberInput(attrs={'min': 0, 'max': len(NIHSS.NIH_LIMB_ATAXIA) - 1,
                                                  'description': NIHSS.NIH_LIMB_ATAXIA_DESCRIPTION}),
            'sensory': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_SENSORY) - 1,
                                              'description': NIHSS.NIH_SENSORY_DESCRIPTION}),
            'best_language': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_BEST_LANGUAGE) - 1,
                                                    'description': NIHSS.NIH_BEST_LANGUAGE_DESCRIPTION}),
            'dysarthria': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_DYSARTHRIA) - 1,
                                                 'description': NIHSS.NIH_DYSARTHRIA_DESCRIPTION}),
            'extinction': StepNumberInput(attrs={'min':0, 'max': len(NIHSS.NIH_EXTINCTION) - 1,
                                                 'description': NIHSS.NIH_EXTINCTION_DESCRIPTION})
        }
