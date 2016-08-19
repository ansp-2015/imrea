# -*- coding: utf-8 -*-
from django import forms
from django.forms import NumberInput
from ..models.bostonaphasia import BostonAphasia
from ..widgets import StepNumberInput


class BostonAphasiaForm(forms.ModelForm):

    form_complex_ideational_1a_1b =  forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_2a_2b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_3a_3b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_4a_4b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_5a_5b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_6a_6b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_7a_7b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_8a_8b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_9a_9b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_10a_10b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_11a_11b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))
    form_complex_ideational_12a_12b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1, 'disabled': True}))


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)


    class Meta:
        model = BostonAphasia
        fields = ('complex_ideational_1a', 'complex_ideational_1b')
        widgets = {
            # EDINBURG HANDEDNESS
            'edinburg_handedness_writing_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_writing_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_drawing_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_drawing_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_throwing_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_throwing_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_ashtray_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_ashtray_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_toothbrush_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_toothbrush_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_fork_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_fork_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_broom_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_broom_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_striking_match_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_striking_match_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_spoon_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_using_spoon_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_opening_box_left_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'edinburg_handedness_opening_box_right_hand': StepNumberInput(attrs={'min': 0, 'max': 2}),

            'complex_ideational_1a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_1b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_2a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_2b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_3a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_3b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_4a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_4b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_5a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_5b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_6a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_6b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_7a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_7b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_8a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_8b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_9a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_9b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_10a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_10b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_11a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_11b': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_12a': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'complex_ideational_12b': StepNumberInput(attrs={'min': 0, 'max': 1}),

            'oral_agility_lips_purse': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'oral_agility_mouth_open': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'oral_agility_lips_retract': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'oral_agility_tongue_corner': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'oral_agility_tongue_protude': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'oral_agility_tongue_teeth': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_a': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_b': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_c': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_d': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_e': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_f': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'verbal_agility_g': StepNumberInput(attrs={'min': 0, 'max': 2}),

            'automzatized_days_week': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'automzatized_months_year': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'automzatized_counting_21': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'automzatized_alphabet': StepNumberInput(attrs={'min': 0, 'max': 2}),

            'reciting_score': StepNumberInput(attrs={'min': 0, 'max': 2}),
            'singing_score': StepNumberInput(attrs={'min': 0, 'max': 2}),

            'repetition_words_what_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_chair_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_hammock_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_purple_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_brown_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_w_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_fifteen_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_1776_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_emphasize_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_words_episcopal_score': StepNumberInput(attrs={'min': 0, 'max': 1}),

            'repetition_phrases_high_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_high_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'repetition_phrases_low_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),

            'word_reading_chair_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_circle_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_hammock_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_triangle_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_fifteen_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_purple_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_seven_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_dripping_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_brown_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'word_reading_smoking_score': StepNumberInput(attrs={'min': 0, 'max': 3}),

            'responsive_naming_time_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_razor_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_soap_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_pencil_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_paper_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_grass_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_cigarette_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_dozen_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_coal_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'responsive_naming_medicine_score': StepNumberInput(attrs={'min': 0, 'max': 3}),

        }


