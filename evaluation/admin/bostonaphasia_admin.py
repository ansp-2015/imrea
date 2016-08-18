from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from ..models.bostonaphasia import BostonAphasia
from .base_admin import BaseAdmin
from ..forms.bostonaphasia_form import BostonAphasiaForm


class BostonAphasiaAdmin(BaseAdmin):

    form = BostonAphasiaForm
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
                'fieldset': '/bostonaphasia/fieldset_10_repetition',
                'text': _(u''),
                'fieldset_total_points': ('8', '16',),
                'fieldset_total_addend_fields': (
                    ('repetition_phrases_high_a_score', 'repetition_phrases_high_b_score', 'repetition_phrases_high_c_score',
                     'repetition_phrases_high_d_score', 'repetition_phrases_high_e_score', 'repetition_phrases_high_f_score',
                     'repetition_phrases_high_g_score', 'repetition_phrases_high_h_score', ),
                    ('repetition_phrases_low_a_score',  'repetition_phrases_low_b_score', 'repetition_phrases_low_c_score',
                     'repetition_phrases_low_d_score', 'repetition_phrases_low_e_score', 'repetition_phrases_low_f_score',
                     'repetition_phrases_low_g_score', 'repetition_phrases_low_h_score', )
                ),
                'fieldset_total_field': ('repetition_phrases_high_total', 'repetition_phrases_low_total'),
            }
        }),
    )

admin.site.register(BostonAphasia, BostonAphasiaAdmin)
# Registrando no reversion-compare
patch_admin(BostonAphasia)
