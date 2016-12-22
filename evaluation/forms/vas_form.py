# -*- coding: utf-8 -*-
from ..widgets import ButtonRadioHorizontalLabelSelect, StepNumberInput
from .base_form import BaseForm
from ..models.vas import VAS


class VASForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super(VASForm, self).__init__(*args, **kwargs)
        self.fields['side'].choices = VAS.VAS_SIDE

    def get_nt_fields(self):
        return ('pain', 'anxiety',)


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
            'anxiety': StepNumberInput(attrs={'min': 0, 'max': 10, 'step': 0.1, 'NT': True}),
        }