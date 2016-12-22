# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import NumberInput
from .base_form import BaseForm
from ..models.bostonaphasia import BostonAphasia, BostonAphasiaVisualConfrontation, BostonAphasiaAnimalNaming, \
    BostonAphasiaOralSentenceReading, BostonAphasiaSymbolWordDisc, BostonAphasiaWordRecognition, \
    BostonAphasiaOralSpelling, BostonAphasiaWordPictureMatching, BostonAphasiaReadingSentences, \
    BostonAphasiaRecallWrittenSymbols, BostonAphasiaDictatedWords, BostonAphasiaCopyPangramPhrase, \
    BostonAphasiaSpellingDictation, BostonAphasiaWrittenPictureNaming, BostonAphasiaNarrativeWriting, \
    BostonAphasiaSentecesWrittenDictation
from ..widgets import StepNumberInput


class BostonAphasiaConfrontationForm(BaseForm):
    def get_nt_fields(self):
        return ('confrontation_card2_h_score', 'confrontation_card2_t_score', 'confrontation_card2_r_score',
                'confrontation_card2_l_score', 'confrontation_card2_s_score', 'confrontation_card2_g_score',
                'confrontation_card2_square_score', 'confrontation_card2_chair_score', 'confrontation_card2_key_score',
                'confrontation_card2_glove_score', 'confrontation_card2_feather_score', 'confrontation_card2_hammock_score',
                'confrontation_card2_cactus_score', 'confrontation_card2_triangle_score',
                'confrontation_card3_red_score', 'confrontation_card3_brown_score', 'confrontation_card3_pink_score',
                'confrontation_card3_blue_score', 'confrontation_card3_gray_score', 'confrontation_card3_purple_score',
                'confrontation_card3_7_score', 'confrontation_card3_15_score', 'confrontation_card3_700_score',
                'confrontation_card3_1936_score', 'confrontation_card3_42_score', 'confrontation_card3_7000_score',
                'confrontation_card3_smoking_score', 'confrontation_card3_dripping_score', 'confrontation_card3_falling_score',
                'confrontation_card3_sleeping_score', 'confrontation_card3_drinking_score', 'confrontation_card3_running_score',
                'confrontation_body_ear_score', 'confrontation_body_nose_score', 'confrontation_body_elbow_score',
                'confrontation_body_ankle_score', 'confrontation_body_wrist_score', 'confrontation_body_shoulder_score',
                )

    def get_nt_field_prefix(self):
        return 'visualconfrontation-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaVisualConfrontation
        fields = '__all__'
        widgets = {
            'confrontation_card2_h_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_t_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_r_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_l_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_s_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_g_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_square_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_chair_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_key_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_glove_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_feather_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_hammock_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_cactus_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card2_triangle_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_red_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_brown_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_pink_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_blue_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_gray_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_purple_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_7_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_15_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_700_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_1936_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_42_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_7000_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_smoking_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_dripping_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_falling_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_sleeping_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_drinking_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_card3_running_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_body_ear_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_body_nose_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_body_elbow_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_body_ankle_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_body_wrist_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
            'confrontation_body_shoulder_score': StepNumberInput(attrs={'min': 0, 'max': 3}),
        }


class BostonAphasiaAnimalNamingForm(BaseForm):
    def get_nt_fields(self):
        return ('animal_naming_score',
                )

    def get_nt_field_prefix(self):
        return 'animalnaming-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaAnimalNaming
        fields = '__all__'
        widgets = {
            'animal_naming_score': StepNumberInput(attrs={'min': 0, 'max': 90}),
        }


