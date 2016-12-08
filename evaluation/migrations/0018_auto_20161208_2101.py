# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0017_auto_20161129_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bostonaphasiarecallwrittensymbols',
            name='serial_writing_numbers_score',
        ),
        migrations.AddField(
            model_name='moca',
            name='total_twelve_year_old',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Less than 12 yr edu', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='bostonaphasiasymbolworddisc',
            name='symbol_word_card8_a_score',
            field=models.IntegerField(null=True, verbose_name='No', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasiasymbolworddisc',
            name='symbol_word_card8_d_score',
            field=models.IntegerField(null=True, verbose_name='Aro', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasiasymbolworddisc',
            name='symbol_word_card9_a_score',
            field=models.IntegerField(null=True, verbose_name='flor', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasiasymbolworddisc',
            name='symbol_word_card9_c_score',
            field=models.IntegerField(null=True, verbose_name='mas', blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasiasymbolworddisc',
            name='symbol_word_card9_e_score',
            field=models.IntegerField(null=True, verbose_name='par', blank=True),
        ),
        migrations.AlterField(
            model_name='moca',
            name='abstraction_1',
            field=models.PositiveIntegerField(help_text='Similarity between train - bicycle', verbose_name='Abstraction 1', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='abstraction_2',
            field=models.PositiveIntegerField(help_text='Similarity between watch - ruler', verbose_name='Abstraction 2', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='backward_digit_span',
            field=models.PositiveIntegerField(help_text='Subject has to repeat them in the backward order: 7 - 4 - 2', verbose_name='Backward digit span', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='forward_digit_span',
            field=models.PositiveIntegerField(help_text='Subject has to repeat them in the forward order: 2 - 1 - 8 - 5 - 4', verbose_name='Forward digit span', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='repeat_1',
            field=models.PositiveIntegerField(help_text='Repeat: I only know that John is the one to help today.', verbose_name='Repeat 1', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='repeat_2',
            field=models.PositiveIntegerField(help_text='Repeat: The cat always hid under the couch when dogs were in the room.', verbose_name='Repeat 2', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='verbal_fluency',
            field=models.PositiveIntegerField(help_text='Fluency / Name maximum number of words in one minute that begin with the letter F. (N >= 11)', verbose_name='Verbal Fluency', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='vigilance',
            field=models.PositiveIntegerField(help_text='Read list of letters. The subject must tap with his hand at each letter A. No points if >= 2 errors. (F B A C M N A A J K L B A F A K D E A A A J A M O F A A B)', verbose_name='Vigilance', choices=[(0, b'0'), (1, b'1')]),
        ),
    ]
