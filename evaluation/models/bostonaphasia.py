# -*- coding: utf-8 -*-
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
import reversion
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

    # WORD READING
    word_reading_chair_score = models.IntegerField(verbose_name=_(u'chair'), blank=True, null=True)
    word_reading_chair_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_chair_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_circle_score = models.IntegerField(verbose_name=_(u'circle'), blank=True, null=True)
    word_reading_circle_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_circle_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_hammock_score = models.IntegerField(verbose_name=_(u'hammock'), blank=True, null=True)
    word_reading_hammock_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_hammock_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_triangle_score = models.IntegerField(verbose_name=_(u'triangle'), blank=True, null=True)
    word_reading_triangle_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_triangle_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_fifteen_score = models.IntegerField(verbose_name=_(u'fifteen'), blank=True, null=True)
    word_reading_fifteen_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_fifteen_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_purple_score = models.IntegerField(verbose_name=_(u'purple'), blank=True, null=True)
    word_reading_purple_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_purple_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_seven_score = models.IntegerField(verbose_name=_(u'seven-twenty-one'), blank=True, null=True)
    word_reading_seven_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_seven_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_dripping_score = models.IntegerField(verbose_name=_(u'dripping'), blank=True, null=True)
    word_reading_dripping_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_dripping_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_brown_score = models.IntegerField(verbose_name=_(u'brown'), blank=True, null=True)
    word_reading_brown_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_brown_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    word_reading_smoking_score = models.IntegerField(verbose_name=_(u'smoking'), blank=True, null=True)
    word_reading_smoking_articulation = models.CharField(max_length=1, blank=True, null=True)
    word_reading_smoking_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    # RESPONSIVE NAMING
    responsive_naming_time_score = models.IntegerField(verbose_name=_(u'What do we tell time with?'), blank=True, null=True)
    responsive_naming_time_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_time_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_razor_score = models.IntegerField(verbose_name=_(u'What do you do with a razor?'), blank=True, null=True)
    responsive_naming_razor_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_razor_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_soap_score = models.IntegerField(verbose_name=_(u'What do you do with soap?'), blank=True, null=True)
    responsive_naming_soap_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_soap_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_pencil_score = models.IntegerField(verbose_name=_(u'What do you do with a pencil?'), blank=True, null=True)
    responsive_naming_pencil_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_pencil_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_paper_score = models.IntegerField(verbose_name=_(u'What do we cut paper with?'), blank=True, null=True)
    responsive_naming_paper_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_paper_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_grass_score = models.IntegerField(verbose_name=_(u'What color is grass?'), blank=True, null=True)
    responsive_naming_grass_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_grass_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_cigarette_score = models.IntegerField(verbose_name=_(u'What do we light a cigarette with?'), blank=True, null=True)
    responsive_naming_cigarette_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_cigarette_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_dozen_score = models.IntegerField(verbose_name=_(u'How many things ina dozen?'), blank=True, null=True)
    responsive_naming_dozen_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_dozen_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_coal_score = models.IntegerField(verbose_name=_(u'What color is coal?'), blank=True, null=True)
    responsive_naming_coal_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_coal_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    responsive_naming_medicine_score = models.IntegerField(verbose_name=_(u'Where do you go to buy medicine?'), blank=True, null=True)
    responsive_naming_medicine_articulation = models.CharField(max_length=1, blank=True, null=True)
    responsive_naming_medicine_paraphasia = models.CharField(max_length=1, blank=True, null=True)
reversion.register(BostonAphasia)


