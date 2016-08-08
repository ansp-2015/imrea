# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation


class BostonAphasia(BaseEvaluation):
    edinburg_handedness_writing_left_hand = models.IntegerField(_(u'Write or distribute a card deck'), blank=True, null=True)
    edinburg_handedness_writing_right_hand = models.IntegerField(_(u'Write or distribute a card deck'), blank=True, null=True)

    edinburg_handedness_drawing_left_hand = models.IntegerField(_(u'Draw or fill a glass of water'), blank=True, null=True)
    edinburg_handedness_drawing_right_hand = models.IntegerField(_(u'Draw or fill a glass of water'), blank=True, null=True)

    edinburg_handedness_throwing_left_hand = models.IntegerField(_(u'Throw a ball'), blank=True, null=True)
    edinburg_handedness_throwing_right_hand = models.IntegerField(_(u'Throw a ball'), blank=True, null=True)

    edinburg_handedness_using_ashtray_left_hand = models.IntegerField(_(u'Use an ashtray'), blank=True, null=True)
    edinburg_handedness_using_ashtray_right_hand = models.IntegerField(_(u'Use an ashtray'), blank=True, null=True)

    edinburg_handedness_using_toothbrush_left_hand = models.IntegerField(_(u'Use a toothbrush'), blank=True, null=True)
    edinburg_handedness_using_toothbrush_right_hand = models.IntegerField(_(u'Use a toothbrush'), blank=True, null=True)

    edinburg_handedness_using_fork_left_hand = models.IntegerField(_(u'Eat with a fork'), blank=True, null=True)
    edinburg_handedness_using_fork_right_hand = models.IntegerField(_(u'Eat with a fork'), blank=True, null=True)

    edinburg_handedness_using_broom_right_hand = models.IntegerField(_(u'Use a broom (upper hand)'), blank=True, null=True)
    edinburg_handedness_using_broom_left_hand = models.IntegerField(_(u'Use a broom (upper hand)'), blank=True, null=True)

    edinburg_handedness_striking_match_left_hand = models.IntegerField(_(u'Strike a match'), blank=True, null=True)
    edinburg_handedness_striking_match_right_hand = models.IntegerField(_(u'Strike a match'), blank=True, null=True)

    edinburg_handedness_using_spoon_left_hand = models.IntegerField(_(u'Use a spoon'), blank=True, null=True)
    edinburg_handedness_using_spoon_right_hand = models.IntegerField(_(u'Use a spoon'), blank=True, null=True)

    edinburg_handedness_opening_box_left_hand = models.IntegerField(_(u'Open a box (holding the lid)'), blank=True, null=True)
    edinburg_handedness_opening_box_right_hand = models.IntegerField(_(u'Open a box (holding the lid)'), blank=True, null=True)

    edinburg_handedness_historic_dominance = models.IntegerField(_(u'History of handedness (including data from other family members, eg: mother, father , brother, offspring)'),
                                                                 blank=True, null=True,
                                                                 help_text=_(u'1: included / 2: absent'))
    # CONVERSATIONAL SPEECH
    conversational_speech_how_are_you = models.TextField(verbose_name=_(u'a. "HOW ARE YOU TODAY?" ("Okay," "Fine," or other appropriate response)'), max_length=500, blank=True, null=True)
    conversational_speech_been_here_before = models.TextField(verbose_name=_(u'b. "HAVE YOU EVER BEEN HERE BEFORE? or "HAVE I EVER TESTED YOU BEFORE?" ("Yes", "No" or other relevant response)'),
                                                              max_length=500, blank=True, null=True)
    conversational_speech_help = models.TextField(verbose_name=_(u'c. "DO YOU THINK WE CAN HELP (HAVE HELPED YOU)?"( "I think so", "Maybe" or equivalent.)'), max_length=500, blank=True, null=True)
    conversational_speech_leaving = models.TextField(verbose_name=_(u'd. "WHEN ARE YOU GOING TO BE LEAVING HERE?("I don\'t know", "Pretty soon", etc.)'), max_length=500, blank=True, null=True)
    conversational_speech_leaving_thought = models.TextField(verbose_name=_(u'e. "WE HOPE TO BE PRETTY SOON. WHAT DO YOU THINK?("I hope so", etc.)'),
                                                             max_length=500, blank=True, null=True)
    conversational_speech_name = models.TextField(verbose_name=_(u'f. "WHAT IS YOUR FULL NAME?"'), max_length=500, blank=True, null=True)
    conversational_speech_address = models.TextField(verbose_name=_(u'g. "WHAT lS YOUR FULL ADDRESS?" (Number street, and city required. Probe for omitted elements).'),
                                                     max_length=500, blank=True, null=True)
    conversational_speech_free_conversation = models.TextField(verbose_name=_(u'h. Free conversation'),
                                                               help_text=_(u'In order to elicit as much conversation as possible, it is suggested that the examiner start with a familiar topic, such as "WHAT KIND OF WORK WERE YOU DOING BEFORE YOU BECAME ILL?" or "TELL ME WHAT HAPPENED TO BRING YOU HERE." Encourage at least three minutes of conversation, if possible. Avoid questions that would elicit "Yes" or "No" responses.lf tape recording is not used,w rite verbatim as much as possible'),
                                                               max_length=500, blank=True, null=True)
    conversational_speech_cookie_jar = models.TextField(verbose_name=_(u'i. Picture description'),
                                                        help_text=_(u'Present the "Cookie Theft" picture on card l. say, "Tell me '
                                                                    u'everything you see going on in this picture." Point to neglected features of the picture and ask for '
                                                                    u'elaboration if the patient´s response is skimpier than his/her apparent potential.'),
                                                        max_length=500, blank=True, null=True)

    # AUDITORY COMPREHENSION
    # Word Comprehension
    # 1. Basic word discrimination
    comprehension_card2_word_chair_answer = models.CharField(verbose_name=_(u'Chair'), max_length=200, blank=True, null=True)
    comprehension_card2_word_chair_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_word_key_answer = models.CharField(verbose_name=_(u'Key'), max_length=200, blank=True, null=True)
    comprehension_card2_word_key_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_word_glove_answer = models.CharField(verbose_name=_(u'Glove'), max_length=200, blank=True, null=True)
    comprehension_card2_word_glove_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_word_feather_answer = models.CharField(verbose_name=_(u'Feather'), max_length=200, blank=True, null=True)
    comprehension_card2_word_feather_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_word_net_answer = models.CharField(verbose_name=_(u'Net'), max_length=200, blank=True, null=True)
    comprehension_card2_word_net_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_word_cactus_answer = models.CharField(verbose_name=_(u'Cactus'), max_length=200, blank=True, null=True)
    comprehension_card2_word_cactus_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_letter_l_answer = models.CharField(verbose_name=u'L', max_length=200, blank=True, null=True)
    comprehension_card2_letter_l_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_letter_s_answer = models.CharField(verbose_name=u'S', max_length=200, blank=True, null=True)
    comprehension_card2_letter_s_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_letter_g_answer = models.CharField(verbose_name=u'G', max_length=200, blank=True, null=True)
    comprehension_card2_letter_g_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_letter_t_answer = models.CharField(verbose_name=u'T', max_length=200, blank=True, null=True)
    comprehension_card2_letter_t_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_letter_h_answer = models.CharField(verbose_name=u'H', max_length=200, blank=True, null=True)
    comprehension_card2_letter_h_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_letter_r_answer = models.CharField(verbose_name=u'R', max_length=200, blank=True, null=True)
    comprehension_card2_letter_r_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_shape_circle_answer = models.CharField(verbose_name=_(u'Circle'), max_length=200, blank=True, null=True)
    comprehension_card2_shape_circle_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_shape_spiral_answer = models.CharField(verbose_name=_(u'Spiral'), max_length=200, blank=True, null=True)
    comprehension_card2_shape_spiral_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_shape_square_answer = models.CharField(verbose_name=_(u'Square'), max_length=200, blank=True, null=True)
    comprehension_card2_shape_square_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_shape_triangle_answer = models.CharField(verbose_name=_(u'Triangle'), max_length=200, blank=True, null=True)
    comprehension_card2_shape_triangle_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_shape_cone_answer = models.CharField(verbose_name=_(u'Cone'), max_length=200, blank=True, null=True)
    comprehension_card2_shape_cone_points = models.IntegerField(blank=True, null=True)

    comprehension_card2_shape_star_answer = models.CharField(verbose_name=_(u'Star'), max_length=200, blank=True, null=True)
    comprehension_card2_shape_star_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_act_drinking_answer = models.CharField(verbose_name=_(u'Drinking'), max_length=200, blank=True, null=True)
    comprehension_card3_act_drinking_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_act_smoking_answer = models.CharField(verbose_name=_(u'Smoking'), max_length=200, blank=True, null=True)
    comprehension_card3_act_smoking_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_act_running_answer = models.CharField(verbose_name=_(u'Running'), max_length=200, blank=True, null=True)
    comprehension_card3_act_running_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_act_falling_answer = models.CharField(verbose_name=_(u'Falling'), max_length=200, blank=True, null=True)
    comprehension_card3_act_falling_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_act_sleeping_answer = models.CharField(verbose_name=_(u'Sleeping'), max_length=200, blank=True, null=True)
    comprehension_card3_act_sleeping_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_act_dropping_answer = models.CharField(verbose_name=_(u'Dropping'), max_length=200, blank=True, null=True)
    comprehension_card3_act_dropping_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_color_blue_answer = models.CharField(verbose_name=_(u'Blue'), max_length=200, blank=True, null=True)
    comprehension_card3_color_blue_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_color_red_answer = models.CharField(verbose_name=_(u'Red'), max_length=200, blank=True, null=True)
    comprehension_card3_color_red_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_color_gray_answer = models.CharField(verbose_name=_(u'Gray'), max_length=200, blank=True, null=True)
    comprehension_card3_color_gray_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_color_brown_answer = models.CharField(verbose_name=_(u'Brown'), max_length=200, blank=True, null=True)
    comprehension_card3_color_brown_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_color_pink_answer = models.CharField(verbose_name=_(u'Pink'), max_length=200, blank=True, null=True)
    comprehension_card3_color_pink_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_color_purple_answer = models.CharField(verbose_name=_(u'Purple'), max_length=200, blank=True, null=True)
    comprehension_card3_color_purple_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_number_7_answer = models.CharField(verbose_name=u'7', max_length=200, blank=True, null=True)
    comprehension_card3_number_7_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_number_42_answer = models.CharField(verbose_name=u'42', max_length=200, blank=True, null=True)
    comprehension_card3_number_42_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_number_700_answer = models.CharField(verbose_name=u'700', max_length=200, blank=True, null=True)
    comprehension_card3_number_700_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_number_1936_answer = models.CharField(verbose_name=u'1936', max_length=200, blank=True, null=True)
    comprehension_card3_number_1936_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_number_15_answer = models.CharField(verbose_name=u'15', max_length=200, blank=True, null=True)
    comprehension_card3_number_15_points = models.IntegerField(blank=True, null=True)

    comprehension_card3_number_7000_answer = models.CharField(verbose_name=u'7000', max_length=200, blank=True, null=True)
    comprehension_card3_number_7000_points = models.IntegerField(blank=True, null=True)

    # Body parts
    body_part_a_ear_answer = models.CharField(verbose_name=u'Ear', max_length=200, blank=True, null=True)
    body_part_a_ear_points = models.IntegerField(blank=True, null=True)

    body_part_a_nose_answer = models.CharField(verbose_name=u'Nose', max_length=200, blank=True, null=True)
    body_part_a_nose_points = models.IntegerField(blank=True, null=True)

    body_part_a_shoulder_answer = models.CharField(verbose_name=u'Shoulder', max_length=200, blank=True, null=True)
    body_part_a_shoulder_points = models.IntegerField(blank=True, null=True)

    body_part_a_knee_answer = models.CharField(verbose_name=u'Knee', max_length=200, blank=True, null=True)
    body_part_a_knee_points = models.IntegerField(blank=True, null=True)

    body_part_a_eyelid_answer = models.CharField(verbose_name=u'Eyelid', max_length=200, blank=True, null=True)
    body_part_a_eyelid_points = models.IntegerField(blank=True, null=True)

    body_part_a_ankle_answer = models.CharField(verbose_name=u'Ankle', max_length=200, blank=True, null=True)
    body_part_a_ankle_points = models.IntegerField(blank=True, null=True)

    body_part_a_chest_answer = models.CharField(verbose_name=u'Chest', max_length=200, blank=True, null=True)
    body_part_a_chest_points = models.IntegerField(blank=True, null=True)

    body_part_a_neck_answer = models.CharField(verbose_name=u'Neck', max_length=200, blank=True, null=True)
    body_part_a_neck_points = models.IntegerField(blank=True, null=True)

    body_part_a_middle_finger_answer = models.CharField(verbose_name=u'Middle finger', max_length=200, blank=True, null=True)
    body_part_a_middle_finger_points = models.IntegerField(blank=True, null=True)

    body_part_b_wrist_answer = models.CharField(verbose_name=u'Wrist', max_length=200, blank=True, null=True)
    body_part_b_wrist_points = models.IntegerField(blank=True, null=True)

    body_part_b_thumb_answer = models.CharField(verbose_name=u'Thumb', max_length=200, blank=True, null=True)
    body_part_b_thumb_points = models.IntegerField(blank=True, null=True)

    body_part_b_thigh_answer = models.CharField(verbose_name=u'Thigh', max_length=200, blank=True, null=True)
    body_part_b_thigh_points = models.IntegerField(blank=True, null=True)

    body_part_b_chin_answer = models.CharField(verbose_name=u'Chin', max_length=200, blank=True, null=True)
    body_part_b_chin_points = models.IntegerField(blank=True, null=True)

    body_part_b_elbow_answer = models.CharField(verbose_name=u'Elbow', max_length=200, blank=True, null=True)
    body_part_b_elbow_points = models.IntegerField(blank=True, null=True)

    body_part_b_lips_answer = models.CharField(verbose_name=u'Lips', max_length=200, blank=True, null=True)
    body_part_b_lips_points = models.IntegerField(blank=True, null=True)

    body_part_b_eyebrow_answer = models.CharField(verbose_name=u'Eyebrow', max_length=200, blank=True, null=True)
    body_part_b_eyebrow_points = models.IntegerField(blank=True, null=True)

    body_part_b_cheek_answer = models.CharField(verbose_name=u'Cheek', max_length=200, blank=True, null=True)
    body_part_b_cheek_points = models.IntegerField(blank=True, null=True)

    body_part_b_forefinger_answer = models.CharField(verbose_name=u'Forefinger', max_length=200, blank=True, null=True)
    body_part_b_forefinger_points = models.IntegerField(blank=True, null=True)

    body_part_c_right_ear_answer = models.CharField(verbose_name=u'Right ear', max_length=200, blank=True, null=True)
    body_part_c_right_ear_points = models.IntegerField(blank=True, null=True)

    body_part_c_left_shoulder_answer = models.CharField(verbose_name=u'Left shoulder', max_length=200, blank=True, null=True)
    body_part_c_left_shoulder_points = models.IntegerField(blank=True, null=True)

    body_part_c_left_knee_answer = models.CharField(verbose_name=u'Left knee', max_length=200, blank=True, null=True)
    body_part_c_left_knee_points = models.IntegerField(blank=True, null=True)

    body_part_c_right_ankle_answer = models.CharField(verbose_name=u'Right ankle', max_length=200, blank=True, null=True)
    body_part_c_right_ankle_points = models.IntegerField(blank=True, null=True)

    body_part_c_right_wrist_answer = models.CharField(verbose_name=u'Right wrist', max_length=200, blank=True, null=True)
    body_part_c_right_wrist_points = models.IntegerField(blank=True, null=True)

    body_part_c_left_thumb_answer = models.CharField(verbose_name=u'Left thumb', max_length=200, blank=True, null=True)
    body_part_c_left_thumb_points = models.IntegerField(blank=True, null=True)

    body_part_c_right_elbow_answer = models.CharField(verbose_name=u'Right elbow', max_length=200, blank=True, null=True)
    body_part_c_right_elbow_points = models.IntegerField(blank=True, null=True)

    body_part_c_left_cheek_answer = models.CharField(verbose_name=u'Left cheek', max_length=200, blank=True, null=True)
    body_part_c_left_cheek_points = models.IntegerField(blank=True, null=True)

    # COMMANDS
    command_close_fist = models.IntegerField(verbose_name=u'1. Make a fist', blank=True, null=True)
    command_point_ceiling = models.IntegerField(verbose_name=u'2. Point to the ceiling, then to the floor', blank=True, null=True)
    command_put_pencil = models.IntegerField(verbose_name=u'3. Put the pencil on top of the card, then put it back in place', blank=True, null=True)
    command_put_watch = models.IntegerField(verbose_name=u'4. Put the watch on the other side of the pencil and turn over the card', blank=True, null=True)
    command_touch_shoulder = models.IntegerField(verbose_name=u'5. Tap each shoulder twice with two fingers, keeping your eyes shut', blank=True, null=True)

    # COMPLEX IDEATIONAL MATERIAL
    complex_ideational_1a = models.IntegerField(verbose_name=u'1a. Will a cork sink in water?', blank=True, null=True)
    complex_ideational_2a = models.IntegerField(verbose_name=u'2a. Can you use a hammer to pound nails?', blank=True, null=True)
    complex_ideational_1b = models.IntegerField(verbose_name=u'1b. Will a stone sink in water?', blank=True, null=True)
    complex_ideational_2b = models.IntegerField(verbose_name=u'2b. Is a hammer good for cutting wood?', blank=True, null=True)

    complex_ideational_3a = models.IntegerField(verbose_name=u'3a. Do two pounds of flour weigh more than one?', blank=True, null=True)
    complex_ideational_4a = models.IntegerField(verbose_name=u'4a. Will water go through a ', blank=True, null=True)
    complex_ideational_3b = models.IntegerField(verbose_name=u'3b. Is one pound of flour heavier than two?', blank=True, null=True)
    complex_ideational_4b = models.IntegerField(verbose_name=u'4b. Will a good pair of rubber boots keep water out?', blank=True, null=True)

    # Mr. Jones had to go to New York.
    # He decided to take a train.
    # His wife drove him to the station, but on the way they had a flat tire.
    # However, they arrived at the station just in time for him to catch the train
    complex_ideational_5a = models.IntegerField(verbose_name=u'5a. Did Mr. Jones miss his train?', blank=True, null=True)
    complex_ideational_6a = models.IntegerField(verbose_name=u'6a. Was Mr. Jones going to New York?', blank=True, null=True)
    complex_ideational_5b = models.IntegerField(verbose_name=u'5b. Did he get to the station on time?', blank=True, null=True)
    complex_ideational_6b = models.IntegerField(verbose_name=u'6b. Was he on his way home from New York?', blank=True, null=True)

    # A soldier tried to cash a check in a bank near his camp.
    # The teller, firm but sympathetic, said,
    # "You will have to have identification from some of your friends from the camp."
    # The discoraged soldier answered, "But I don't have any friends in camp - I'm the bugler."
    complex_ideational_7a = models.IntegerField(verbose_name=u'7a. Was the soldier\'s check cashed at once?', blank=True, null=True)
    complex_ideational_8a = models.IntegerField(verbose_name=u'8a. Did the soldier have a friend with him?', blank=True, null=True)
    complex_ideational_7b = models.IntegerField(verbose_name=u'7b. Did the teller object to cashing the check?', blank=True, null=True)
    complex_ideational_8b = models.IntegerField(verbose_name=u'8b. Did the soldier have trouble finding friends?', blank=True, null=True)

    # A customer walked into a hotel carrying a coil of rope in one hand and a suitcase in the other.
    # The hotel clerk asked, "Pardon me, sir, but will you tell me what the rope is for?"
    # "Yes," replied the man, "That's my fire escape." "I'm sorry, sir," said the clerk,
    # "but all guests carrying their own fire escapes must pay in advance."
    complex_ideational_9a = models.IntegerField(verbose_name=u'9a. Was the customer carrying a suitcase in each hand?', blank=True, null=True)
    complex_ideational_10a = models.IntegerField(verbose_name=u'10a. Was the clerk suspicious of the guest?', blank=True, null=True)
    complex_ideational_9b = models.IntegerField(verbose_name=u'9b. Was the customer carrying something unusual in one hand?', blank=True, null=True)
    complex_ideational_10b = models.IntegerField(verbose_name=u'10b. Did the clerk trust this guest?', blank=True, null=True)

    # The lion cub is born with a deep-seated hunting instinct.
    # One cub will stalk and pounce on another with the same eagerness and thrill exhibited by a kitten.
    # During the year and a half of cubhood, this play develops into a hunting and killing technique.
    # Skill comes through long practice, imitation of the old lions, and obedience to warning growls of the mother.
    complex_ideational_11a = models.IntegerField(verbose_name=u'11a. Does this paragraph tell how lions learn to hunt?', blank=True, null=True)
    complex_ideational_12a = models.IntegerField(verbose_name=u'12a. Does this paragraph say that lions are skillful killers from the time they are born?', blank=True, null=True)
    complex_ideational_11b = models.IntegerField(verbose_name=u'11b. Does the paragraph tell how to hunt lions?', blank=True, null=True)
    complex_ideational_12b = models.IntegerField(verbose_name=u'12b. Does it say lions need practice before they can kill their prey?', blank=True, null=True)






