from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from evaluation.models.verbal_fluency import VerbalFluency


class VerbalFluencyForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = VerbalFluency
        fields = ['fas_words', 'fas_count', 'fas_obs', 'animals_words', 'animals_count', 'animals_obs']

        widgets = {
            'fas_count': StepNumberInput(attrs={'min': 0}),
            'animals_count': StepNumberInput(attrs={'min': 0}),
        }