class BostonAphasiaVisualConfrontation(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='visualconfrontation')
    # VISUAL CONFRONTATION NAMING
    confrontation_card2_h_answer = models.CharField(verbose_name=_(u'H'), max_length=25, blank=True, null=True)
    confrontation_card2_h_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_h_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_h_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_t_answer = models.CharField(verbose_name=_(u'T'), max_length=25, blank=True, null=True)
    confrontation_card2_t_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_t_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_t_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_r_answer = models.CharField(verbose_name=_(u'R'), max_length=25, blank=True, null=True)
    confrontation_card2_r_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_r_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_r_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_l_answer = models.CharField(verbose_name=_(u'L'), max_length=25, blank=True, null=True)
    confrontation_card2_l_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_l_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_l_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_s_answer = models.CharField(verbose_name=_(u'S'), max_length=25, blank=True, null=True)
    confrontation_card2_s_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_s_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_s_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_g_answer = models.CharField(verbose_name=_(u'G'), max_length=25, blank=True, null=True)
    confrontation_card2_g_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_g_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_g_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_square_answer = models.CharField(verbose_name=_(u'square'), max_length=25, blank=True, null=True)
    confrontation_card2_square_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_square_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_square_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_chair_answer = models.CharField(verbose_name=_(u'chair'), max_length=25, blank=True, null=True)
    confrontation_card2_chair_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_chair_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_chair_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_key_answer = models.CharField(verbose_name=_(u'key'), max_length=25, blank=True, null=True)
    confrontation_card2_key_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_key_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_key_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_glove_answer = models.CharField(verbose_name=_(u'glove'), max_length=25, blank=True, null=True)
    confrontation_card2_glove_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_glove_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_glove_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_feather_answer = models.CharField(verbose_name=_(u'feather'), max_length=25, blank=True, null=True)
    confrontation_card2_feather_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_feather_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_feather_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_hammock_answer = models.CharField(verbose_name=_(u'hammock'), max_length=25, blank=True, null=True)
    confrontation_card2_hammock_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_hammock_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_hammock_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_cactus_answer = models.CharField(verbose_name=_(u'cactus'), max_length=25, blank=True, null=True)
    confrontation_card2_cactus_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_cactus_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_cactus_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card2_triangle_answer = models.CharField(verbose_name=_(u'triangle'), max_length=25, blank=True, null=True)
    confrontation_card2_triangle_score = models.IntegerField(blank=True, null=True)
    confrontation_card2_triangle_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card2_triangle_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_red_answer = models.CharField(verbose_name=_(u'red'), max_length=25, blank=True, null=True)
    confrontation_card3_red_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_red_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_red_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_brown_answer = models.CharField(verbose_name=_(u'brown'), max_length=25, blank=True, null=True)
    confrontation_card3_brown_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_brown_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_brown_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_pink_answer = models.CharField(verbose_name=_(u'pink'), max_length=25, blank=True, null=True)
    confrontation_card3_pink_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_pink_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_pink_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_blue_answer = models.CharField(verbose_name=_(u'blue'), max_length=25, blank=True, null=True)
    confrontation_card3_blue_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_blue_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_blue_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_gray_answer = models.CharField(verbose_name=_(u'gray'), max_length=25, blank=True, null=True)
    confrontation_card3_gray_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_gray_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_gray_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_purple_answer = models.CharField(verbose_name=_(u'purple'), max_length=25, blank=True, null=True)
    confrontation_card3_purple_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_purple_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_purple_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_7_answer = models.CharField(verbose_name=_(u'7'), max_length=25, blank=True, null=True)
    confrontation_card3_7_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_7_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_7_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_15_answer = models.CharField(verbose_name=_(u'15'), max_length=25, blank=True, null=True)
    confrontation_card3_15_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_15_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_15_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_700_answer = models.CharField(verbose_name=_(u'700'), max_length=25, blank=True, null=True)
    confrontation_card3_700_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_700_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_700_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_1936_answer = models.CharField(verbose_name=_(u'1936'), max_length=25, blank=True, null=True)
    confrontation_card3_1936_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_1936_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_1936_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_42_answer = models.CharField(verbose_name=_(u'42'), max_length=25, blank=True, null=True)
    confrontation_card3_42_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_42_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_42_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_7000_answer = models.CharField(verbose_name=_(u'7000'), max_length=25, blank=True, null=True)
    confrontation_card3_7000_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_7000_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_7000_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_smoking_answer = models.CharField(verbose_name=_(u'smoking'), max_length=25, blank=True, null=True)
    confrontation_card3_smoking_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_smoking_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_smoking_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_dripping_answer = models.CharField(verbose_name=_(u'dripping'), max_length=25, blank=True, null=True)
    confrontation_card3_dripping_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_dripping_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_dripping_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_falling_answer = models.CharField(verbose_name=_(u'falling'), max_length=25, blank=True, null=True)
    confrontation_card3_falling_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_falling_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_falling_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_sleeping_answer = models.CharField(verbose_name=_(u'sleeping'), max_length=25, blank=True, null=True)
    confrontation_card3_sleeping_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_sleeping_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_sleeping_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_drinking_answer = models.CharField(verbose_name=_(u'drinking'), max_length=25, blank=True, null=True)
    confrontation_card3_drinking_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_drinking_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_drinking_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_card3_running_answer = models.CharField(verbose_name=_(u'running'), max_length=25, blank=True, null=True)
    confrontation_card3_running_score = models.IntegerField(blank=True, null=True)
    confrontation_card3_running_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_card3_running_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_body_ear_answer = models.CharField(verbose_name=_(u'ear'), max_length=25, blank=True, null=True)
    confrontation_body_ear_score = models.IntegerField(blank=True, null=True)
    confrontation_body_ear_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_body_ear_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_body_nose_answer = models.CharField(verbose_name=_(u'nose'), max_length=25, blank=True, null=True)
    confrontation_body_nose_score = models.IntegerField(blank=True, null=True)
    confrontation_body_nose_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_body_nose_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_body_elbow_answer = models.CharField(verbose_name=_(u'elbow'), max_length=25, blank=True, null=True)
    confrontation_body_elbow_score = models.IntegerField(blank=True, null=True)
    confrontation_body_elbow_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_body_elbow_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_body_ankle_answer = models.CharField(verbose_name=_(u'ankle'), max_length=25, blank=True, null=True)
    confrontation_body_ankle_score = models.IntegerField(blank=True, null=True)
    confrontation_body_ankle_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_body_ankle_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_body_wrist_answer = models.CharField(verbose_name=_(u'wrist'), max_length=25, blank=True, null=True)
    confrontation_body_wrist_score = models.IntegerField(blank=True, null=True)
    confrontation_body_wrist_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_body_wrist_paraphasia = models.CharField(max_length=1, blank=True, null=True)

    confrontation_body_shoulder_answer = models.CharField(verbose_name=_(u'shoulder'), max_length=25, blank=True, null=True)
    confrontation_body_shoulder_score = models.IntegerField(blank=True, null=True)
    confrontation_body_shoulder_articulation = models.CharField(max_length=1, blank=True, null=True)
    confrontation_body_shoulder_paraphasia = models.CharField(max_length=1, blank=True, null=True)
