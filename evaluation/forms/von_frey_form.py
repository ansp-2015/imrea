from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from evaluation.models.von_frey import VonFrey


class VonFreyForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = VonFrey
        fields = ['sensibility1_forearm_right', 'sensibility1_forearm_left', 'sensibility1_thenar_right',
                  'sensibility1_thenar_left', 'sensibility2_forearm_right', 'sensibility2_forearm_left',
                  'sensibility2_thenar_right', 'sensibility2_thenar_left', 'algometer1_forearm_right',
                  'algometer1_forearm_left', 'algometer1_thenar_right', 'algometer1_thenar_left',
                  'algometer2_forearm_right', 'algometer2_forearm_left', 'algometer2_thenar_right',
                  'algometer2_thenar_left', 'algometer3_forearm_right', 'algometer3_forearm_left',
                  'algometer3_thenar_right','algometer3_thenar_left', 'obs']

        widgets = {
            'sensibility1_forearm_right': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility1_forearm_left': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility1_thenar_right': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility1_thenar_left': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility2_forearm_right': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility2_forearm_left': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility2_thenar_right': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'sensibility2_thenar_left': StepNumberInput(attrs={'min': 0, 'step': 0.05, 'decimals': 2}),
            'algometer1_forearm_right': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer1_forearm_left': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer1_thenar_right': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer1_thenar_left': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer2_forearm_right': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer2_forearm_left': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer2_thenar_right': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer2_thenar_left': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer3_forearm_right': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer3_forearm_left': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer3_thenar_right': StepNumberInput(attrs={'min': 0, 'step': 0.5}),
            'algometer3_thenar_left': StepNumberInput(attrs={'min': 0, 'step': 0.5})
        }