class BostonAphasiaOralSentenceReadingForm(BaseForm):
    def get_nt_fields(self):
        return ('sentence_reading_a_score', 'sentence_reading_b_score', 'sentence_reading_c_score',
                'sentence_reading_d_score', 'sentence_reading_e_score',
                'sentence_reading_f_score', 'sentence_reading_g_score', 'sentence_reading_h_score',
                'sentence_reading_i_score', 'sentence_reading_j_score',
                )

    def get_nt_field_prefix(self):
        return 'oralsentencereading-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaOralSentenceReading
        fields = '__all__'
        widgets = {
            'sentence_reading_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_i_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'sentence_reading_j_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaSymbolWordDiscForm(BaseForm):
    def get_nt_fields(self):
        return ('symbol_word_card8_a_score', 'symbol_word_card8_b_score', 'symbol_word_card8_c_score',
                'symbol_word_card8_d_score', 'symbol_word_card8_e_score',
                'symbol_word_card9_a_score', 'symbol_word_card9_b_score', 'symbol_word_card9_c_score',
                'symbol_word_card9_d_score', 'symbol_word_card9_e_score',
                )

    def get_nt_field_prefix(self):
        return 'symbolworddisc-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaSymbolWordDisc
        fields = '__all__'
        widgets = {
            'symbol_word_card8_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card8_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card8_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card8_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card8_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card9_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card9_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card9_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card9_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'symbol_word_card9_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaWordRecognitionForm(BaseForm):
    def get_nt_fields(self):
        return ('word_recognition_a_score', 'word_recognition_b_score', 'word_recognition_c_score',
                'word_recognition_d_score', 'word_recognition_e_score', 'word_recognition_f_score',
                'word_recognition_g_score', 'word_recognition_h_score',)

    def get_nt_field_prefix(self):
        return 'wordrecognition-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaWordRecognition
        fields = '__all__'
        widgets = {
            'word_recognition_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_recognition_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaOralSpellingForm(BaseForm):
    def get_nt_fields(self):
        return ('oral_spelling_a_score', 'oral_spelling_b_score', 'oral_spelling_c_score',
                'oral_spelling_d_score', 'oral_spelling_e_score', 'oral_spelling_f_score',
                'oral_spelling_g_score', 'oral_spelling_h_score',)

    def get_nt_field_prefix(self):
        return 'oralspelling-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaOralSpelling
        fields = '__all__'
        widgets = {
            'oral_spelling_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'oral_spelling_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaWordPictureMatchingForm(BaseForm):
    def get_nt_fields(self):
        return ('word_picture_chair_score', 'word_picture_circle_score', 'word_picture_hammock_score',
                'word_picture_triangle_score', 'word_picture_fifteen_score', 'word_picture_purple_score',
                'word_picture_seven_t_o_score', 'word_picture_dripping_score', 'word_picture_brown_score',
                'word_picture_smoking_score',)

    def get_nt_field_prefix(self):
        return 'wordpicturematching-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaWordPictureMatching
        fields = '__all__'
        widgets = {
            'word_picture_chair_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_circle_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_hammock_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_triangle_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_fifteen_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_purple_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_seven_t_o_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_dripping_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_brown_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'word_picture_smoking_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaReadingSentencesForm(BaseForm):
    def get_nt_fields(self):
        return ('reading_sentences_dog_score', 'reading_sentences_mother_score', 'reading_sentences_haircut_score',
                'reading_sentences_bird_score', 'reading_sentences_school_score', 'reading_sentences_artist_score',
                'reading_sentences_aluminum_score', 'reading_sentences_sanitation_score',
                'reading_sentences_civil_service_score', 'reading_sentences_government_score',)

    def get_nt_field_prefix(self):
        return 'readingsentences-0-'

    reading_sentences_dog_items = (_('Talk'), _('Bark'), _('Sing'), _('Cat'), )
    reading_sentences_mother_items = (_('Tree'), _('Cook'), _('Child'), _('Truck'),)
    reading_sentences_haircut_items = (_('Shaving'), _('Boy'), _('Butcher'), _('Barber'),)
    reading_sentences_bird_items = (_('Nests'), _('Eggs'), _('Sparrow'), _('Cat'),)
    reading_sentences_school_items = (_('Houses'), _('Country'), _('Taxes'), _('Police'),)
    reading_sentences_artist_items = (_('Picture'), _('Musician'), _('Library'), _('Soldier'),)
    reading_sentences_aluminum_items = (_('Very strong'), _('A miner'), _('Electronic'), _('Much cheaper'),)
    reading_sentences_sanitation_items = (_('Sanitation'), _('Good food'), _('Pasteur\' discovery'), _('Germs'),)
    reading_sentences_civil_service_items = (_('Achieve higher salaries'), _('Establish favoritism'), _('Effect a reduction in taxes'), _('Match the salary to the duties'),)
    reading_sentences_government_items = (_('Local affairs above all'), _('The price of lumber'), _('The actions of the government'), _('The authority of town officials'),)

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaReadingSentences
        fields = '__all__'
        widgets = {
            'reading_sentences_dog_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_mother_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_haircut_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_bird_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_school_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_artist_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_aluminum_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_sanitation_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_civil_service_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'reading_sentences_government_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaMechanicsWritingForm(BaseForm):
    def get_nt_fields(self):
        return ('mechanics_writing_score',)

    def get_nt_field_prefix(self):
        return 'mechanicswriting-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaReadingSentences
        fields = '__all__'
        widgets = {
            'mechanics_writing_score': StepNumberInput(attrs={'min': 0, 'max': 5}),
        }


class BostonAphasiaRecallWrittenSymbolsForm(BaseForm):
    def get_nt_fields(self):
        return ('serial_writing_letters_score',)

    def get_nt_field_prefix(self):
        return 'recallwrittensymbols-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaRecallWrittenSymbols
        fields = '__all__'
        widgets = {
            'serial_writing_letters_score': StepNumberInput(attrs={'min': 0, 'max': 26}),
            #'serial_writing_numbers_score': StepNumberInput(attrs={'min': 0, 'max': 21}),
        }


class BostonAphasiaDictatedWordsForm(BaseForm):
    def get_nt_fields(self):
        return ('dictated_words_letters_score', 'dictated_words_numbers_score', 'dictated_words_words_score',)

    def get_nt_field_prefix(self):
        return 'dictatedwords-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaDictatedWords
        fields = '__all__'
        widgets = {
            'dictated_words_letters_score': StepNumberInput(attrs={'min': 0, 'max': 5}),
            'dictated_words_numbers_score': StepNumberInput(attrs={'min': 0, 'max': 5}),
            'dictated_words_words_score': StepNumberInput(attrs={'min': 0, 'max': 5}),
        }


class BostonAphasiaCopyPangramPhraseForm(BaseForm):
    def get_nt_fields(self):
        return ('copy_pangram_phrase_score', )

    def get_nt_field_prefix(self):
        return 'copypangramphrase-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaCopyPangramPhrase
        fields = '__all__'
        widgets = {
            'copy_pangram_phrase_score': StepNumberInput(attrs={'min': 0, 'max': 4}),
        }


class BostonAphasiaSpellingDictationForm(BaseForm):
    def get_nt_fields(self):
        return ('spelling_dictation_a_score', 'spelling_dictation_b_score',
                'spelling_dictation_c_score', 'spelling_dictation_d_score',
                'spelling_dictation_e_score', 'spelling_dictation_f_score',
                'spelling_dictation_g_score', 'spelling_dictation_h_score',
                'spelling_dictation_i_score', 'spelling_dictation_j_score',
                )

    def get_nt_field_prefix(self):
        return 'spellingdictation-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaSpellingDictation
        fields = '__all__'
        widgets = {
            'spelling_dictation_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_i_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'spelling_dictation_j_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaWrittenPictureNamingForm(BaseForm):
    def get_nt_fields(self):
        return ('written_picture_naming_a_score', 'written_picture_naming_b_score',
                'written_picture_naming_c_score', 'written_picture_naming_d_score',
                'written_picture_naming_e_score', 'written_picture_naming_f_score',
                'written_picture_naming_g_score', 'written_picture_naming_h_score',
                'written_picture_naming_i_score', 'written_picture_naming_j_score',
                )

    def get_nt_field_prefix(self):
        return 'writtenpicturenaming-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaWrittenPictureNaming
        fields = '__all__'
        widgets = {
            'written_picture_naming_a_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_b_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_c_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_d_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_e_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_f_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_g_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_h_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_i_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
            'written_picture_naming_j_score': StepNumberInput(attrs={'min': 0, 'max': 1}),
        }


class BostonAphasiaNarrativeWritingForm(BaseForm):
    def get_nt_fields(self):
        return ('narrative_writing_score',)

    def get_nt_field_prefix(self):
        return 'narrativewriting-0-'


    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaNarrativeWriting
        fields = '__all__'
        widgets = {
            'narrative_writing_score': StepNumberInput(attrs={'min': 0, 'max': 5}),
        }


class BostonAphasiaSentecesWrittenDictationForm(BaseForm):
    def get_nt_fields(self):
        return ('sentences_written_dictation_a_score',
                'sentences_written_dictation_b_score',
                'sentences_written_dictation_c_score',)

    def get_nt_field_prefix(self):
        return 'senteceswrittendictation-0-'

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasiaSentecesWrittenDictation
        fields = '__all__'
        widgets = {
            'sentences_written_dictation_a_score': StepNumberInput(attrs={'min': 0, 'max': 4}),
            'sentences_written_dictation_b_score': StepNumberInput(attrs={'min': 0, 'max': 4}),
            'sentences_written_dictation_c_score': StepNumberInput(attrs={'min': 0, 'max': 4}),
        }




class BostonAphasiaForm(BaseForm):
    def get_nt_fields(self):
        return (
            'edinburg_handedness_writing_left_hand', 'edinburg_handedness_writing_right_hand',
            'edinburg_handedness_drawing_left_hand', 'edinburg_handedness_drawing_right_hand',
            'edinburg_handedness_throwing_left_hand', 'edinburg_handedness_throwing_right_hand',
            'edinburg_handedness_using_ashtray_left_hand', 'edinburg_handedness_using_ashtray_right_hand',
            'edinburg_handedness_using_toothbrush_left_hand', 'edinburg_handedness_using_toothbrush_right_hand',
            'edinburg_handedness_using_fork_left_hand', 'edinburg_handedness_using_fork_right_hand',
            'edinburg_handedness_using_broom_right_hand', 'edinburg_handedness_using_broom_left_hand',
            'edinburg_handedness_striking_match_left_hand', 'edinburg_handedness_striking_match_right_hand',
            'edinburg_handedness_using_spoon_left_hand', 'edinburg_handedness_using_spoon_right_hand',
            'edinburg_handedness_opening_box_left_hand', 'edinburg_handedness_opening_box_right_hand',

            'complex_ideational_1a', 'complex_ideational_1b',
            'complex_ideational_2a', 'complex_ideational_2b',
            'complex_ideational_3a', 'complex_ideational_3b',
            'complex_ideational_4a', 'complex_ideational_4b',
            'complex_ideational_5a', 'complex_ideational_5b',
            'complex_ideational_6a', 'complex_ideational_6b',
            'complex_ideational_7a', 'complex_ideational_7b',
            'complex_ideational_8a', 'complex_ideational_8b',
            'complex_ideational_9a', 'complex_ideational_9b',
            'complex_ideational_10a', 'complex_ideational_10b',
            'complex_ideational_11a', 'complex_ideational_11b',
            'complex_ideational_12a', 'complex_ideational_12b',

            'oral_agility_lips_purse', 'oral_agility_mouth_open', 'oral_agility_lips_retract',
            'oral_agility_tongue_corner', 'oral_agility_tongue_protude', 'oral_agility_tongue_teeth',
            'verbal_agility_a', 'verbal_agility_b', 'verbal_agility_c', 'verbal_agility_d',
            'verbal_agility_e', 'verbal_agility_f', 'verbal_agility_g',

            'automzatized_days_week', 'automzatized_months_year', 'automzatized_counting_21', 'automzatized_alphabet',

            'reciting_score', 'singing_score',

            'repetition_words_what_score', 'repetition_words_chair_score', 'repetition_words_hammock_score',
            'repetition_words_purple_score', 'repetition_words_brown_score',
            'repetition_words_w_score', 'repetition_words_fifteen_score',
            'repetition_words_1776_score', 'repetition_words_emphasize_score',
            'repetition_words_episcopal_score',

            'repetition_phrases_high_a_score', 'repetition_phrases_high_b_score', 'repetition_phrases_high_c_score',
            'repetition_phrases_high_d_score', 'repetition_phrases_high_e_score', 'repetition_phrases_high_f_score',
            'repetition_phrases_high_g_score', 'repetition_phrases_high_h_score',
            'repetition_phrases_low_a_score', 'repetition_phrases_low_b_score', 'repetition_phrases_low_c_score',
            'repetition_phrases_low_d_score', 'repetition_phrases_low_e_score', 'repetition_phrases_low_f_score',
            'repetition_phrases_low_g_score', 'repetition_phrases_low_h_score',

            'word_reading_chair_score', 'word_reading_circle_score', 'word_reading_hammock_score',
            'word_reading_triangle_score', 'word_reading_fifteen_score', 'word_reading_purple_score',
            'word_reading_seven_score', 'word_reading_dripping_score', 'word_reading_brown_score',
            'word_reading_smoking_score',

            'responsive_naming_time_score', 'responsive_naming_razor_score', 'responsive_naming_soap_score',
            'responsive_naming_pencil_score', 'responsive_naming_paper_score', 'responsive_naming_grass_score',
            'responsive_naming_cigarette_score', 'responsive_naming_dozen_score', 'responsive_naming_coal_score',
            'responsive_naming_medicine_score',
        )

    # fields to be used as counters
    form_complex_ideational_1a_1b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_2a_2b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_3a_3b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_4a_4b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_5a_5b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_6a_6b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_7a_7b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_8a_8b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_9a_9b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_10a_10b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_11a_11b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))
    form_complex_ideational_12a_12b = forms.IntegerField(widget=NumberInput(attrs={'min': 0, 'max': 1}))

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)

    class Meta:
        model = BostonAphasia
        fields = '__all__'
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