reversion.register(BostonAphasiaVisualConfrontation, follow=["bostonAphasia"])


class BostonAphasiaAnimalNaming(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='animalnaming')

    animal_naming_answer = models.TextField(verbose_name=_(u'Answer'), max_length=500, blank=True, null=True)
    animal_naming_score = models.IntegerField(verbose_name=_(u'Score'), blank=True, null=True)
reversion.register(BostonAphasiaAnimalNaming, follow=["bostonAphasia"])


class BostonAphasiaOralSentenceReading(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='oralsentencereading')

    sentence_reading_a_score = models.IntegerField(verbose_name=_(u'You know how.'), blank=True, null=True)
    sentence_reading_a_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_b_score = models.IntegerField(verbose_name=_(u'Down to earth.'), blank=True, null=True)
    sentence_reading_b_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_c_score = models.IntegerField(verbose_name=_(u'I got home from work.'), blank=True, null=True)
    sentence_reading_c_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_d_score = models.IntegerField(verbose_name=_(u'Near the table in the dining room.'), blank=True, null=True)
    sentence_reading_d_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_e_score = models.IntegerField(verbose_name=_(u'They heard him speak on the radio last night.'), blank=True, null=True)
    sentence_reading_e_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_f_score = models.IntegerField(verbose_name=_(u'Limes are sour.'), blank=True, null=True)
    sentence_reading_f_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_g_score = models.IntegerField(verbose_name=_(u'The spy fled to Greece.'), blank=True, null=True)
    sentence_reading_g_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_h_score = models.IntegerField(verbose_name=_(u'The barm swallow captured a plump worm.'), blank=True, null=True)
    sentence_reading_h_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_i_score = models.IntegerField(verbose_name=_(u'The lawyer\'s closing argument convinced him.'), blank=True, null=True)
    sentence_reading_i_answer = models.CharField(max_length=100, blank=True, null=True)

    sentence_reading_j_score = models.IntegerField(verbose_name=_(u'The phantom soared across the foggy heath.'), blank=True, null=True)
    sentence_reading_j_answer = models.CharField(max_length=100, blank=True, null=True)
