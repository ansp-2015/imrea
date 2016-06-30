# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models import MMSE


class MMSEForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MMSEForm, self).__init__(*args, **kwargs)
        self.fields['orientation_day_week'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_day_week'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_day_month'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_month'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_year'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_time'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_place'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_institution'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_district'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_city'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['orientation_state'].choices = MMSE.MMSE_ORIENTATION_CHOICES
        self.fields['registration_words'].choices = MMSE.MMSE_REGISTRATION_CHOICES
        self.fields['attention_calc'].choices = MMSE.MMSE_ATTENTION_CHOICES
        self.fields['recall_words'].choices = MMSE.MMSE_RECALL_CHOICES
        self.fields['language_watch_pen'].choices = MMSE.MMSE_LANGUAGE_PEN_CHOICES
        self.fields['language_repeat'].choices = MMSE.MMSE_LANGUAGE_REPEAT_CHOICES
        self.fields['language_command'].choices = MMSE.MMSE_LANGUAGE_COMMAND_CHOICES
        self.fields['language_read'].choices = MMSE.MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES
        self.fields['language_write'].choices = MMSE.MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES
        self.fields['language_copy'].choices = MMSE.MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = MMSE
        fields = ['orientation_day_week', 'orientation_day_month', 'orientation_month', 'orientation_year',
                  'orientation_time', 'orientation_place', 'orientation_institution', 'orientation_district',
                  'orientation_city', 'orientation_state', 'registration_words', 'attention_calc',
                  'recall_words', 'language_watch_pen', 'language_repeat', 'language_command',
                  'language_read', 'language_write', 'language_copy', 'obs']
        widgets = {
            'orientation_day_week': ButtonRadioHorizontalValueSelect(),
            'orientation_day_month': ButtonRadioHorizontalValueSelect(),
            'orientation_month': ButtonRadioHorizontalValueSelect(),
            'orientation_year': ButtonRadioHorizontalValueSelect(),
            'orientation_time': ButtonRadioHorizontalValueSelect(),
            'orientation_place': ButtonRadioHorizontalValueSelect(),
            'orientation_institution': ButtonRadioHorizontalValueSelect(),
            'orientation_district': ButtonRadioHorizontalValueSelect(),
            'orientation_city': ButtonRadioHorizontalValueSelect(),
            'orientation_state': ButtonRadioHorizontalValueSelect(),
            'registration_words': ButtonRadioHorizontalValueSelect(),
            'attention_calc': ButtonRadioHorizontalValueSelect(),
            'recall_words': ButtonRadioHorizontalValueSelect(),
            'language_watch_pen': ButtonRadioHorizontalValueSelect(),
            'language_repeat': ButtonRadioHorizontalValueSelect(),
            'language_command': ButtonRadioHorizontalValueSelect(),
            'language_read': ButtonRadioHorizontalValueSelect(),
            'language_write': ButtonRadioHorizontalValueSelect(),
            'language_copy': ButtonRadioHorizontalValueSelect(),
        }
