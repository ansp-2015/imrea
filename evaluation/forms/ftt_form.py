from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from evaluation.models.ftt import FTT


class FTTForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = FTT
        fields = ['paretic_hand_first', 'healthy_hand_first', 'paretic_hand_second', 'healthy_hand_second',
                  'paretic_hand_third', 'healthy_hand_third']