reversion.register(BostonAphasiaOralSentenceReading, follow=["bostonAphasia"])


class BostonAphasiaSymbolWordDisc(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='symbolworddisc')

    symbol_word_card8_a_score = models.IntegerField(verbose_name='In', blank=True, null=True)
    symbol_word_card8_b_score = models.IntegerField(verbose_name='J', blank=True, null=True)
    symbol_word_card8_c_score = models.IntegerField(verbose_name='H', blank=True, null=True)
    symbol_word_card8_d_score = models.IntegerField(verbose_name='salt', blank=True, null=True)
    symbol_word_card8_e_score = models.IntegerField(verbose_name='R', blank=True, null=True)

    symbol_word_card9_a_score = models.IntegerField(verbose_name='flower', blank=True, null=True)
    symbol_word_card9_b_score = models.IntegerField(verbose_name='B', blank=True, null=True)
    symbol_word_card9_c_score = models.IntegerField(verbose_name='lead', blank=True, null=True)
    symbol_word_card9_d_score = models.IntegerField(verbose_name='F', blank=True, null=True)
    symbol_word_card9_e_score = models.IntegerField(verbose_name='plus', blank=True, null=True)
reversion.register(BostonAphasiaSymbolWordDisc, follow=["bostonAphasia"])


class BostonAphasiaWordRecognition(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='wordrecognition')

    word_recognition_a_score = models.IntegerField(verbose_name=_(u'boat'), blank=True, null=True)
    word_recognition_b_score = models.IntegerField(verbose_name=_(u'frog'), blank=True, null=True)
    word_recognition_c_score = models.IntegerField(verbose_name=_(u'hammock'), blank=True, null=True)
    word_recognition_d_score = models.IntegerField(verbose_name=_(u'yours'), blank=True, null=True)
    word_recognition_e_score = models.IntegerField(verbose_name=_(u'mass'), blank=True, null=True)
    word_recognition_f_score = models.IntegerField(verbose_name=_(u'key'), blank=True, null=True)
    word_recognition_g_score = models.IntegerField(verbose_name=_(u'sum'), blank=True, null=True)
    word_recognition_h_score = models.IntegerField(verbose_name=_(u'want'), blank=True, null=True)
reversion.register(BostonAphasiaWordRecognition, follow=["bostonAphasia"])


class BostonAphasiaOralSpelling(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='oralspelling')

    oral_spelling_a_score = models.IntegerField(verbose_name=_(u'Y-E-S'), blank=True, null=True)
    oral_spelling_b_score = models.IntegerField(verbose_name=_(u'B-R-O-W-N'), blank=True, null=True)
    oral_spelling_c_score = models.IntegerField(verbose_name=_(u'M-A-N'), blank=True, null=True)
    oral_spelling_d_score = models.IntegerField(verbose_name=_(u'E-L-B-O-W'), blank=True, null=True)
    oral_spelling_e_score = models.IntegerField(verbose_name=_(u'W-O-M-A-N'), blank=True, null=True)
    oral_spelling_f_score = models.IntegerField(verbose_name=_(u'F-I-F-T-E-E-N'), blank=True, null=True)
    oral_spelling_g_score = models.IntegerField(verbose_name=_(u'W-I-P'), blank=True, null=True)
    oral_spelling_h_score = models.IntegerField(verbose_name=_(u'E-X-A-C-T'), blank=True, null=True)
reversion.register(BostonAphasiaOralSpelling, follow=["bostonAphasia"])


class BostonAphasiaWordPictureMatching(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='wordpicturematching')
    word_picture_chair_score = models.IntegerField(verbose_name=_(u'chair'), blank=True, null=True)
    word_picture_circle_score = models.IntegerField(verbose_name=_(u'circle'), blank=True, null=True)
    word_picture_hammock_score = models.IntegerField(verbose_name=_(u'hammock'), blank=True, null=True)
    word_picture_triangle_score = models.IntegerField(verbose_name=_(u'triangle'), blank=True, null=True)
    word_picture_fifteen_score = models.IntegerField(verbose_name=_(u'fifteen'), blank=True, null=True)
    word_picture_purple_score = models.IntegerField(verbose_name=_(u'purple'), blank=True, null=True)
    word_picture_seven_t_o_score = models.IntegerField(verbose_name=_(u'seven-twenty-one'), blank=True, null=True)
    word_picture_dripping_score = models.IntegerField(verbose_name=_(u'dripping'), blank=True, null=True)
    word_picture_brown_score = models.IntegerField(verbose_name=_(u'brown'), blank=True, null=True)
    word_picture_smoking_score = models.IntegerField(verbose_name=_(u'smoking'), blank=True, null=True)
