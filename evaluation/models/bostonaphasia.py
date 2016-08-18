# -*- coding: utf-8 -*-
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
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
    body_part_a_ear_answer = models.CharField(verbose_name=_(u'Ear'), max_length=200, blank=True, null=True)
    body_part_a_ear_points = models.IntegerField(verbose_name=_(u'Ear'), blank=True, null=True)

    body_part_a_nose_answer = models.CharField(verbose_name=_(u'Nose'), max_length=200, blank=True, null=True)
    body_part_a_nose_points = models.IntegerField(verbose_name=_(u'Nose'), blank=True, null=True)

    body_part_a_shoulder_answer = models.CharField(verbose_name=_(u'Shoulder'), max_length=200, blank=True, null=True)
    body_part_a_shoulder_points = models.IntegerField(verbose_name=_(u'Shoulder'), blank=True, null=True)

    body_part_a_knee_answer = models.CharField(verbose_name=_(u'Knee'), max_length=200, blank=True, null=True)
    body_part_a_knee_points = models.IntegerField(verbose_name=_(u'Knee'), blank=True, null=True)

    body_part_a_eyelid_answer = models.CharField(verbose_name=_(u'Eyelid'), max_length=200, blank=True, null=True)
    body_part_a_eyelid_points = models.IntegerField(verbose_name=_(u'Eyelid'), blank=True, null=True)

    body_part_a_ankle_answer = models.CharField(verbose_name=_(u'Ankle'), max_length=200, blank=True, null=True)
    body_part_a_ankle_points = models.IntegerField(verbose_name=_(u'Ankle'), blank=True, null=True)

    body_part_a_chest_answer = models.CharField(verbose_name=_(u'Chest'), max_length=200, blank=True, null=True)
    body_part_a_chest_points = models.IntegerField(verbose_name=_(u'Chest'), blank=True, null=True)

    body_part_a_neck_answer = models.CharField(verbose_name=_(u'Neck'), max_length=200, blank=True, null=True)
    body_part_a_neck_points = models.IntegerField(verbose_name=_(u'Neck'), blank=True, null=True)

    body_part_a_middle_finger_answer = models.CharField(verbose_name=_(u'Middle finger'), max_length=200, blank=True, null=True)
    body_part_a_middle_finger_points = models.IntegerField(verbose_name=_(u'Middle finger'), blank=True, null=True)

    body_part_b_wrist_answer = models.CharField(verbose_name=_(u'Wrist'), max_length=200, blank=True, null=True)
    body_part_b_wrist_points = models.IntegerField(verbose_name=_(u'Wrist'), blank=True, null=True)

    body_part_b_thumb_answer = models.CharField(verbose_name=_(u'Thumb'), max_length=200, blank=True, null=True)
    body_part_b_thumb_points = models.IntegerField(verbose_name=_(u'Thumb'), blank=True, null=True)

    body_part_b_thigh_answer = models.CharField(verbose_name=_(u'Thigh'), max_length=200, blank=True, null=True)
    body_part_b_thigh_points = models.IntegerField(verbose_name=_(u'Thigh'), blank=True, null=True)

    body_part_b_chin_answer = models.CharField(verbose_name=_(u'Chin'), max_length=200, blank=True, null=True)
    body_part_b_chin_points = models.IntegerField(verbose_name=_(u'Chin'), blank=True, null=True)

    body_part_b_elbow_answer = models.CharField(verbose_name=_(u'Elbow'), max_length=200, blank=True, null=True)
    body_part_b_elbow_points = models.IntegerField(verbose_name=_(u'Elbow'), blank=True, null=True)

    body_part_b_lips_answer = models.CharField(verbose_name=_(u'Lips'), max_length=200, blank=True, null=True)
    body_part_b_lips_points = models.IntegerField(verbose_name=_(u'Lips'), blank=True, null=True)

    body_part_b_eyebrow_answer = models.CharField(verbose_name=_(u'Eyebrow'), max_length=200, blank=True, null=True)
    body_part_b_eyebrow_points = models.IntegerField(verbose_name=_(u'Eyebrow'), blank=True, null=True)

    body_part_b_cheek_answer = models.CharField(verbose_name=_(u'Cheek'), max_length=200, blank=True, null=True)
    body_part_b_cheek_points = models.IntegerField(verbose_name=_(u'Cheek'), blank=True, null=True)

    body_part_b_forefinger_answer = models.CharField(verbose_name=_(u'Forefinger'), max_length=200, blank=True, null=True)
    body_part_b_forefinger_points = models.IntegerField(verbose_name=_(u'Forefinger'), blank=True, null=True)

    body_part_c_right_ear_answer = models.CharField(verbose_name=_(u'Right ear'), max_length=200, blank=True, null=True)
    body_part_c_right_ear_points = models.IntegerField(verbose_name=_(u'Right ear'), blank=True, null=True)

    body_part_c_left_shoulder_answer = models.CharField(verbose_name=_(u'Left shoulder'), max_length=200, blank=True, null=True)
    body_part_c_left_shoulder_points = models.IntegerField(verbose_name=_(u'Left shoulder'), blank=True, null=True)

    body_part_c_left_knee_answer = models.CharField(verbose_name=_(u'Left knee'), max_length=200, blank=True, null=True)
    body_part_c_left_knee_points = models.IntegerField(verbose_name=_(u'Left knee'), blank=True, null=True)

    body_part_c_right_ankle_answer = models.CharField(verbose_name=_(u'Right ankle'), max_length=200, blank=True, null=True)
    body_part_c_right_ankle_points = models.IntegerField(verbose_name=_(u'Right ankle'), blank=True, null=True)

    body_part_c_right_wrist_answer = models.CharField(verbose_name=_(u'Right wrist'), max_length=200, blank=True, null=True)
    body_part_c_right_wrist_points = models.IntegerField(verbose_name=_(u'Right wrist'), blank=True, null=True)

    body_part_c_left_thumb_answer = models.CharField(verbose_name=_(u'Left thumb'), max_length=200, blank=True, null=True)
    body_part_c_left_thumb_points = models.IntegerField(verbose_name=_(u'Left thumb'), blank=True, null=True)

    body_part_c_right_elbow_answer = models.CharField(verbose_name=_(u'Right elbow'), max_length=200, blank=True, null=True)
    body_part_c_right_elbow_points = models.IntegerField(verbose_name=_(u'Right elbow'), blank=True, null=True)

    body_part_c_left_cheek_answer = models.CharField(verbose_name=_(u'Left cheek'), max_length=200, blank=True, null=True)
    body_part_c_left_cheek_points = models.IntegerField(verbose_name=_(u'Left cheek'), blank=True, null=True)

    # COMMANDS
    command_close_fist = models.IntegerField(verbose_name=_(u'1. Make a "fist"'), blank=True, null=True)
    command_point_ceiling = models.IntegerField(verbose_name=_(u'2. Point to "the ceiling", then to "the floor"'), blank=True, null=True)
    command_put_pencil = models.IntegerField(verbose_name=_(u'3. Put "the pencil" on "top of the card", then "put it back in place"'), blank=True, null=True)
    command_put_watch = models.IntegerField(verbose_name=_(u'4. Put "the watch" on "the other side" of "the pencil" and "turn over the card"'), blank=True, null=True)
    command_touch_shoulder = models.IntegerField(verbose_name=_(u'5. Tap "each shoulder" "twice" with "two fingers", keeping your "eyes shut"'), blank=True, null=True)

    # COMPLEX IDEATIONAL MATERIAL
    complex_ideational_1a = models.IntegerField(verbose_name=_(u'1a. Will a cork sink in water?'), blank=True, null=True)
    complex_ideational_2a = models.IntegerField(verbose_name=_(u'2a. Can you use a hammer to pound nails?'), blank=True, null=True)
    complex_ideational_1b = models.IntegerField(verbose_name=_(u'1b. Will a stone sink in water?'), blank=True, null=True)
    complex_ideational_2b = models.IntegerField(verbose_name=_(u'2b. Is a hammer good for cutting wood?'), blank=True, null=True)

    complex_ideational_3a = models.IntegerField(verbose_name=_(u'3a. Do two pounds of flour weigh more than one?'), blank=True, null=True)
    complex_ideational_4a = models.IntegerField(verbose_name=_(u'4a. Will water go through a good pair of rubber boots?'), blank=True, null=True)
    complex_ideational_3b = models.IntegerField(verbose_name=_(u'3b. Is one pound of flour heavier than two?'), blank=True, null=True)
    complex_ideational_4b = models.IntegerField(verbose_name=_(u'4b. Will a good pair of rubber boots keep water out?'), blank=True, null=True)

    # Mr. Jones had to go to New York.
    # He decided to take a train.
    # His wife drove him to the station, but on the way they had a flat tire.
    # However, they arrived at the station just in time for him to catch the train
    complex_ideational_5a = models.IntegerField(verbose_name=_(u'5a. Did Mr. Jones miss his train?'), blank=True, null=True)
    complex_ideational_6a = models.IntegerField(verbose_name=_(u'6a. Was Mr. Jones going to New York?'), blank=True, null=True)
    complex_ideational_5b = models.IntegerField(verbose_name=_(u'5b. Did he get to the station on time?'), blank=True, null=True)
    complex_ideational_6b = models.IntegerField(verbose_name=_(u'6b. Was he on his way home from New York?'), blank=True, null=True)

    # A soldier tried to cash a check in a bank near his camp.
    # The teller, firm but sympathetic, said,
    # "You will have to have identification from some of your friends from the camp."
    # The discoraged soldier answered, "But I don't have any friends in camp - I'm the bugler."
    complex_ideational_7a = models.IntegerField(verbose_name=_(u'7a. Was the soldier\'s check cashed at once?'), blank=True, null=True)
    complex_ideational_8a = models.IntegerField(verbose_name=_(u'8a. Did the soldier have a friend with him?'), blank=True, null=True)
    complex_ideational_7b = models.IntegerField(verbose_name=_(u'7b. Did the teller object to cashing the check?'), blank=True, null=True)
    complex_ideational_8b = models.IntegerField(verbose_name=_(u'8b. Did the soldier have trouble finding friends?'), blank=True, null=True)

    # A customer walked into a hotel carrying a coil of rope in one hand and a suitcase in the other.
    # The hotel clerk asked, "Pardon me, sir, but will you tell me what the rope is for?"
    # "Yes," replied the man, "That's my fire escape." "I'm sorry, sir," said the clerk,
    # "but all guests carrying their own fire escapes must pay in advance."
    complex_ideational_9a = models.IntegerField(verbose_name=_(u'9a. Was the customer carrying a suitcase in each hand?'), blank=True, null=True)
    complex_ideational_10a = models.IntegerField(verbose_name=_(u'10a. Was the clerk suspicious of the guest?'), blank=True, null=True)
    complex_ideational_9b = models.IntegerField(verbose_name=_(u'9b. Was the customer carrying something unusual in one hand?'), blank=True, null=True)
    complex_ideational_10b = models.IntegerField(verbose_name=_(u'10b. Did the clerk trust this guest?'), blank=True, null=True)

    # The lion cub is born with a deep-seated hunting instinct.
    # One cub will stalk and pounce on another with the same eagerness and thrill exhibited by a kitten.
    # During the year and a half of cubhood, this play develops into a hunting and killing technique.
    # Skill comes through long practice, imitation of the old lions, and obedience to warning growls of the mother.
    complex_ideational_11a = models.IntegerField(verbose_name=_(u'11a. Does this paragraph tell how lions learn to hunt?'), blank=True, null=True)
    complex_ideational_12a = models.IntegerField(verbose_name=_(u'12a. Does this paragraph say that lions are skillful killers from the time they are born?'), blank=True, null=True)
    complex_ideational_11b = models.IntegerField(verbose_name=_(u'11b. Does the paragraph tell how to hunt lions?'), blank=True, null=True)
    complex_ideational_12b = models.IntegerField(verbose_name=_(u'12b. Does it say lions need practice before they can kill their prey?'), blank=True, null=True)

    # ORAL EXPRESSION
    # ORAL AGILITY
    # Nonverbal agility: Have the patient carry out the following rapidly repeated mouth movements as well as he can,
    # after you demonstrate and describe the movement
    # Count the number of full alternations carried out in 5 seconds.
    oral_agility_lips_purse = models.IntegerField(verbose_name=_(u'Purse lips, release'), blank=True, null=True)
    oral_agility_mouth_open = models.IntegerField(verbose_name=_(u'Open and close mouth'), blank=True, null=True)
    oral_agility_lips_retract = models.IntegerField(verbose_name=_(u'Retract lips, release'), blank=True, null=True)
    oral_agility_tongue_corner = models.IntegerField(verbose_name=_(u'Tongue to alternate corners of mouth'), blank=True, null=True)
    oral_agility_tongue_protude = models.IntegerField(verbose_name=_(u'Protrude and retract tongue'), blank=True, null=True)
    oral_agility_tongue_teeth = models.IntegerField(verbose_name=_(u'Tongue to upper and lower teeth'), blank=True, null=True)

    # Verbal agility: Have the patient repeat the following words as rapidly as he can,
    # while you time the number of repetitions for 5 seconds
    # Any assistance which helps patient to produce the desired word initially is permitted.
    verbal_agility_a = models.IntegerField(verbose_name=_(u'Mama, mama'), blank=True, null=True)
    verbal_agility_b = models.IntegerField(verbose_name=_(u'Tip-top, tip-top'), blank=True, null=True)
    verbal_agility_c = models.IntegerField(verbose_name=_(u'Fifty-fifty, fifty-fifty'), blank=True, null=True)
    verbal_agility_d = models.IntegerField(verbose_name=_(u'Thanks, thanks'), blank=True, null=True)
    verbal_agility_e = models.IntegerField(verbose_name=_(u'Huckleberry'), blank=True, null=True)
    verbal_agility_f = models.IntegerField(verbose_name=_(u'Baseball player, baseball player'), blank=True, null=True)
    verbal_agility_g = models.IntegerField(verbose_name=_(u'Caterpillar'), blank=True, null=True)

    # AUTOMATIZED SEQUENCES
    # Have patient recite each of the following four series, giving him assistance with the first word, if necessary.
    # Provide further assistance as needed, but discontinue a series when patient fails with four successive words.
    # Record assistance given by circling the word; cross out words omitted by patient.
    # Allow 0, 1 or 2 points, as indicated.
    automzatized_days_week = models.IntegerField(verbose_name=_(u'1. Days of the week:'), blank=True, null=True)
    automzatized_days_week_note = models.TextField(max_length=250, blank=True, null=True)
    automzatized_months_year = models.IntegerField(verbose_name=_(u'2. Months of the year:'), blank=True, null=True)
    automzatized_months_year_note = models.TextField(max_length=250, blank=True, null=True)
    automzatized_counting_21 = models.IntegerField(verbose_name=_(u'3. Counting to 21:'), blank=True, null=True)
    automzatized_counting_21_note = models.TextField(max_length=250, blank=True, null=True)
    automzatized_alphabet = models.IntegerField(verbose_name=_(u'4. Alphabet:'), blank=True, null=True)
    automzatized_alphabet_note = models.TextField(max_length=250, blank=True, null=True)

    # RECITATION, SINGING AND RHYTHM
    reciting_note = models.TextField(verbose_name=_(u'Reciting'), help_text=_(u'Jack and Jill (went)...'), max_length=250, blank=True, null=True)
    reciting_score = models.IntegerField(verbose_name=_(u'Reciting'), help_text=_(u'Jack and Jill (went)...'), blank=True, null=True)

    singing_note = models.TextField(verbose_name=_(u'Singing'), help_text=_(u'After recitation have patient sing this or any othet song with which he is familiar'), max_length=250, blank=True, null=True)
    singing_score = models.IntegerField(verbose_name=_(u'Singing'), help_text=_(u'After recitation have patient sing this or any othet song with which he is familiar'), blank=True, null=True)

    # REPETITION OF WORDS
    repetition_words_what_score = models.IntegerField(verbose_name=_(u'What'), blank=True, null=True)
    repetition_words_what_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_what_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_what_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_chair_score = models.IntegerField(verbose_name=_(u'Chair'), blank=True, null=True)
    repetition_words_chair_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_chair_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_chair_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_hammock_score = models.IntegerField(verbose_name=_(u'Hammock'), blank=True, null=True)
    repetition_words_hammock_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_hammock_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_hammock_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_purple_score = models.IntegerField(verbose_name=_(u'Purple'), blank=True, null=True)
    repetition_words_purple_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_purple_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_purple_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_brown_score = models.IntegerField(verbose_name=_(u'Brown'), blank=True, null=True)
    repetition_words_brown_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_brown_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_brown_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_w_score = models.IntegerField(verbose_name=_(u'W'), blank=True, null=True)
    repetition_words_w_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_w_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_w_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_fifteen_score = models.IntegerField(verbose_name=_(u'Fifteen'), blank=True, null=True)
    repetition_words_fifteen_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_fifteen_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_fifteen_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_1776_score = models.IntegerField(verbose_name=_(u'1776'), blank=True, null=True)
    repetition_words_1776_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_1776_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_1776_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_emphasize_score = models.IntegerField(verbose_name=_(u'Emphasize'), blank=True, null=True)
    repetition_words_emphasize_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_emphasize_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_emphasize_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_words_episcopal_score = models.IntegerField(verbose_name=_(u'Methodist Episcopal'), blank=True, null=True)
    repetition_words_episcopal_transcription = models.TextField(max_length=150, blank=True, null=True)
    repetition_words_episcopal_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_words_episcopal_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    # REPEATING PHRASES
    repetition_phrases_high_a_score = models.IntegerField(verbose_name=_(u'a. You know how'), blank=True, null=True)
    repetition_phrases_high_a_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_a_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_b_score = models.IntegerField(verbose_name=_(u'b. Down to earth.'), blank=True, null=True)
    repetition_phrases_high_b_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_b_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_c_score = models.IntegerField(verbose_name=_(u'c. I got home from work.'), blank=True, null=True)
    repetition_phrases_high_c_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_c_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_d_score = models.IntegerField(verbose_name=_(u'd. You should not tell her.'), blank=True, null=True)
    repetition_phrases_high_d_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_d_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_e_score = models.IntegerField(verbose_name=_(u'e. Go ahead and do it if possible'), blank=True, null=True)
    repetition_phrases_high_e_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_e_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_f_score = models.IntegerField(verbose_name=_(u'f. Near the table in the dining room.'), blank=True, null=True)
    repetition_phrases_high_f_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_f_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_g_score = models.IntegerField(verbose_name=_(u'g. They heard him speak on the radio last night.'), blank=True, null=True)
    repetition_phrases_high_g_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_g_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_high_h_score = models.IntegerField(verbose_name=_(u'h. I stopped at his front door and rang the bell.'), blank=True, null=True)
    repetition_phrases_high_h_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_high_h_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_a_score = models.IntegerField(verbose_name=_(u'a. The vat leaks.'), blank=True, null=True)
    repetition_phrases_low_a_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_a_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_b_score = models.IntegerField(verbose_name=_(u'b. limes are sour.'), blank=True, null=True)
    repetition_phrases_low_b_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_b_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_c_score = models.IntegerField(verbose_name=_(u'c. The spy fled to Greece.'), blank=True, null=True)
    repetition_phrases_low_c_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_c_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_d_score = models.IntegerField(verbose_name=_(u'd. Pry the tin lid off.'), blank=True, null=True)
    repetition_phrases_low_d_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_d_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_e_score = models.IntegerField(verbose_name=_(u'e. The Chinese fan had a rare emerald.'), blank=True, null=True)
    repetition_phrases_low_e_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_e_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_f_score = models.IntegerField(verbose_name=_(u'f. The barn swallow captured a plump worm.'), blank=True, null=True)
    repetition_phrases_low_f_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_f_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_g_score = models.IntegerField(verbose_name=_(u'g. The lawyer\'s closing argument convinced him.'), blank=True, null=True)
    repetition_phrases_low_g_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_g_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    repetition_phrases_low_h_score = models.IntegerField(verbose_name=_(u'h. The phantom soared across the foggy heath.'), blank=True, null=True)
    repetition_phrases_low_h_articulation = models.CharField(max_length=1, blank=True, null=True)
    repetition_phrases_low_h_paraphasia = models.CharField(max_length=1, blank=True, null=True)



