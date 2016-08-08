# -*- coding: utf-8 -*-
from django import forms
from ..widgets import StepNumberInput


class BostonAphasiaForm(forms.ModelForm):
    # EDINBURG HANDEDNESS
    edinburg_handedness_writing_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_writing_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_drawing_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_drawing_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_throwing_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_throwing_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_using_ashtray_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_using_ashtray_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_using_toothbrush_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_using_toothbrush_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_using_fork_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_using_fork_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_using_broom_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_using_broom_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_striking_match_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_striking_match_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_using_spoon_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_using_spoon_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    edinburg_handedness_opening_box_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))
    edinburg_handedness_opening_box_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 2}))

    form_complex_ideational_1a_1b =  forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_2a_2b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_3a_3b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_4a_4b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_5a_5b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_6a_6b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_7a_7b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_8a_8b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_9a_9b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_10a_10b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_11a_11b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_12a_12b = forms.IntegerField(widget=StepNumberInput(attrs={'min': 0, 'max': 1}))

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)
