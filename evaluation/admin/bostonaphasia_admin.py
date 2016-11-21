from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.options import InlineModelAdmin
from django.forms import fields, models, formsets, widgets, inlineformset_factory
from reversion_compare.helpers import patch_admin
from ..models.bostonaphasia import BostonAphasia, BostonAphasiaVisualConfrontation, \
    BostonAphasiaAnimalNaming, BostonAphasiaOralSentenceReading, BostonAphasiaSymbolWordDisc, \
    BostonAphasiaWordRecognition, BostonAphasiaOralSpelling, BostonAphasiaWordPictureMatching, \
    BostonAphasiaReadingSentences, BostonAphasiaMechanicsWriting, BostonAphasiaRecallWrittenSymbols, \
    BostonAphasiaDictatedWords, BostonAphasiaCopyPangramPhrase, BostonAphasiaSpellingDictation, \
    BostonAphasiaWrittenPictureNaming, BostonAphasiaNarrativeWriting, BostonAphasiaSentecesWrittenDictation
from .base_admin import BaseAdmin
from ..forms.bostonaphasia_form import \
    BostonAphasiaForm, BostonAphasiaConfrontationForm, \
    BostonAphasiaAnimalNamingForm, BostonAphasiaOralSentenceReadingForm, BostonAphasiaSymbolWordDiscForm, \
    BostonAphasiaWordRecognitionForm, BostonAphasiaOralSpellingForm, BostonAphasiaWordPictureMatchingForm, \
    BostonAphasiaReadingSentencesForm, BostonAphasiaMechanicsWritingForm, BostonAphasiaRecallWrittenSymbolsForm, \
    BostonAphasiaDictatedWordsForm, BostonAphasiaCopyPangramPhraseForm, BostonAphasiaSpellingDictationForm, \
    BostonAphasiaWrittenPictureNamingForm, BostonAphasiaNarrativeWritingForm, BostonAphasiaSentecesWrittenDictationForm


class BostonAphasiaVisualConfrontationInlineAdmin(InlineModelAdmin):
    #template = 'admin/edit_inline/evaluation.html'
    form = BostonAphasiaConfrontationForm
    model = BostonAphasiaVisualConfrontation
    extra = 1
    max_num = 1

    fieldsets = (_(u'Visual confrontation naming'), {
            'fields': (
                ('confrontation_card2_h_answer', 'confrontation_card2_h_score', 'confrontation_card2_h_articulation', 'confrontation_card2_h_paraphasia'),
                ('confrontation_card2_t_answer', 'confrontation_card2_t_score', 'confrontation_card2_t_articulation', 'confrontation_card2_t_paraphasia'),
                ('confrontation_card2_r_answer', 'confrontation_card2_r_score', 'confrontation_card2_r_articulation', 'confrontation_card2_r_paraphasia'),
                ('confrontation_card2_l_answer', 'confrontation_card2_l_score', 'confrontation_card2_l_articulation', 'confrontation_card2_l_paraphasia'),
                ('confrontation_card2_s_answer', 'confrontation_card2_s_score', 'confrontation_card2_s_articulation', 'confrontation_card2_s_paraphasia'),
                ('confrontation_card2_g_answer', 'confrontation_card2_g_score', 'confrontation_card2_g_articulation', 'confrontation_card2_g_paraphasia'),
                ('confrontation_card2_square_answer', 'confrontation_card2_square_score', 'confrontation_card2_square_articulation', 'confrontation_card2_square_paraphasia'),
                ('confrontation_card2_chair_answer', 'confrontation_card2_chair_score', 'confrontation_card2_chair_articulation', 'confrontation_card2_chair_paraphasia'),
                ('confrontation_card2_key_answer', 'confrontation_card2_key_score', 'confrontation_card2_key_articulation', 'confrontation_card2_key_paraphasia'),
                ('confrontation_card2_glove_answer', 'confrontation_card2_glove_score', 'confrontation_card2_glove_articulation', 'confrontation_card2_glove_paraphasia'),
                ('confrontation_card2_feather_answer', 'confrontation_card2_feather_score', 'confrontation_card2_feather_articulation', 'confrontation_card2_feather_paraphasia'),
                ('confrontation_card2_hammock_answer', 'confrontation_card2_hammock_score', 'confrontation_card2_hammock_articulation', 'confrontation_card2_hammock_paraphasia'),
                ('confrontation_card2_cactus_answer', 'confrontation_card2_cactus_score', 'confrontation_card2_cactus_articulation', 'confrontation_card2_cactus_paraphasia'),
                ('confrontation_card2_triangle_answer', 'confrontation_card2_triangle_score', 'confrontation_card2_triangle_articulation',
                 'confrontation_card2_triangle_paraphasia'),
                ('confrontation_card3_red_answer', 'confrontation_card3_red_score', 'confrontation_card3_red_articulation', 'confrontation_card3_red_paraphasia'),
                ('confrontation_card3_brown_answer', 'confrontation_card3_brown_score', 'confrontation_card3_brown_articulation', 'confrontation_card3_brown_paraphasia'),
                ('confrontation_card3_pink_answer', 'confrontation_card3_pink_score', 'confrontation_card3_pink_articulation', 'confrontation_card3_pink_paraphasia'),
                ('confrontation_card3_blue_answer', 'confrontation_card3_blue_score', 'confrontation_card3_blue_articulation', 'confrontation_card3_blue_paraphasia'),
                ('confrontation_card3_gray_answer', 'confrontation_card3_gray_score', 'confrontation_card3_gray_articulation', 'confrontation_card3_gray_paraphasia'),
                ('confrontation_card3_purple_answer', 'confrontation_card3_purple_score', 'confrontation_card3_purple_articulation', 'confrontation_card3_purple_paraphasia'),
                ('confrontation_card3_smoking_answer', 'confrontation_card3_smoking_score', 'confrontation_card3_smoking_articulation', 'confrontation_card3_smoking_paraphasia'),
                ('confrontation_card3_dripping_answer', 'confrontation_card3_dripping_score', 'confrontation_card3_dripping_articulation',
                 'confrontation_card3_dripping_paraphasia'),
                ('confrontation_card3_falling_answer', 'confrontation_card3_falling_score', 'confrontation_card3_falling_articulation', 'confrontation_card3_falling_paraphasia'),
                ('confrontation_card3_7_answer', 'confrontation_card3_7_score', 'confrontation_card3_7_articulation', 'confrontation_card3_7_paraphasia'),
                ('confrontation_card3_15_answer', 'confrontation_card3_15_score', 'confrontation_card3_15_articulation', 'confrontation_card3_15_paraphasia'),
                ('confrontation_card3_700_answer', 'confrontation_card3_700_score', 'confrontation_card3_700_articulation', 'confrontation_card3_700_paraphasia'),
                ('confrontation_card3_1936_answer', 'confrontation_card3_1936_score', 'confrontation_card3_1936_articulation', 'confrontation_card3_1936_paraphasia'),
                ('confrontation_card3_42_answer', 'confrontation_card3_42_score', 'confrontation_card3_42_articulation', 'confrontation_card3_42_paraphasia'),
                ('confrontation_card3_7000_answer', 'confrontation_card3_7000_score', 'confrontation_card3_7000_articulation', 'confrontation_card3_7000_paraphasia'),
                ('confrontation_card3_sleeping_answer', 'confrontation_card3_sleeping_score', 'confrontation_card3_sleeping_articulation',
                 'confrontation_card3_sleeping_paraphasia'),
                ('confrontation_card3_drinking_answer', 'confrontation_card3_drinking_score', 'confrontation_card3_drinking_articulation',
                 'confrontation_card3_drinking_paraphasia'),
                ('confrontation_card3_running_answer', 'confrontation_card3_running_score', 'confrontation_card3_running_articulation', 'confrontation_card3_running_paraphasia'),
                ('confrontation_body_ear_answer', 'confrontation_body_ear_score', 'confrontation_body_ear_articulation', 'confrontation_body_ear_paraphasia'),
                ('confrontation_body_nose_answer', 'confrontation_body_nose_score', 'confrontation_body_nose_articulation', 'confrontation_body_nose_paraphasia'),
                ('confrontation_body_elbow_answer', 'confrontation_body_elbow_score', 'confrontation_body_elbow_articulation', 'confrontation_body_elbow_paraphasia'),
                ('confrontation_body_ankle_answer', 'confrontation_body_ankle_score', 'confrontation_body_ankle_articulation', 'confrontation_body_ankle_paraphasia'),
                ('confrontation_body_wrist_answer', 'confrontation_body_wrist_score', 'confrontation_body_wrist_articulation', 'confrontation_body_wrist_paraphasia'),
                ('confrontation_body_shoulder_answer', 'confrontation_body_shoulder_score', 'confrontation_body_shoulder_articulation', 'confrontation_body_shoulder_paraphasia'),

            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_14_visual_confrontation',
                'text': _(u'Are you left or right-handed? Which hand you prefer for that activity? Do you ever use the other hand for the activity?'),
                'fieldset_total_points': '114',
                'fieldset_total_addend_field_prefix': 'bostonaphasiavisualconfrontation-0-',
                'fieldset_total_addend_fields': ('confrontation_card2_h_score', 'confrontation_card2_t_score', 'confrontation_card2_r_score',
                                                 'confrontation_card2_l_score', 'confrontation_card2_g_score', 'confrontation_card2_square_score',
                                                 'confrontation_card2_chair_score', 'confrontation_card2_key_score', 'confrontation_card2_glove_score',
                                                 'confrontation_card2_feather_score', 'confrontation_card2_hammock_score', 'confrontation_card2_cactus_score',
                                                 'confrontation_card2_triangle_score', 'confrontation_card3_red_score', 'confrontation_card3_brown_score',
                                                 'confrontation_card3_pink_score', 'confrontation_card3_blue_score', 'confrontation_card3_gray_score',
                                                 'confrontation_card3_purple_score', 'confrontation_card3_7_score', 'confrontation_card3_15_score',
                                                 'confrontation_card3_700_score', 'confrontation_card3_1936_score', 'confrontation_card3_42_score',
                                                 'confrontation_card3_7000_score', 'confrontation_card3_smoking_score', 'confrontation_card3_dripping_score',
                                                 'confrontation_card3_falling_score', 'confrontation_card3_sleeping_score', 'confrontation_card3_drinking_score',
                                                 'confrontation_card3_running_score', 'confrontation_body_ear_score', 'confrontation_body_nose_score',
                                                 'confrontation_body_elbow_score', 'confrontation_body_ankle_score', 'confrontation_body_wrist_score',
                                                 'confrontation_body_shoulder_score'),
                'fieldset_total_field': 'confrontation_total',
            }
        }),

class BostonAphasiaAnimalNamingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaAnimalNamingForm
    model = BostonAphasiaAnimalNaming
    extra = 1
    max_num = 1

    fieldsets = (_(u'Animal naming'), {
            'fields': (
                ('animal_naming_answer', 'animal_naming_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_15_animal_naming',
                'text': _(u'Instruct the patient \"I want to see how many different animals you can call to mind and name for about a minute, while I count them. Any animals will do; they can be from the farm, the jungle, the ocean or house pets. For instance you can start with dog.\" Start timing from this point and continue for a minute and a half. Score is based on the most productive consecutive 60 seconds. Record verbatim below.'),
            }
        }),


class BostonAphasiaOralSentenceReadingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaOralSentenceReadingForm
    model = BostonAphasiaOralSentenceReading
    extra = 1
    max_num = 1

    fieldsets = (_(u'Oral sentence-reading'), {
            'fields': (
                ('sentence_reading_a_score', 'sentence_reading_a_answer', ),
                ('sentence_reading_b_score', 'sentence_reading_b_answer', ),
                ('sentence_reading_c_score', 'sentence_reading_c_answer', ),
                ('sentence_reading_d_score', 'sentence_reading_d_answer', ),
                ('sentence_reading_e_score', 'sentence_reading_e_answer',),
                ('sentence_reading_f_score', 'sentence_reading_f_answer',),
                ('sentence_reading_g_score', 'sentence_reading_g_answer',),
                ('sentence_reading_h_score', 'sentence_reading_h_answer',),
                ('sentence_reading_i_score', 'sentence_reading_i_answer',),
                ('sentence_reading_j_score', 'sentence_reading_j_answer',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_16_oral_sentence',
                'text': _(u'Have the patient read the following sentences aloud. Indicate by marking on this record any assistance given, omissions, substitutions,etc. One point credit is allowed for each completely correct sentence.'),
                'fieldset_total_points': '10',
                'fieldset_total_addend_field_prefix': 'bostonaphasiaoralsentencereading-0-',
                'fieldset_total_addend_fields': ('sentence_reading_a_score', 'sentence_reading_b_score', 'sentence_reading_c_score',
                                                 'sentence_reading_d_score', 'sentence_reading_e_score', 'sentence_reading_f_score',
                                                 'sentence_reading_g_score', 'sentence_reading_h_score', 'sentence_reading_i_score',
                                                 'sentence_reading_j_score',
                                                 ),
                'fieldset_total_field': 'oral_sentence_total',
            }
        }),


class BostonAphasiaSymbolWordDiscInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaSymbolWordDiscForm
    model = BostonAphasiaSymbolWordDisc
    extra = 1
    max_num = 1

    fieldsets = (_(u'Oral sentence-reading'), {
            'fields': (
                ('symbol_word_card8_a_score', 'symbol_word_card8_b_score',
                'symbol_word_card8_c_score', 'symbol_word_card8_d_score',
                'symbol_word_card8_e_score',
                'symbol_word_card9_a_score', 'symbol_word_card9_b_score',
                'symbol_word_card9_c_score', 'symbol_word_card9_d_score',
                'symbol_word_card9_e_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_17_symbol_word',
                'text': _(u'Point to the letter or word template from the cards 8 and 9. The patient should find the matching the word or letter from the selection below.'),
                'fieldset_total_points': '10',
                'fieldset_total_addend_field_prefix': 'bostonaphasiasymbolworddisc-0-',
                'fieldset_total_addend_fields': ('symbol_word_card8_a_score', 'symbol_word_card8_b_score',
                                                 'symbol_word_card8_c_score', 'symbol_word_card8_d_score',
                                                 'symbol_word_card8_e_score',
                                                 'symbol_word_card9_a_score', 'symbol_word_card9_b_score',
                                                 'symbol_word_card9_c_score', 'symbol_word_card9_d_score',
                                                 'symbol_word_card9_e_score',
                                                 ),
                'fieldset_total_field': 'symbol_word_total',
            }
        }),


class BostonAphasiaWordRecognitionInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaWordRecognitionForm
    model = BostonAphasiaWordRecognition
    extra = 1
    max_num = 1

    fieldsets = (_(u'Word recognition'), {
            'fields': (
                ('word_recognition_a_score', 'word_recognition_b_score',
                 'word_recognition_c_score', 'word_recognition_d_score',
                 'word_recognition_e_score', 'word_recognition_f_score',
                 'word_recognition_g_score', 'word_recognition_h_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_18_word_recognition',
                'text': _(u'The patient should point the cards 10 and 11 the written words corresponding to those presented orally. The patient should be directed to the correct line on the card.'),
                'fieldset_total_points': '8',
                'fieldset_total_addend_field_prefix': 'bostonaphasiawordrecognition-0-',
                'fieldset_total_addend_fields': ('word_recognition_a_score', 'word_recognition_b_score',
                                                 'word_recognition_c_score', 'word_recognition_d_score',
                                                 'word_recognition_e_score', 'word_recognition_f_score',
                                                 'word_recognition_g_score', 'word_recognition_h_score',
                                                 ),
                'fieldset_total_field': 'word_recognition_total',
            }
        }),


class BostonAphasiaOralSpellingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaOralSpellingForm
    model = BostonAphasiaOralSpelling
    extra = 1
    max_num = 1

    fieldsets = (_(u'Oral spelling'), {
            'fields': (
                ('oral_spelling_a_score', 'oral_spelling_b_score',
                 'oral_spelling_c_score', 'oral_spelling_d_score',
                 'oral_spelling_e_score', 'oral_spelling_f_score',
                 'oral_spelling_g_score', 'oral_spelling_h_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_19_oral_spelling',
                'text': _(u'Spell the words for the patient and he/she must identify the word spelled.'),
                'fieldset_total_points': '8',
                'fieldset_total_addend_field_prefix': 'bostonaphasiaoralspelling-0-',
                'fieldset_total_addend_fields': ('oral_spelling_a_score', 'oral_spelling_b_score',
                                                 'oral_spelling_c_score', 'oral_spelling_d_score',
                                                 'oral_spelling_e_score', 'oral_spelling_f_score',
                                                 'oral_spelling_g_score', 'oral_spelling_h_score',
                                                 ),
                'fieldset_total_field': 'oral_spelling_total',
            }
        }),


class BostonAphasiaWordPictureMatchingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaWordPictureMatchingForm
    model = BostonAphasiaWordPictureMatching
    extra = 1
    max_num = 1

    fieldsets = (_(u'Word-picture matching'), {
            'fields': (
                ('word_picture_chair_score', 'word_picture_circle_score', 'word_picture_hammock_score',
                 'word_picture_triangle_score', 'word_picture_fifteen_score', 'word_picture_purple_score',
                 'word_picture_seven_t_o_score', 'word_picture_dripping_score', 'word_picture_brown_score',
                 'word_picture_smoking_score'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_20_word_picture_matching',
                'text': _(u'Asserted objects, color, etc. Using Cards 2 and 3, and Card 5, have patient pick out appropriate picture for each word shown him. ("Which of these pictures is this word:") Discourage patients from reading aloud.'),
                'fieldset_total_points': '10',
                'fieldset_total_addend_field_prefix': 'bostonaphasiawordpicturematching-0-',
                'fieldset_total_addend_fields': ('word_picture_chair_score', 'word_picture_circle_score',
                                                 'word_picture_hammock_score', 'word_picture_triangle_score',
                                                 'word_picture_fifteen_score', 'word_picture_purple_score',
                                                 'word_picture_seven_t_o_score', 'word_picture_dripping_score',
                                                 'word_picture_brown_score', 'word_picture_smoking_score'),
                'fieldset_total_field': 'word_picture_total',
            }
        }),


class BostonAphasiaReadingSentencesInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaReadingSentencesForm
    model = BostonAphasiaReadingSentences
    extra = 1
    max_num = 1

    fieldsets = (_(u'Reading sentences and paragraphs'), {
            'fields': (
                ('reading_sentences_dog_score', 'reading_sentences_mother_score',
                 'reading_sentences_haircut_score', 'reading_sentences_bird_score',
                 'reading_sentences_school_score', 'reading_sentences_artist_score',
                 'reading_sentences_aluminum_score', 'reading_sentences_sanitation_score',
                 'reading_sentences_civil_service_score', 'reading_sentences_government_score'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_21_reading_sentences',
                'text': _(u'Patient is presented with Cards 12, 13, 14, 15 and 16 successively. Patient indicates his selection on the card and the examiner underlines the choice in the test booklet. Assistance may be given in the two examples, but not in the test proper.'),
                'fieldset_total_points': '10',
                'fieldset_total_addend_field_prefix': 'bostonaphasiareadingsentences-0-',
                'fieldset_total_addend_fields': (
                    'reading_sentences_dog_score', 'reading_sentences_mother_score',
                    'reading_sentences_haircut_score', 'reading_sentences_bird_score',
                    'reading_sentences_school_score', 'reading_sentences_artist_score',
                    'reading_sentences_aluminum_score', 'reading_sentences_sanitation_score',
                    'reading_sentences_civil_service_score', 'reading_sentences_government_score'),
                'fieldset_total_field': 'reading_sentences_total',
                'reading_sentences_items': [form.reading_sentences_dog_items, form.reading_sentences_mother_items,
                    form.reading_sentences_haircut_items, form.reading_sentences_bird_items,
                    form.reading_sentences_school_items, form.reading_sentences_artist_items,
                    form.reading_sentences_aluminum_items, form.reading_sentences_sanitation_items,
                    form.reading_sentences_civil_service_items, form.reading_sentences_government_items,]
            }
        }),


class BostonAphasiaMechanicsWritingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaMechanicsWritingForm
    model = BostonAphasiaMechanicsWriting
    extra = 1
    max_num = 1

    fieldsets = (_(u'Mechanics of Writing'), {
            'fields': (
                ('mechanics_writing_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_22_mechanics_writing',
            }
        }),


class BostonAphasiaRecallWrittenSymbolsInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaRecallWrittenSymbolsForm
    model = BostonAphasiaRecallWrittenSymbols
    extra = 1
    max_num = 1

    fieldsets = (_(u'Recall written symbols'), {
            'fields': (
                ('serial_writing_letters_score', 'serial_writing_numbers_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_23_recall_written_symbols',
                'text': _(u'Asserted objects, color, etc. Using Cards 2 and 3, and Card 5, have patient pick out appropriate picture for each word shown him. ("Which of these pictures is this word:") Discourage patients from reading aloud.'),
                'fieldset_total_points': '8/8f',
                'fieldset_total_addend_field_prefix': 'bostonaphasiarecallwrittensymbols-0-',
                'fieldset_total_addend_fields': (
                    'serial_writing_letters_score', 'serial_writing_numbers_score',),
                'fieldset_total_field': 'serial_writing_numbers_total',

            }
        }),


class BostonAphasiaDictatedWordsInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaDictatedWordsForm
    model = BostonAphasiaDictatedWords
    extra = 1
    max_num = 1

    fieldsets = (_(u'Dictated words'), {
            'fields': (
                ('dictated_words_letters_score', 'dictated_words_numbers_score', 'dictated_words_words_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_24_dictated_words',
                'text': '',
                'fieldset_total_points': '8/8',
                'fieldset_total_addend_field_prefix': 'bostonaphasiadictatedwords-0-',
                'fieldset_total_addend_fields': (
                    'dictated_words_letters_score', 'dictated_words_numbers_score', 'dictated_words_words_score'),
                'fieldset_total_field': 'dictated_words_words_total',

            }
        }),


class BostonAphasiaCopyPangramPhraseInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaCopyPangramPhraseForm
    model = BostonAphasiaCopyPangramPhrase
    extra = 1
    max_num = 1

    fieldsets = (_(u'Copy'), {
            'fields': (
                ('copy_pangram_phrase_score',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_25_copy_pangram',
                'text': '',
                'fieldset_total_points': '5/5',
                'fieldset_total_addend_field_prefix': 'bostonaphasiacopypangramphrase-0-',
                'fieldset_total_addend_fields': (
                    'copy_pangram_phrase_score',),
                'fieldset_total_field': 'copy_pangram_total',

            }
        }),


class BostonAphasiaSpellingDictationInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaSpellingDictationForm
    model = BostonAphasiaSpellingDictation
    extra = 1
    max_num = 1

    fieldsets = (_(u'Spelling dictation'), {
            'fields': (
                ('spelling_dictation_a_score', 'spelling_dictation_a_answer',),
                ('spelling_dictation_b_score', 'spelling_dictation_b_answer',),
                ('spelling_dictation_c_score', 'spelling_dictation_c_answer',),
                ('spelling_dictation_d_score', 'spelling_dictation_d_answer',),
                ('spelling_dictation_e_score', 'spelling_dictation_e_answer',),
                ('spelling_dictation_f_score', 'spelling_dictation_f_answer',),
                ('spelling_dictation_g_score', 'spelling_dictation_g_answer',),
                ('spelling_dictation_h_score', 'spelling_dictation_h_answer',),
                ('spelling_dictation_i_score', 'spelling_dictation_i_answer',),
                ('spelling_dictation_j_score', 'spelling_dictation_j_answer',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_26_spelling_dictation',
                'text': _(u'Offer the patient the words orally and ask to write them. If a word spelling is a failure, '
                          'the patient should spell the word orally and being registered in the appropriate column. '
                          'Oral spelling does not enter the score.'),
                'fields_header': (_(u'Word'), _(u'Answer'), _(u'Oral Patient Spelling'), ),
                'fieldset_total_points': '10/10',
                'fieldset_total_addend_field_prefix': 'bostonaphasiaspellingdictation-0-',
                'fieldset_total_addend_fields': (
                    'spelling_dictation_a_score', 'spelling_dictation_b_score', 'spelling_dictation_c_score',
                    'spelling_dictation_d_score', 'spelling_dictation_e_score', 'spelling_dictation_f_score',
                    'spelling_dictation_g_score', 'spelling_dictation_h_score', 'spelling_dictation_i_score',
                    'spelling_dictation_j_score'),
                'fieldset_total_field': 'spelling_dictation_total',

            }
        }),


class BostonAphasiaWrittenPictureNamingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaWrittenPictureNamingForm
    model = BostonAphasiaWrittenPictureNaming
    extra = 1
    max_num = 1

    fieldsets = (_(u'Written picture naming'), {
            'fields': (
                'written_picture_naming_a_score', 'written_picture_naming_b_score', 'written_picture_naming_c_score',
                'written_picture_naming_d_score', 'written_picture_naming_e_score', 'written_picture_naming_f_score',
                'written_picture_naming_g_score', 'written_picture_naming_h_score', 'written_picture_naming_i_score',
                'written_picture_naming_j_score',
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_27_written_picture',
                'text': _(u'The examiner points to each picture and asks the patient to write the name of the item.'),
                'fields_header': (_(u'Picture'), _(u'Answer'),),
                'fieldset_total_points': '10/10',
                'fieldset_total_addend_field_prefix': 'bostonaphasiawrittenpicturenaming-0-',
                'fieldset_total_addend_fields': (
                    'written_picture_naming_a_score', 'written_picture_naming_b_score', 'written_picture_naming_c_score',
                    'written_picture_naming_d_score', 'written_picture_naming_e_score', 'written_picture_naming_f_score',
                    'written_picture_naming_g_score', 'written_picture_naming_h_score', 'written_picture_naming_i_score',
                    'written_picture_naming_j_score'),
                'fieldset_total_field': 'written_picture_naming_total',
            }
        }),


class BostonAphasiaNarrativeWritingInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaNarrativeWritingForm
    model = BostonAphasiaNarrativeWriting
    extra = 1
    max_num = 1

    fieldsets = (_(u'Narrative writing'), {
            'fields': (
                'narrative_writing_score',
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_28_narrative_writing',
                'text': _(u'Present the "Cookie Theft" picture on the card 1. Say: "WRITE AS MUCH AS YOU CAN '
                          'ABOUT WHAT YOU SEE GOING ON IN THIS PICTURE". Allow the patient roughly 5 minutes to write.'),
                'fieldset_total_points': '5/5',
                'fieldset_total_addend_field_prefix': 'bostonaphasianarrativewriting-0-',
                'fieldset_total_addend_fields': (
                    'narrative_writing_score',),
                'fieldset_total_field': 'narrative_writing_score_total',
            }
        }),


class BostonAphasiaSentecesWrittenDictationInlineAdmin(InlineModelAdmin):
    form = BostonAphasiaSentecesWrittenDictationForm
    model = BostonAphasiaSentecesWrittenDictation
    extra = 1
    max_num = 1

    fieldsets = (_(u'Sentences written under dictation'), {
            'fields': (
                ('sentences_written_dictation_a_score', 'sentences_written_dictation_a_exchanges', ),
                ('sentences_written_dictation_b_score', 'sentences_written_dictation_b_exchanges',),
                ('sentences_written_dictation_c_score', 'sentences_written_dictation_c_exchanges',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_29_sentences_written_dictation',
                'text': _(u'The patient must write these sentences after the dictation.'),
                'fields_header': (_(u'Sentence for dictation'), _(u'A - Score'), _(u'B - Qualification of Parametric Substitutions'),),
                'fieldset_total_points': '12/12',
                'fieldset_total_addend_field_prefix': 'bostonaphasiasenteceswrittendictation-0-',
                'fieldset_total_addend_fields': (
                    'sentences_written_dictation_a_score', 'sentences_written_dictation_b_score', 'sentences_written_dictation_c_score',),
                'fieldset_total_field': 'sentences_written_dictation_total',
            }
        }),


class BostonAphasiaAdmin(BaseAdmin):

    form = BostonAphasiaForm
    inlines = [BostonAphasiaVisualConfrontationInlineAdmin, BostonAphasiaAnimalNamingInlineAdmin,
               BostonAphasiaOralSentenceReadingInlineAdmin, BostonAphasiaSymbolWordDiscInlineAdmin,
               BostonAphasiaWordRecognitionInlineAdmin, BostonAphasiaOralSpellingInlineAdmin,
               BostonAphasiaWordPictureMatchingInlineAdmin, BostonAphasiaReadingSentencesInlineAdmin,
               BostonAphasiaMechanicsWritingInlineAdmin, BostonAphasiaRecallWrittenSymbolsInlineAdmin,
               BostonAphasiaDictatedWordsInlineAdmin, BostonAphasiaCopyPangramPhraseInlineAdmin,
               BostonAphasiaSpellingDictationInlineAdmin, BostonAphasiaWrittenPictureNamingInlineAdmin,
               BostonAphasiaNarrativeWritingInlineAdmin, BostonAphasiaSentecesWrittenDictationInlineAdmin
               ]
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Manual dominance.'), {
            'fields': (('edinburg_handedness_writing_left_hand', 'edinburg_handedness_writing_right_hand'),
                       ('edinburg_handedness_drawing_left_hand', 'edinburg_handedness_drawing_right_hand'),
                       ('edinburg_handedness_throwing_left_hand', 'edinburg_handedness_throwing_right_hand'),
                       ('edinburg_handedness_using_ashtray_left_hand', 'edinburg_handedness_using_ashtray_right_hand'),
                       ('edinburg_handedness_using_toothbrush_left_hand', 'edinburg_handedness_using_toothbrush_right_hand'),
                       ('edinburg_handedness_using_fork_left_hand', 'edinburg_handedness_using_fork_right_hand'),
                       ('edinburg_handedness_using_broom_right_hand', 'edinburg_handedness_using_broom_left_hand'),
                       ('edinburg_handedness_striking_match_left_hand', 'edinburg_handedness_striking_match_right_hand'),
                       ('edinburg_handedness_using_spoon_left_hand', 'edinburg_handedness_using_spoon_right_hand'),
                       ('edinburg_handedness_opening_box_left_hand', 'edinburg_handedness_opening_box_right_hand'),
                       'edinburg_handedness_historic_dominance'
                      ),
            'description': {
                'columns': ((0, _(u'Activity')), (1, _(u'Left hand')), (2, _(u'Right hand'))),
                'fieldset': '/bostonaphasia/fieldset_01_manual_dominance',
                'text': _(u'Are you left or right-handed? Which hand you prefer for that activity? Do you ever use the other hand for the activity?')
            }
        }),
        (_(u'Conversational and expository speech'), {
            'fields': (
                'conversational_speech_how_are_you', 'conversational_speech_been_here_before',
                'conversational_speech_help',
                'conversational_speech_leaving', 'conversational_speech_name',
                'conversational_speech_address', 'conversational_speech_free_conversation',
                'conversational_speech_cookie_jar',
                ),
            'description': {
                'fieldset': '_1col_v2',
                'text': _(u'Conduct an informal exchange, incorporating suggested questions, to elicit as many ofthe desired responses as possible. Write responses verbatim. Tape record if possible')
            }
        }),
        (_(u'Auditory Comprehension'), {
            'fields': (
                ('comprehension_card2_word_chair_answer', 'comprehension_card2_word_chair_points'),
                ('comprehension_card2_word_key_answer', 'comprehension_card2_word_key_points'),
                ('comprehension_card2_word_glove_answer', 'comprehension_card2_word_glove_points'),
                ('comprehension_card2_word_feather_answer', 'comprehension_card2_word_feather_points'),
                ('comprehension_card2_word_net_answer', 'comprehension_card2_word_net_points'),
                ('comprehension_card2_word_cactus_answer', 'comprehension_card2_word_cactus_points'),
                ('comprehension_card2_letter_l_answer', 'comprehension_card2_letter_l_points'),
                ('comprehension_card2_letter_s_answer', 'comprehension_card2_letter_s_points'),
                ('comprehension_card2_letter_g_answer', 'comprehension_card2_letter_g_points'),
                ('comprehension_card2_letter_t_answer', 'comprehension_card2_letter_t_points'),
                ('comprehension_card2_letter_h_answer', 'comprehension_card2_letter_h_points'),
                ('comprehension_card2_letter_r_answer', 'comprehension_card2_letter_r_points'),
                ('comprehension_card2_shape_circle_answer', 'comprehension_card2_shape_circle_points'),
                ('comprehension_card2_shape_spiral_answer', 'comprehension_card2_shape_spiral_points'),
                ('comprehension_card2_shape_square_answer', 'comprehension_card2_shape_square_points'),
                ('comprehension_card2_shape_triangle_answer', 'comprehension_card2_shape_triangle_points'),
                ('comprehension_card2_shape_cone_answer', 'comprehension_card2_shape_cone_points'),
                ('comprehension_card2_shape_star_answer', 'comprehension_card2_shape_star_points'),
                ('comprehension_card3_act_drinking_answer', 'comprehension_card3_act_drinking_points'),
                ('comprehension_card3_act_smoking_answer', 'comprehension_card3_act_smoking_points'),
                ('comprehension_card3_act_running_answer', 'comprehension_card3_act_running_points'),
                ('comprehension_card3_act_falling_answer', 'comprehension_card3_act_falling_points'),
                ('comprehension_card3_act_sleeping_answer', 'comprehension_card3_act_sleeping_points'),
                ('comprehension_card3_act_dropping_answer', 'comprehension_card3_act_dropping_points'),
                ('comprehension_card3_color_blue_answer', 'comprehension_card3_color_blue_points'),
                ('comprehension_card3_color_red_answer', 'comprehension_card3_color_red_points'),
                ('comprehension_card3_color_gray_answer', 'comprehension_card3_color_gray_points'),
                ('comprehension_card3_color_brown_answer', 'comprehension_card3_color_brown_points'),
                ('comprehension_card3_color_pink_answer', 'comprehension_card3_color_pink_points'),
                ('comprehension_card3_color_purple_answer', 'comprehension_card3_color_purple_points'),
                ('comprehension_card3_number_7_answer', 'comprehension_card3_number_7_points'),
                ('comprehension_card3_number_42_answer', 'comprehension_card3_number_42_points'),
                ('comprehension_card3_number_700_answer', 'comprehension_card3_number_700_points'),
                ('comprehension_card3_number_1936_answer', 'comprehension_card3_number_1936_points'),
                ('comprehension_card3_number_15_answer', 'comprehension_card3_number_15_points'),
                ('comprehension_card3_number_7000_answer', 'comprehension_card3_number_7000_points'),
            ),
            'description': {
                'columns': ((0, _(u'Activity')), (1, _(u'Left hand')), (2, _(u'Right hand'))),
                'fieldset': '/bostonaphasia/fieldset_02_comprehension',
                'text': _(u"Show the cards 2 and 3 separately."
                          u"The patient must look all the pictures from the card before the start."
                          u"Instruct the patient to point to the picture or symbol, saying \"Show me the...\""
                          u"Change randomly from one category to another"
                          u"It is allowed one repetition, if asked."
                          u"Show the correct category if the patient can\'t find it and repeat the item name to be identified."
                          u"Score 2 points if the response is correct within 5 seconds, otherwise, 1 point"
                          u"Correct category but inaccurate item score 1/2 point."),
                'fieldset_total_points': '30',
                'fieldset_total_addend_fields': ('orientation_day_week', 'orientation_day_month', 'orientation_month', 'orientation_year',
                                                 'orientation_time', 'orientation_place', 'orientation_institution', 'orientation_district',
                                                 'orientation_city', 'orientation_state', 'registration_words', 'attention_calc',
                                                 'recall_words', 'language_watch_pen', 'language_repeat', 'language_command',
                                                 'language_read', 'language_write', 'language_copy'),
                'fieldset_total_field': 'mmse_total',
            }
        }),
        (_(u'Body parts identification'), {
            'fields': (
                    ('body_part_a_ear_points', 'body_part_a_ear_answer'),
                    ('body_part_a_nose_points', 'body_part_a_nose_answer'),
                    ('body_part_a_shoulder_points', 'body_part_a_shoulder_answer'),
                    ('body_part_a_knee_points', 'body_part_a_knee_answer'),
                    ('body_part_a_eyelid_points', 'body_part_a_eyelid_answer'),
                    ('body_part_a_ankle_points', 'body_part_a_ankle_answer'),
                    ('body_part_a_chest_points', 'body_part_a_chest_answer'),
                    ('body_part_a_neck_points', 'body_part_a_neck_answer'),
                    ('body_part_a_middle_finger_points', 'body_part_a_middle_finger_answer'),
                    ('body_part_b_wrist_points', 'body_part_b_wrist_answer'),
                    ('body_part_b_thumb_points', 'body_part_b_thumb_answer'),
                    ('body_part_b_thigh_points', 'body_part_b_thigh_answer'),
                    ('body_part_b_chin_points', 'body_part_b_chin_answer'),
                    ('body_part_b_elbow_points', 'body_part_b_elbow_answer'),
                    ('body_part_b_lips_points', 'body_part_b_lips_answer'),
                    ('body_part_b_eyebrow_points', 'body_part_b_eyebrow_answer'),
                    ('body_part_b_cheek_points', 'body_part_b_cheek_answer'),
                    ('body_part_b_forefinger_points', 'body_part_b_forefinger_answer'),
                    ('body_part_c_right_ear_points', 'body_part_c_right_ear_answer'),
                    ('body_part_c_left_shoulder_points', 'body_part_c_left_shoulder_answer'),
                    ('body_part_c_left_knee_points', 'body_part_c_left_knee_answer'),
                    ('body_part_c_right_ankle_points', 'body_part_c_right_ankle_answer'),
                    ('body_part_c_right_wrist_points', 'body_part_c_right_wrist_answer'),
                    ('body_part_c_left_thumb_points', 'body_part_c_left_thumb_answer'),
                    ('body_part_c_right_elbow_points', 'body_part_c_right_elbow_answer'),
                    ('body_part_c_left_cheek_points', 'body_part_c_left_cheek_answer'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_03_body_parts',
                'text': _(u'The patient is asked to point on his/her body to the part named. Enter erroneous responses.'

                          u'Score: The items in the first two columns A and B have the scores 1 point if recognized immediately (within 5 seconds), and 1/2 point is correctly identified (after 5 seconds). The third column C is right-left discrimination and receives a total of 2 points if all 8 items are correct (the body part may be incorrect since there is no failure in the right-left discrimination), 1 point is 6 or 7 items are correct, otherwise zero.'),
                'fieldset_a_b_total_points': 18,
                'fieldset_a_b_total_addend_fields': (
                    'body_part_a_ear_points', 'body_part_a_nose_points', 'body_part_a_shoulder_points', 'body_part_a_knee_points',
                    'body_part_a_eyelid_points', 'body_part_a_ankle_points', 'body_part_a_chest_points', 'body_part_a_neck_points',
                    'body_part_a_middle_finger_points',
                    'body_part_b_wrist_points', 'body_part_b_thumb_points', 'body_part_b_thigh_points', 'body_part_b_chin_points',
                    'body_part_b_elbow_points', 'body_part_b_lips_points', 'body_part_b_eyebrow_points', 'body_part_b_cheek_points',
                    'body_part_b_forefinger_points',),
                'fieldset_a_b_total_field': 'body_part_a_b_total_points',
                'fieldset_c_total_points': 2,
                'fieldset_c_total_addend_fields': (
                    'body_part_c_right_ear_points', 'body_part_c_left_shoulder_points', 'body_part_c_left_knee_points',
                    'body_part_c_right_ankle_points', 'body_part_c_right_wrist_points', 'body_part_c_left_thumb_points',
                    'body_part_c_right_elbow_points', 'body_part_c_left_cheek_points',),
                'fieldset_c_total_field': 'body_part_c_total_points',
                'fieldset_a_b_c_total_points': 20,
                'fieldset_a_b_c_total_addend_fields': (
                    'body_part_a_b_total_points', 'body_part_c_total_points',),
                'fieldset_a_b_c_total_field': 'body_part_a_b_c_total_points',
            }
        }),
        (_(u'Commands'), {
            'fields': (
                ('command_close_fist', 'command_point_ceiling',),
                ('command_put_pencil', 'command_put_watch', 'command_touch_shoulder')
                ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_04_commands',
                'text': _(u'Have the patient carry out the following commands, giving one point of credit for each underlined element '
                          u'that he or she carries out. One repetition is permitted on request, '
                          u'but the whole command must be repeated.'),
                'fieldset_total_points': '15',
                'fieldset_total_addend_fields': ('command_close_fist', 'command_point_ceiling',
                                                 'command_put_pencil', 'command_put_watch', 'command_touch_shoulder'),
                'fieldset_total_field': 'command_total',
            }
        }),
        (_(u'Complex ideational material'), {
            'fields': (
                ('complex_ideational_1a', 'complex_ideational_1b', 'form_complex_ideational_1a_1b',),
                ('complex_ideational_2a', 'complex_ideational_2b', 'form_complex_ideational_2a_2b',),
                ('complex_ideational_3a', 'complex_ideational_3b', 'form_complex_ideational_3a_3b',),
                ('complex_ideational_4a', 'complex_ideational_4b', 'form_complex_ideational_4a_4b',),
                ('complex_ideational_5a', 'complex_ideational_5b', 'form_complex_ideational_5a_5b',),
                ('complex_ideational_6a', 'complex_ideational_6b', 'form_complex_ideational_6a_6b',),
                ('complex_ideational_7a', 'complex_ideational_7b', 'form_complex_ideational_7a_7b',),
                ('complex_ideational_8a', 'complex_ideational_8b', 'form_complex_ideational_8a_8b',),
                ('complex_ideational_9a', 'complex_ideational_9b', 'form_complex_ideational_9a_9b',),
                ('complex_ideational_10a', 'complex_ideational_10b', 'form_complex_ideational_10a_10b',),
                ('complex_ideational_11a', 'complex_ideational_11b', 'form_complex_ideational_11a_11b',),
                ('complex_ideational_12a', 'complex_ideational_12b', 'form_complex_ideational_12a_12b',),
                ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_05_complex_ideational',
                'text': _(u'Both the A and B questions must be correct to gain 1 point of credit for each numbered pair. '
                          u'One repetition is permitted. First read all the question from column A and then questions from column B.'),
                'fieldset_total_points': '12',
                'fieldset_total_addend_fields': ('form_complex_ideational_1a_1b', 'form_complex_ideational_2a_2b',
                                                 'form_complex_ideational_3a_3b', 'form_complex_ideational_4a_4b',
                                                 'form_complex_ideational_5a_5b', 'form_complex_ideational_6a_6b',
                                                 'form_complex_ideational_7a_7b', 'form_complex_ideational_8a_8b',
                                                 'form_complex_ideational_9a_9b', 'form_complex_ideational_10a_10b',
                                                 'form_complex_ideational_11a_11b', 'form_complex_ideational_12a_12b',),
                'fieldset_total_field': 'complex_ideational_total',
            }
        }),
        (_(u'Oral agility'), {
            'fields': (
                ('oral_agility_lips_purse', 'oral_agility_mouth_open', 'oral_agility_lips_retract',
                 'oral_agility_tongue_corner', 'oral_agility_tongue_protude', 'oral_agility_tongue_teeth'),
                ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_06_oral_agility',
                'text': _(u'If patient cannot get started on one or two items at the most, either because of perseveration '
                          u'or paraphasic substitution, eliminate items and prorate score. '
                          u'If more than two items are unscoreable, do not enter total score.'),
                'fieldset_total_points': '12',
                'fieldset_total_addend_fields': ('oral_agility_lips_purse', 'oral_agility_mouth_open', 'oral_agility_lips_retract',
                                                 'oral_agility_tongue_corner', 'oral_agility_tongue_protude', 'oral_agility_tongue_teeth'),
                'fieldset_total_field': 'oral_agility_non_verbal_total',
            }
        }),
        (_(u'Oral agility'), {
            'fields': (
                ('verbal_agility_a', 'verbal_agility_b', 'verbal_agility_c', 'verbal_agility_d',
                 'verbal_agility_e', 'verbal_agility_f', 'verbal_agility_g'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_07_oral_agility',
                'fieldset_total_points': '14',
                'fieldset_total_addend_fields': ('verbal_agility_a', 'verbal_agility_b', 'verbal_agility_c', 'verbal_agility_d',
                                                 'verbal_agility_e', 'verbal_agility_f', 'verbal_agility_g'),
                'fieldset_total_field': 'oral_agility_verbal_total',
            }
        }),
        (_(u'Automatized sequences'), {
            'fields': (
                ('automzatized_days_week', 'automzatized_days_week_note'),
                ('automzatized_months_year', 'automzatized_months_year_note'),
                ('automzatized_counting_21', 'automzatized_counting_21_note'),
                ('automzatized_alphabet', 'automzatized_alphabet_note'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_08_automatized',
                'text': _(u'Have patient recite each of the following four series, giving him assistance with the first word, if necessary.'
                          u'<br>Provide further assistance as needed, but discontinue a series when patient fails with four successive words.'
                          u'<br>Record assistance given by circling the word; cross out words omitted by patient.'
                          u'<br>Allow 0, 1 or 2 points, as indicated.'),
                'fieldset_total_points': '8',
                'fieldset_total_addend_fields': ('automzatized_days_week', 'automzatized_months_year', 'automzatized_counting_21', 'automzatized_alphabet'),
                'fieldset_total_field': 'automatized_total',
            }
        }),
        (_(u'Recitation, Singing'), {
            'fields': (
                ('reciting_note', 'reciting_score'),
                ('singing_note', 'singing_score'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_09_recitation',
                'text': _(u'Instruct patient to complete the line for the following rhymes. Words in parentheses may be given as additional cues, if necessary.'
                          u'Use a natural or slightly exaggerated inflection to encourage completion of the rhyme.'
                          u'If patient fails, or is not familiar with the material, attempt other memorized or automatized matter, '
                          u'such as the Lord\'s Prayer, the Pledge of Allegiance, etc.'
                          u'Circle qualitative ratings below.'),
                'fieldset_total_points': '4',
                'fieldset_total_addend_fields': ('reciting_score', 'singing_score'),
                'fieldset_total_field': 'reciting_singing_total',
            }
        }),
        (_(u'Repetition of words'), {
            'fields': (
                ('repetition_words_what_score', 'repetition_words_what_transcription', 'repetition_words_what_articulation', 'repetition_words_what_paraphasia',),
                ('repetition_words_chair_score', 'repetition_words_chair_transcription', 'repetition_words_chair_articulation', 'repetition_words_chair_paraphasia',),
                ('repetition_words_hammock_score', 'repetition_words_hammock_transcription', 'repetition_words_hammock_articulation', 'repetition_words_hammock_paraphasia',),
                ('repetition_words_purple_score', 'repetition_words_purple_transcription', 'repetition_words_purple_articulation', 'repetition_words_purple_paraphasia',),
                ('repetition_words_brown_score', 'repetition_words_brown_transcription', 'repetition_words_brown_articulation', 'repetition_words_brown_paraphasia',),
                ('repetition_words_w_score', 'repetition_words_w_transcription', 'repetition_words_w_articulation', 'repetition_words_w_paraphasia',),
                ('repetition_words_fifteen_score', 'repetition_words_fifteen_transcription', 'repetition_words_fifteen_articulation', 'repetition_words_fifteen_paraphasia',),
                ('repetition_words_1776_score', 'repetition_words_1776_transcription', 'repetition_words_1776_articulation', 'repetition_words_1776_paraphasia',),
                ('repetition_words_emphasize_score', 'repetition_words_emphasize_transcription', 'repetition_words_emphasize_articulation', 'repetition_words_emphasize_paraphasia',),
                ('repetition_words_episcopal_score', 'repetition_words_episcopal_transcription', 'repetition_words_episcopal_articulation', 'repetition_words_episcopal_paraphasia',),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_10_repetition',
                'text': _(u'Have patient repeat each of the following words. One repetition by examiner is permitted when it appears that this may help, or when it is requested. '
                          u'For credit, all syllables must be in their proper order, although distortion of individual sound elements is permitted, '
                          u'provided it is in keeping with patient\'s general articulation difficulty and that the word is recognizable.'),
                'fieldset_total_points': '10',
                'fieldset_total_addend_fields': ('repetition_words_what_score', 'repetition_words_chair_score', 'repetition_words_hammock_score',
                                                 'repetition_words_purple_score', 'repetition_words_brown_score', 'repetition_words_w_score',
                                                 'repetition_words_fifteen_score', 'repetition_words_1776_score', 'repetition_words_emphasize_score',
                                                 'repetition_words_episcopal_score', ),
                'fieldset_total_field': 'repetition_words_total',
            }
        }),
        (_(u'Repeating phrases'), {
            'fields': (
                ('repetition_phrases_high_a_score', 'repetition_phrases_high_a_articulation', 'repetition_phrases_high_a_paraphasia'),
                ('repetition_phrases_high_b_score', 'repetition_phrases_high_b_articulation', 'repetition_phrases_high_b_paraphasia'),
                ('repetition_phrases_high_c_score', 'repetition_phrases_high_c_articulation', 'repetition_phrases_high_c_paraphasia'),
                ('repetition_phrases_high_d_score', 'repetition_phrases_high_d_articulation', 'repetition_phrases_high_d_paraphasia'),
                ('repetition_phrases_high_e_score', 'repetition_phrases_high_e_articulation', 'repetition_phrases_high_e_paraphasia'),
                ('repetition_phrases_high_f_score', 'repetition_phrases_high_f_articulation', 'repetition_phrases_high_f_paraphasia'),
                ('repetition_phrases_high_g_score', 'repetition_phrases_high_g_articulation', 'repetition_phrases_high_g_paraphasia'),
                ('repetition_phrases_high_h_score', 'repetition_phrases_high_h_articulation', 'repetition_phrases_high_h_paraphasia'),
                ('repetition_phrases_low_a_score', 'repetition_phrases_low_a_articulation', 'repetition_phrases_low_a_paraphasia'),
                ('repetition_phrases_low_b_score', 'repetition_phrases_low_b_articulation', 'repetition_phrases_low_b_paraphasia'),
                ('repetition_phrases_low_c_score', 'repetition_phrases_low_c_articulation', 'repetition_phrases_low_c_paraphasia'),
                ('repetition_phrases_low_d_score', 'repetition_phrases_low_d_articulation', 'repetition_phrases_low_d_paraphasia'),
                ('repetition_phrases_low_e_score', 'repetition_phrases_low_e_articulation', 'repetition_phrases_low_e_paraphasia'),
                ('repetition_phrases_low_f_score', 'repetition_phrases_low_f_articulation', 'repetition_phrases_low_f_paraphasia'),
                ('repetition_phrases_low_g_score', 'repetition_phrases_low_g_articulation', 'repetition_phrases_low_g_paraphasia'),
                ('repetition_phrases_low_h_score', 'repetition_phrases_low_h_articulation', 'repetition_phrases_low_h_paraphasia'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_11_repetition',
                'text': '',
                'fieldset_total_points': ('8', '8', '16',),
                'fieldset_total_addend_fields': (
                    ('repetition_phrases_high_a_score', 'repetition_phrases_high_b_score', 'repetition_phrases_high_c_score',
                     'repetition_phrases_high_d_score', 'repetition_phrases_high_e_score', 'repetition_phrases_high_f_score',
                     'repetition_phrases_high_g_score', 'repetition_phrases_high_h_score', ),
                    ('repetition_phrases_low_a_score',  'repetition_phrases_low_b_score', 'repetition_phrases_low_c_score',
                     'repetition_phrases_low_d_score', 'repetition_phrases_low_e_score', 'repetition_phrases_low_f_score',
                     'repetition_phrases_low_g_score', 'repetition_phrases_low_h_score', ),
                    ('repetition_phrases_high_total', 'repetition_phrases_high_total', )
                ),
                'fieldset_total_field': ('repetition_phrases_high_total', 'repetition_phrases_high_total', 'repetition_phrases_high_low_total'),
            }
        }),
        (_(u'Word reading'), {
            'fields': (
                ('word_reading_chair_score', 'word_reading_chair_articulation', 'word_reading_chair_paraphasia'),
                ('word_reading_circle_score', 'word_reading_circle_articulation', 'word_reading_circle_paraphasia'),
                ('word_reading_hammock_score', 'word_reading_hammock_articulation', 'word_reading_hammock_paraphasia'),
                ('word_reading_triangle_score', 'word_reading_triangle_articulation', 'word_reading_triangle_paraphasia'),
                ('word_reading_fifteen_score', 'word_reading_fifteen_articulation', 'word_reading_fifteen_paraphasia'),
                ('word_reading_purple_score', 'word_reading_purple_articulation', 'word_reading_purple_paraphasia'),
                ('word_reading_seven_score', 'word_reading_seven_articulation', 'word_reading_seven_paraphasia'),
                ('word_reading_dripping_score', 'word_reading_dripping_articulation', 'word_reading_dripping_paraphasia'),
                ('word_reading_brown_score', 'word_reading_brown_articulation', 'word_reading_brown_paraphasia'),
                ('word_reading_smoking_score', 'word_reading_smoking_articulation', 'word_reading_smoking_paraphasia'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_12_reading',
                'text': _(u'Have the patient read the words, one at a time, from test Card 5. '
                          u'Check approximate lag between your pointing to the word and the patient\'s adequate response. '
                          u'Assist as required, but give no credit for responses obtained with help.'),
                'fieldset_total_points': '30',
                'fieldset_total_addend_fields': ('word_reading_chair_score', 'word_reading_circle_score', 'word_reading_hammock_score',
                                                 'word_reading_triangle_score', 'word_reading_fifteen_score', 'word_reading_purple_score',
                                                 'word_reading_seven_score', 'word_reading_dripping_score', 'word_reading_brown_score',
                                                 'word_reading_smoking_score'),
                'fieldset_total_field': 'word_reading_total',
            }
        }),
        (_(u'Responsive naming'), {
            'fields': (
                ('responsive_naming_time_score', 'responsive_naming_time_articulation', 'responsive_naming_time_paraphasia'),
                ('responsive_naming_razor_score', 'responsive_naming_razor_articulation', 'responsive_naming_razor_paraphasia'),
                ('responsive_naming_soap_score', 'responsive_naming_soap_articulation', 'responsive_naming_soap_paraphasia'),
                ('responsive_naming_pencil_score', 'responsive_naming_pencil_articulation', 'responsive_naming_pencil_paraphasia'),
                ('responsive_naming_paper_score', 'responsive_naming_paper_articulation', 'responsive_naming_paper_paraphasia'),
                ('responsive_naming_grass_score', 'responsive_naming_grass_articulation', 'responsive_naming_grass_paraphasia'),
                ('responsive_naming_cigarette_score', 'responsive_naming_cigarette_articulation', 'responsive_naming_cigarette_paraphasia'),
                ('responsive_naming_dozen_score', 'responsive_naming_dozen_articulation', 'responsive_naming_dozen_paraphasia'),
                ('responsive_naming_coal_score', 'responsive_naming_coal_articulation', 'responsive_naming_coal_paraphasia'),
                ('responsive_naming_medicine_score', 'responsive_naming_medicine_articulation', 'responsive_naming_medicine_paraphasia'),
            ),
            'description': {
                'fieldset': '/bostonaphasia/fieldset_13_responsive',
                'text': _(u'Have patient supply the one-word responses required by the stimulus questions. Check approximate lag.'),
                'fieldset_total_points': '27',
                'fieldset_total_addend_fields': ('responsive_naming_time_score', 'responsive_naming_razor_score', 'responsive_naming_soap_score',
                                                 'responsive_naming_pencil_score', 'responsive_naming_paper_score', 'responsive_naming_grass_score',
                                                 'responsive_naming_cigarette_score', 'responsive_naming_dozen_score', 'responsive_naming_coal_score',
                                                 'responsive_naming_medicine_score'),
                'fieldset_total_field': 'responsive_naming_total',
            }
        }),

    )





admin.site.register(BostonAphasia, BostonAphasiaAdmin)
# Registrando no reversion-compare
patch_admin(BostonAphasia)



