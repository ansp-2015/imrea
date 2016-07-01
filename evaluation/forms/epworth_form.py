from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models import Epworth


class EpworthForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EpworthForm, self).__init__(*args, **kwargs)
        self.fields['sitting_reading'].choices = Epworth.EPWORTH_CHOICES
        self.fields['watching_tv'].choices = Epworth.EPWORTH_CHOICES
        self.fields['sitting_inactive_public'].choices = Epworth.EPWORTH_CHOICES
        self.fields['car_passenger'].choices = Epworth.EPWORTH_CHOICES
        self.fields['lying_down'].choices = Epworth.EPWORTH_CHOICES
        self.fields['sitting_talking'].choices = Epworth.EPWORTH_CHOICES
        self.fields['sitting_quietly_lunch'].choices = Epworth.EPWORTH_CHOICES
        self.fields['car_traffic'].choices = Epworth.EPWORTH_CHOICES

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = Epworth
        fields = ['sitting_reading', 'watching_tv', 'sitting_inactive_public', 'car_passenger', 'lying_down',
                  'sitting_talking', 'sitting_quietly_lunch', 'car_traffic']

        widgets = {
            'sitting_reading': ButtonRadioHorizontalValueSelect(),
            'watching_tv': ButtonRadioHorizontalValueSelect(),
            'sitting_inactive_public': ButtonRadioHorizontalValueSelect(),
            'car_passenger': ButtonRadioHorizontalValueSelect(),
            'lying_down': ButtonRadioHorizontalValueSelect(),
            'sitting_talking': ButtonRadioHorizontalValueSelect(),
            'sitting_quietly_lunch': ButtonRadioHorizontalValueSelect(),
            'car_traffic': ButtonRadioHorizontalValueSelect(),
        }