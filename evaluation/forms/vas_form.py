from django import forms
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from evaluation.models.vas import VAS


class VASForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VASForm, self).__init__(*args, **kwargs)
        self.fields['side'].choices = VAS.VAS_SIDE

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = VAS
        fields = ['side', 'pain', 'anxiety']

        widgets = {
            'side': ButtonRadioHorizontalLabelSelect(),
            'pain': StepNumberInput(attrs={'min': 0, 'max': 10, 'step': 0.1}),
            'anxiety': StepNumberInput(attrs={'min': 0, 'max': 10, 'step': 0.1}),
        }