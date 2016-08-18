# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0007_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eegfile',
            options={'verbose_name': 'Arquivo EEG', 'verbose_name_plural': 'Arquivos EEG'},
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='write_or_distribute_card_deck_left_hand',
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='write_or_distribute_card_deck_right_hand',
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_ankle_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Ankle', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_ankle_points',
            field=models.IntegerField(null=True, verbose_name='Ankle', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_chest_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Chest', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_chest_points',
            field=models.IntegerField(null=True, verbose_name='Chest', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_ear_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Ear', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_ear_points',
            field=models.IntegerField(null=True, verbose_name='Ear', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_eyelid_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Eyelid', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_eyelid_points',
            field=models.IntegerField(null=True, verbose_name='Eyelid', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_knee_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Knee', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_knee_points',
            field=models.IntegerField(null=True, verbose_name='Knee', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_middle_finger_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Middle finger', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_middle_finger_points',
            field=models.IntegerField(null=True, verbose_name='Middle finger', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_neck_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Neck', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_neck_points',
            field=models.IntegerField(null=True, verbose_name='Neck', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_nose_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Nose', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_nose_points',
            field=models.IntegerField(null=True, verbose_name='Nose', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_shoulder_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Shoulder', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_a_shoulder_points',
            field=models.IntegerField(null=True, verbose_name='Shoulder', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_cheek_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Cheek', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_cheek_points',
            field=models.IntegerField(null=True, verbose_name='Cheek', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_chin_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Chin', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_chin_points',
            field=models.IntegerField(null=True, verbose_name='Chin', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_elbow_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Elbow', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_elbow_points',
            field=models.IntegerField(null=True, verbose_name='Elbow', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_eyebrow_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Eyebrow', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_eyebrow_points',
            field=models.IntegerField(null=True, verbose_name='Eyebrow', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_forefinger_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Forefinger', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_forefinger_points',
            field=models.IntegerField(null=True, verbose_name='Forefinger', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_lips_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Lips', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_lips_points',
            field=models.IntegerField(null=True, verbose_name='Lips', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_thigh_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Thigh', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_thigh_points',
            field=models.IntegerField(null=True, verbose_name='Thigh', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_thumb_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Thumb', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_thumb_points',
            field=models.IntegerField(null=True, verbose_name='Thumb', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_wrist_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Wrist', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_b_wrist_points',
            field=models.IntegerField(null=True, verbose_name='Wrist', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_cheek_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Left cheek', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_cheek_points',
            field=models.IntegerField(null=True, verbose_name='Left cheek', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_knee_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Left knee', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_knee_points',
            field=models.IntegerField(null=True, verbose_name='Left knee', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_shoulder_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Left shoulder', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_shoulder_points',
            field=models.IntegerField(null=True, verbose_name='Left shoulder', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_thumb_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Left thumb', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_left_thumb_points',
            field=models.IntegerField(null=True, verbose_name='Left thumb', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_ankle_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Right ankle', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_ankle_points',
            field=models.IntegerField(null=True, verbose_name='Right ankle', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_ear_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Right ear', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_ear_points',
            field=models.IntegerField(null=True, verbose_name='Right ear', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_elbow_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Right elbow', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_elbow_points',
            field=models.IntegerField(null=True, verbose_name='Right elbow', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_wrist_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Right wrist', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='body_part_c_right_wrist_points',
            field=models.IntegerField(null=True, verbose_name='Right wrist', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='command_close_fist',
            field=models.IntegerField(null=True, verbose_name='1. Make a fist', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='command_point_ceiling',
            field=models.IntegerField(null=True, verbose_name='2. Point to the ceiling, then to the floor', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='command_put_pencil',
            field=models.IntegerField(null=True, verbose_name='3. Put the pencil on top of the card, then put it back in place', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='command_put_watch',
            field=models.IntegerField(null=True, verbose_name='4. Put the watch on the other side of the pencil and turn over the card', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='command_touch_shoulder',
            field=models.IntegerField(null=True, verbose_name='5. Tap each shoulder twice with two fingers, keeping your eyes shut', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_10a',
            field=models.IntegerField(null=True, verbose_name='10a. Was the clerk suspicious of the guest?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_10b',
            field=models.IntegerField(null=True, verbose_name='10b. Did the clerk trust this guest?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_11a',
            field=models.IntegerField(null=True, verbose_name='11a. Does this paragraph tell how lions learn to hunt?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_11b',
            field=models.IntegerField(null=True, verbose_name='11b. Does the paragraph tell how to hunt lions?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_12a',
            field=models.IntegerField(null=True, verbose_name='12a. Does this paragraph say that lions are skillful killers from the time they are born?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_12b',
            field=models.IntegerField(null=True, verbose_name='12b. Does it say lions need practice before they can kill their prey?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_1a',
            field=models.IntegerField(null=True, verbose_name='1a. Will a cork sink in water?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_1b',
            field=models.IntegerField(null=True, verbose_name='1b. Will a stone sink in water?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_2a',
            field=models.IntegerField(null=True, verbose_name='2a. Can you use a hammer to pound nails?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_2b',
            field=models.IntegerField(null=True, verbose_name='2b. Is a hammer good for cutting wood?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_3a',
            field=models.IntegerField(null=True, verbose_name='3a. Do two pounds of flour weigh more than one?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_3b',
            field=models.IntegerField(null=True, verbose_name='3b. Is one pound of flour heavier than two?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_4a',
            field=models.IntegerField(null=True, verbose_name='4a. Will water go through a good pair of rubber boots?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_4b',
            field=models.IntegerField(null=True, verbose_name='4b. Will a good pair of rubber boots keep water out?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_5a',
            field=models.IntegerField(null=True, verbose_name='5a. Did Mr. Jones miss his train?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_5b',
            field=models.IntegerField(null=True, verbose_name='5b. Did he get to the station on time?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_6a',
            field=models.IntegerField(null=True, verbose_name='6a. Was Mr. Jones going to New York?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_6b',
            field=models.IntegerField(null=True, verbose_name='6b. Was he on his way home from New York?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_7a',
            field=models.IntegerField(null=True, verbose_name="7a. Was the soldier's check cashed at once?", blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_7b',
            field=models.IntegerField(null=True, verbose_name='7b. Did the teller object to cashing the check?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_8a',
            field=models.IntegerField(null=True, verbose_name='8a. Did the soldier have a friend with him?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_8b',
            field=models.IntegerField(null=True, verbose_name='8b. Did the soldier have trouble finding friends?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_9a',
            field=models.IntegerField(null=True, verbose_name='9a. Was the customer carrying a suitcase in each hand?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='complex_ideational_9b',
            field=models.IntegerField(null=True, verbose_name='9b. Was the customer carrying something unusual in one hand?', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_g_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='G', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_g_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_h_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='H', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_h_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_l_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='L', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_l_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_r_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='R', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_r_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_s_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='S', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_s_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_t_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='T', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_letter_t_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_circle_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Circle', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_circle_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_cone_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Cone', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_cone_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_spiral_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Spiral', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_spiral_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_square_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Square', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_square_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_star_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Star', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_star_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_triangle_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Triangle', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_shape_triangle_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_cactus_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Cactus', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_cactus_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_chair_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Chair', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_chair_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_feather_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Feather', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_feather_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_glove_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Glove', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_glove_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_key_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Key', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_key_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_net_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Net', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card2_word_net_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_drinking_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Drinking', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_drinking_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_dropping_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Dropping', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_dropping_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_falling_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Falling', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_falling_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_running_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Running', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_running_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_sleeping_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Sleeping', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_sleeping_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_smoking_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Smoking', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_act_smoking_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_blue_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Blue', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_blue_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_brown_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Brown', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_brown_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_gray_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Gray', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_gray_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_pink_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Pink', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_pink_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_purple_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Purple', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_purple_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_red_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='Red', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_color_red_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_15_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='15', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_15_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_1936_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='1936', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_1936_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_42_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='42', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_42_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_7000_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='7000', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_7000_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_700_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='700', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_700_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_7_answer',
            field=models.CharField(max_length=200, null=True, verbose_name='7', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='comprehension_card3_number_7_points',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_address',
            field=models.TextField(max_length=500, null=True, verbose_name='g. "WHAT lS YOUR FULL ADDRESS?" (Number street, and city required. Probe for omitted elements).', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_been_here_before',
            field=models.TextField(max_length=500, null=True, verbose_name='b. "HAVE YOU EVER BEEN HERE BEFORE? or "HAVE I EVER TESTED YOU BEFORE?" ("Yes", "No" or other relevant response)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_cookie_jar',
            field=models.TextField(help_text='Present the "Cookie Theft" picture on card l. say, "Tell me everything you see going on in this picture." Point to neglected features of the picture and ask for elaboration if the patient\xb4s response is skimpier than his/her apparent potential.', max_length=500, null=True, verbose_name='i. Picture description', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_free_conversation',
            field=models.TextField(help_text='In order to elicit as much conversation as possible, it is suggested that the examiner start with a familiar topic, such as "WHAT KIND OF WORK WERE YOU DOING BEFORE YOU BECAME ILL?" or "TELL ME WHAT HAPPENED TO BRING YOU HERE." Encourage at least three minutes of conversation, if possible. Avoid questions that would elicit "Yes" or "No" responses.lf tape recording is not used,w rite verbatim as much as possible', max_length=500, null=True, verbose_name='h. Free conversation', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_help',
            field=models.TextField(max_length=500, null=True, verbose_name='c. "DO YOU THINK WE CAN HELP (HAVE HELPED YOU)?"( "I think so", "Maybe" or equivalent.)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_how_are_you',
            field=models.TextField(max_length=500, null=True, verbose_name='a. "HOW ARE YOU TODAY?" ("Okay," "Fine," or other appropriate response)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_leaving',
            field=models.TextField(max_length=500, null=True, verbose_name='d. "WHEN ARE YOU GOING TO BE LEAVING HERE?("I don\'t know", "Pretty soon", etc.)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_leaving_thought',
            field=models.TextField(max_length=500, null=True, verbose_name='e. "WE HOPE TO BE PRETTY SOON. WHAT DO YOU THINK?("I hope so", etc.)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='conversational_speech_name',
            field=models.TextField(max_length=500, null=True, verbose_name='f. "WHAT IS YOUR FULL NAME?"', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_drawing_left_hand',
            field=models.IntegerField(null=True, verbose_name='Draw or fill a glass of water', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_drawing_right_hand',
            field=models.IntegerField(null=True, verbose_name='Draw or fill a glass of water', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_historic_dominance',
            field=models.IntegerField(help_text='1: included / 2: absent', null=True, verbose_name='History of handedness (including data from other family members, eg: mother, father , brother, offspring)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_opening_box_left_hand',
            field=models.IntegerField(null=True, verbose_name='Open a box (holding the lid)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_opening_box_right_hand',
            field=models.IntegerField(null=True, verbose_name='Open a box (holding the lid)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_striking_match_left_hand',
            field=models.IntegerField(null=True, verbose_name='Strike a match', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_striking_match_right_hand',
            field=models.IntegerField(null=True, verbose_name='Strike a match', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_throwing_left_hand',
            field=models.IntegerField(null=True, verbose_name='Throw a ball', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_throwing_right_hand',
            field=models.IntegerField(null=True, verbose_name='Throw a ball', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_ashtray_left_hand',
            field=models.IntegerField(null=True, verbose_name='Use an ashtray', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_ashtray_right_hand',
            field=models.IntegerField(null=True, verbose_name='Use an ashtray', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_broom_left_hand',
            field=models.IntegerField(null=True, verbose_name='Use a broom (upper hand)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_broom_right_hand',
            field=models.IntegerField(null=True, verbose_name='Use a broom (upper hand)', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_fork_left_hand',
            field=models.IntegerField(null=True, verbose_name='Eat with a fork', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_fork_right_hand',
            field=models.IntegerField(null=True, verbose_name='Eat with a fork', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_spoon_left_hand',
            field=models.IntegerField(null=True, verbose_name='Use a spoon', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_spoon_right_hand',
            field=models.IntegerField(null=True, verbose_name='Use a spoon', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_toothbrush_left_hand',
            field=models.IntegerField(null=True, verbose_name='Use a toothbrush', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_using_toothbrush_right_hand',
            field=models.IntegerField(null=True, verbose_name='Use a toothbrush', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_writing_left_hand',
            field=models.IntegerField(null=True, verbose_name='Write or distribute a card deck', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='edinburg_handedness_writing_right_hand',
            field=models.IntegerField(null=True, verbose_name='Write or distribute a card deck', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='oral_agility_lips_purse',
            field=models.IntegerField(null=True, verbose_name='Purse lips, release', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='oral_agility_lips_retract',
            field=models.IntegerField(null=True, verbose_name='Retract lips, release', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='oral_agility_mouth_open',
            field=models.IntegerField(null=True, verbose_name='Open and close mouth', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='oral_agility_tongue_corner',
            field=models.IntegerField(null=True, verbose_name='Tongue to alternate corners of mouth', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='oral_agility_tongue_protude',
            field=models.IntegerField(null=True, verbose_name='Protrude and retract tongue', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='oral_agility_tongue_teeth',
            field=models.IntegerField(null=True, verbose_name='Tongue to upper and lower teeth', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_a',
            field=models.IntegerField(null=True, verbose_name='Mama, mama', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_b',
            field=models.IntegerField(null=True, verbose_name='Tip-top, tip-top', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_c',
            field=models.IntegerField(null=True, verbose_name='Fifty-fifty, fifty-fifty', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_d',
            field=models.IntegerField(null=True, verbose_name='Thanks, thanks', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_e',
            field=models.IntegerField(null=True, verbose_name='Huckleberry', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_f',
            field=models.IntegerField(null=True, verbose_name='Baseball player, baseball player', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='verbal_agility_g',
            field=models.IntegerField(null=True, verbose_name='Caterpillar', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_spherical_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to perform a spherical grasp by grasping a tennis ball. The tester may support the patient\u2019s arm but may not assist with the hand function required for the retrieval task. Test this grip against resistance by asking the patient to hold as you attempt to pull the ball out with a slight tug. <strong>Hold the ball and keep it steady</strong>', verbose_name='Fingers in abduction/flexion, thumb opposed, tennis ball', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia')]),
        ),
    ]