reversion.register(BostonAphasiaWordPictureMatching, follow=["bostonAphasia"])


class BostonAphasiaReadingSentences(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='readingsentences')
    reading_sentences_dog_score = models.IntegerField(verbose_name=_(u'1. A dog can'), blank=True, null=True)
    reading_sentences_mother_score = models.IntegerField(verbose_name=_(u'2. A mother has a'), blank=True, null=True)
    reading_sentences_haircut_score = models.IntegerField(verbose_name=_(u'3. Mr. Jones gives haircuts and shampoos. He is a'), blank=True, null=True)
    reading_sentences_bird_score = models.IntegerField(verbose_name=_(u'4. Many birds come back in the summer. They build'), blank=True, null=True)
    reading_sentences_school_score = models.IntegerField(verbose_name=_(u'5. Schools and roads cost money. We all pay for them through'), blank=True, null=True)
    reading_sentences_artist_score = models.IntegerField(verbose_name=_(u'6. Artists are people who make beautiful paintings or statues. Another kind of artist is a'), blank=True, null=True)
    reading_sentences_aluminum_score = models.IntegerField(verbose_name=_(u'7. Aluminum was once very costly to refine. Now, electricity has solved the refining problem, and aluminum has become'), blank=True, null=True)
    reading_sentences_sanitation_score = models.IntegerField(verbose_name=_(u'8. The connection between sanitation and disease became clear when pasteur showed that food would not decay if germs were killed by heat and then sealed out. Sterilization by heat is a result of'), blank=True, null=True)
    reading_sentences_civil_service_score = models.IntegerField(verbose_name=_(u'9. Favoritism used to be the rule in civil service and many jobs paid more than they were worth. Civil service reform has resulted in classifying positions according to their duties and responsibilities. The aim of civil service classification is to'), blank=True, null=True)
    reading_sentences_government_score = models.IntegerField(verbose_name=_(u'10. In the early days of this country, the functions of government were few in number. Most of these functions were carried out by local town and contry officials, while centralized authority was distrusted. The growth of industry and of the cities has so changed the situation that the farmer of today is concerned with'), blank=True, null=True)
reversion.register(BostonAphasiaReadingSentences, follow=["bostonAphasia"])


class BostonAphasiaMechanicsWriting(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='mechanicswriting')
    mechanics_writing_score = models.IntegerField(verbose_name=_(u'Qualification level of writing mechanics:'), blank=True, null=True)
reversion.register(BostonAphasiaMechanicsWriting, follow=["bostonAphasia"])


class BostonAphasiaRecallWrittenSymbols(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='recallwrittensymbols')
    serial_writing_letters_score = models.IntegerField(verbose_name=_(u'Qualification level of writing mechanics:'), blank=True, null=True)
    serial_writing_numbers_score = models.IntegerField(blank=True, null=True)
reversion.register(BostonAphasiaRecallWrittenSymbols, follow=["bostonAphasia"])


class BostonAphasiaDictatedWords(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='dictatedwords')
    dictated_words_letters_score = models.IntegerField(verbose_name=_(u'Dictated letters (B - K - L - R - T)'), blank=True, null=True)
    dictated_words_numbers_score = models.IntegerField(verbose_name=_(u'Dictated numbers (7 - 15 - 42 - 193 - 1865)'), blank=True, null=True)
    dictated_words_words_score = models.IntegerField(verbose_name=_(u'Dictated words (go - boy - run - come - baby)'), blank=True, null=True)
reversion.register(BostonAphasiaDictatedWords, follow=["bostonAphasia"])


class BostonAphasiaCopyPangramPhrase(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='copypangramphrase')
    copy_pangram_phrase_score = models.IntegerField(verbose_name=_(u'Copy score'), blank=True, null=True)
reversion.register(BostonAphasiaCopyPangramPhrase, follow=["bostonAphasia"])


