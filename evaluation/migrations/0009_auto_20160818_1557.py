# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0008_auto_20160811_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_alphabet',
            field=models.IntegerField(null=True, verbose_name='4. Alphabet:', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_alphabet_note',
            field=models.TextField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_counting_21',
            field=models.IntegerField(null=True, verbose_name='3. Counting to 21:', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_counting_21_note',
            field=models.TextField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_days_week',
            field=models.IntegerField(null=True, verbose_name='1. Days of the week:', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_days_week_note',
            field=models.TextField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_months_year',
            field=models.IntegerField(null=True, verbose_name='2. Months of the year:', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='automzatized_months_year_note',
            field=models.TextField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='reciting_note',
            field=models.TextField(help_text='Jack and Jill (went)...', max_length=250, null=True, verbose_name='Reciting', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='reciting_score',
            field=models.IntegerField(help_text='Jack and Jill (went)...', null=True, verbose_name='Reciting', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_a_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_a_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_a_score',
            field=models.IntegerField(null=True, verbose_name='a. You know how', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_b_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_b_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_b_score',
            field=models.IntegerField(null=True, verbose_name='b. Down to earth.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_c_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_c_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_c_score',
            field=models.IntegerField(null=True, verbose_name='c. I got home from work.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_d_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_d_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_d_score',
            field=models.IntegerField(null=True, verbose_name='d. You should not tell her.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_e_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_e_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_e_score',
            field=models.IntegerField(null=True, verbose_name='e. Go ahead and do it if possible', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_f_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_f_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_f_score',
            field=models.IntegerField(null=True, verbose_name='f. Near the table in the dining room.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_g_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_g_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_g_score',
            field=models.IntegerField(null=True, verbose_name='g. They heard him speak on the radio last night.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_h_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_h_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_high_h_score',
            field=models.IntegerField(null=True, verbose_name='h. I stopped at his front door and rang the bell.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_a_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_a_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_a_score',
            field=models.IntegerField(null=True, verbose_name='a. The vat leaks.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_b_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_b_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_b_score',
            field=models.IntegerField(null=True, verbose_name='b. limes are sour.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_c_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_c_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_c_score',
            field=models.IntegerField(null=True, verbose_name='c. The spy fled to Greece.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_d_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_d_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_d_score',
            field=models.IntegerField(null=True, verbose_name='d. Pry the tin lid off.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_e_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_e_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_e_score',
            field=models.IntegerField(null=True, verbose_name='e. The Chinese fan had a rare emerald.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_f_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_f_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_f_score',
            field=models.IntegerField(null=True, verbose_name='f. The barn swallow captured a plump worm.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_g_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_g_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_g_score',
            field=models.IntegerField(null=True, verbose_name="g. The lawyer's closing argument convinced him.", blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_h_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_h_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_phrases_low_h_score',
            field=models.IntegerField(null=True, verbose_name='h. The phantom soared across the foggy heath.', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_1776_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_1776_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_1776_score',
            field=models.IntegerField(null=True, verbose_name='1776', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_1776_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_brown_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_brown_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_brown_score',
            field=models.IntegerField(null=True, verbose_name='Brown', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_brown_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_chair_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_chair_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_chair_score',
            field=models.IntegerField(null=True, verbose_name='Chair', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_chair_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_emphasize_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_emphasize_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_emphasize_score',
            field=models.IntegerField(null=True, verbose_name='Emphasize', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_emphasize_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_episcopal_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_episcopal_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_episcopal_score',
            field=models.IntegerField(null=True, verbose_name='Methodist Episcopal', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_episcopal_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_fifteen_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_fifteen_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_fifteen_score',
            field=models.IntegerField(null=True, verbose_name='Fifteen', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_fifteen_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_hammock_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_hammock_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_hammock_score',
            field=models.IntegerField(null=True, verbose_name='Hammock', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_hammock_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_purple_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_purple_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_purple_score',
            field=models.IntegerField(null=True, verbose_name='Purple', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_purple_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_w_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_w_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_w_score',
            field=models.IntegerField(null=True, verbose_name='W', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_w_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_what_articulation',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_what_paraphasia',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_what_score',
            field=models.IntegerField(null=True, verbose_name='What', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='repetition_words_what_transcription',
            field=models.TextField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='singing_note',
            field=models.TextField(help_text='After recitation have patient sing this or any othet song with which he is familiar', max_length=250, null=True, verbose_name='Singing', blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='singing_score',
            field=models.IntegerField(help_text='After recitation have patient sing this or any othet song with which he is familiar', null=True, verbose_name='Singing', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='command_close_fist',
            field=models.IntegerField(null=True, verbose_name='1. Make a "fist"', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='command_point_ceiling',
            field=models.IntegerField(null=True, verbose_name='2. Point to "the ceiling", then to "the floor"', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='command_put_pencil',
            field=models.IntegerField(null=True, verbose_name='3. Put "the pencil" on "top of the card", then "put it back in place"', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='command_put_watch',
            field=models.IntegerField(null=True, verbose_name='4. Put "the watch" on "the other side" of "the pencil" and "turn over the card"', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='command_touch_shoulder',
            field=models.IntegerField(null=True, verbose_name='5. Tap "each shoulder" "twice" with "two fingers", keeping your "eyes shut"', blank=True),
        ),
    ]
