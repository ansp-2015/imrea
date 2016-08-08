from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from evaluation.models.bostonaphasia import BostonAphasia
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
                'fieldset': '/bostonaphasia/fieldset_01_table',
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
                'fieldset': '/bostonaphasia/fieldset_02_table',
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
                'fieldset': '/bostonaphasia/fieldset_03_table',
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
                'fieldset': '/bostonaphasia/fieldset_04_table',
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
                'fieldset': '/bostonaphasia/fieldset_05_table',
                'text': _(u'Both the A and B questions must be correct to gain 1 point of credit for each numbered pair. '
                          u'One repetition is permitted. First read all the question from column A and then questions from column B.'),
            }
        }),
    )

admin.site.register(BostonAphasia, BostonAphasiaAdmin)
# Registrando no reversion-compare
patch_admin(BostonAphasia)