class BostonAphasiaSpellingDictation(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='spellingdictation')
    spelling_dictation_a_score = models.IntegerField(verbose_name=_(u'soft'), blank=True, null=True)
    spelling_dictation_a_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_b_score = models.IntegerField(verbose_name=_(u'own'), blank=True, null=True)
    spelling_dictation_b_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_c_score = models.IntegerField(verbose_name=_(u'soap'), blank=True, null=True)
    spelling_dictation_c_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_d_score = models.IntegerField(verbose_name=_(u'fight'), blank=True, null=True)
    spelling_dictation_d_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_e_score = models.IntegerField(verbose_name=_(u'uncle'), blank=True, null=True)
    spelling_dictation_e_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_f_score = models.IntegerField(verbose_name=_(u'freedom'), blank=True, null=True)
    spelling_dictation_f_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_g_score = models.IntegerField(verbose_name=_(u'theater'), blank=True, null=True)
    spelling_dictation_g_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_h_score = models.IntegerField(verbose_name=_(u'private'), blank=True, null=True)
    spelling_dictation_h_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_i_score = models.IntegerField(verbose_name=_(u'physician'), blank=True, null=True)
    spelling_dictation_i_answer = models.CharField(max_length=100, blank=True, null=True)

    spelling_dictation_j_score = models.IntegerField(verbose_name=_(u'awareness'), blank=True, null=True)
    spelling_dictation_j_answer = models.CharField(max_length=100, blank=True, null=True)
reversion.register(BostonAphasiaSpellingDictation, follow=["bostonAphasia"])


class BostonAphasiaWrittenPictureNaming(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='writtenpicturenaming')
    written_picture_naming_a_score = models.IntegerField(verbose_name=_(u'key'), blank=True, null=True)
    written_picture_naming_b_score = models.IntegerField(verbose_name=_(u'chair'), blank=True, null=True)
    written_picture_naming_c_score = models.IntegerField(verbose_name=_(u'circle'), blank=True, null=True)
    written_picture_naming_d_score = models.IntegerField(verbose_name=_(u'square'), blank=True, null=True)
    written_picture_naming_e_score = models.IntegerField(verbose_name=_(u'fifteen'), blank=True, null=True)
    written_picture_naming_f_score = models.IntegerField(verbose_name=_(u'seven'), blank=True, null=True)
    written_picture_naming_g_score = models.IntegerField(verbose_name=_(u'brown'), blank=True, null=True)
    written_picture_naming_h_score = models.IntegerField(verbose_name=_(u'red'), blank=True, null=True)
    written_picture_naming_i_score = models.IntegerField(verbose_name=_(u'drinking'), blank=True, null=True)
    written_picture_naming_j_score = models.IntegerField(verbose_name=_(u'smoking'), blank=True, null=True)
reversion.register(BostonAphasiaWrittenPictureNaming, follow=["bostonAphasia"])


class BostonAphasiaNarrativeWriting(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='narrativewriting')
    narrative_writing_score = models.IntegerField(verbose_name=_(u'Total'), blank=True, null=True)
reversion.register(BostonAphasiaNarrativeWriting, follow=["bostonAphasia"])


class BostonAphasiaSentecesWrittenDictation(models.Model):
    bostonAphasia = models.OneToOneField(BostonAphasia, related_name='senteceswrittendictation')
    sentences_written_dictation_a_score = models.IntegerField(verbose_name=_(u'She can not see him.'), blank=True, null=True)
    sentences_written_dictation_a_exchanges = models.IntegerField(blank=True, null=True)

    sentences_written_dictation_b_score = models.IntegerField(verbose_name=_(u'The boy is stealing cookies'), blank=True, null=True)
    sentences_written_dictation_b_exchanges = models.IntegerField(blank=True, null=True)

    sentences_written_dictation_c_score = models.IntegerField(verbose_name=_(u'If he is not careful the stool will fall'), blank=True, null=True)
    sentences_written_dictation_c_exchanges = models.IntegerField(blank=True, null=True)
reversion.register(BostonAphasiaSentecesWrittenDictation, follow=["bostonAphasia"])





"""
Understanding written language

Symbol word discrimination
Phonetic Word recognition
comprehension of Oral spelling
Word-picture matching
sentence and paragraph comprehension
"""

