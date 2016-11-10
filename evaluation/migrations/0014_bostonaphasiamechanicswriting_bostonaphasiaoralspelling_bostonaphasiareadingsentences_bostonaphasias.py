# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0013_auto_20161019_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='BostonAphasiaMechanicsWriting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mechanics_writing_score', models.IntegerField(null=True, blank=True)),
                ('bostonAphasia', models.OneToOneField(to='evaluation.BostonAphasia')),
            ],
        ),
        migrations.CreateModel(
            name='BostonAphasiaOralSpelling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oral_spelling_a_score', models.IntegerField(null=True, verbose_name='Y-E-S', blank=True)),
                ('oral_spelling_b_score', models.IntegerField(null=True, verbose_name='B-R-O-W-N', blank=True)),
                ('oral_spelling_c_score', models.IntegerField(null=True, verbose_name='M-A-N', blank=True)),
                ('oral_spelling_d_score', models.IntegerField(null=True, verbose_name='E-L-B-O-W', blank=True)),
                ('oral_spelling_e_score', models.IntegerField(null=True, verbose_name='W-O-M-A-N', blank=True)),
                ('oral_spelling_f_score', models.IntegerField(null=True, verbose_name='F-I-F-T-E-E-N', blank=True)),
                ('oral_spelling_g_score', models.IntegerField(null=True, verbose_name='W-I-P', blank=True)),
                ('oral_spelling_h_score', models.IntegerField(null=True, verbose_name='E-X-A-C-T', blank=True)),
                ('bostonAphasia', models.OneToOneField(to='evaluation.BostonAphasia')),
            ],
        ),
        migrations.CreateModel(
            name='BostonAphasiaReadingSentences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reading_sentences_dog_score', models.IntegerField(null=True, verbose_name='1. A dog can', blank=True)),
                ('reading_sentences_mother_score', models.IntegerField(null=True, verbose_name='2. A mother has a', blank=True)),
                ('reading_sentences_haircut_score', models.IntegerField(null=True, verbose_name='3. Mr. Jones gives haircuts and shampoos. He is a', blank=True)),
                ('reading_sentences_bird_score', models.IntegerField(null=True, verbose_name='4. Many birds come back in the summer. They build', blank=True)),
                ('reading_sentences_school_score', models.IntegerField(null=True, verbose_name='5. Schools and roads cost money. We all pay for them through', blank=True)),
                ('reading_sentences_artist_score', models.IntegerField(null=True, verbose_name='6. Artists are people who make beautiful paintings or statues. Another kind of artist is a', blank=True)),
                ('reading_sentences_aluminum_score', models.IntegerField(null=True, verbose_name='7. Aluminum was once very costly to refine. Now, electricity has solved the refining problem, and aluminum has become', blank=True)),
                ('reading_sentences_sanitation_score', models.IntegerField(null=True, verbose_name='8. The connection between sanitation and disease became clear when pasteur showed that food would not decay if germs were killed by heat and then sealed out. Sterilization by heat is a result of', blank=True)),
                ('reading_sentences_civil_service_score', models.IntegerField(null=True, verbose_name='9. Favoritism used to be the rule in civil service and many jobs paid more than they were worth. Civil service reform has resulted in classifying positions according to their duties and responsibilities. The aim of civil service classification is to', blank=True)),
                ('reading_sentences_government_score', models.IntegerField(null=True, verbose_name='10. In the early days of this country, the functions of government were few in number. Most of these functions were carried out by local town and contry officials, while centralized authority was distrusted. The growth of industry and of the cities has so changed the situation that the farmer of today is concerned with', blank=True)),
                ('bostonAphasia', models.OneToOneField(to='evaluation.BostonAphasia')),
            ],
        ),
        migrations.CreateModel(
            name='BostonAphasiaSymbolWordDisc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol_word_card8_a_score', models.IntegerField(null=True, verbose_name=b'In', blank=True)),
                ('symbol_word_card8_b_score', models.IntegerField(null=True, verbose_name=b'J', blank=True)),
                ('symbol_word_card8_c_score', models.IntegerField(null=True, verbose_name=b'H', blank=True)),
                ('symbol_word_card8_d_score', models.IntegerField(null=True, verbose_name=b'salt', blank=True)),
                ('symbol_word_card8_e_score', models.IntegerField(null=True, verbose_name=b'R', blank=True)),
                ('symbol_word_card9_a_score', models.IntegerField(null=True, verbose_name=b'flower', blank=True)),
                ('symbol_word_card9_b_score', models.IntegerField(null=True, verbose_name=b'B', blank=True)),
                ('symbol_word_card9_c_score', models.IntegerField(null=True, verbose_name=b'lead', blank=True)),
                ('symbol_word_card9_d_score', models.IntegerField(null=True, verbose_name=b'F', blank=True)),
                ('symbol_word_card9_e_score', models.IntegerField(null=True, verbose_name=b'plus', blank=True)),
                ('bostonAphasia', models.OneToOneField(to='evaluation.BostonAphasia')),
            ],
        ),
        migrations.CreateModel(
            name='BostonAphasiaWordPictureMatching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_picture_chair_score', models.IntegerField(null=True, verbose_name='chair', blank=True)),
                ('word_picture_circle_score', models.IntegerField(null=True, verbose_name='circle', blank=True)),
                ('word_picture_hammock_score', models.IntegerField(null=True, verbose_name='hammock', blank=True)),
                ('word_picture_triangle_score', models.IntegerField(null=True, verbose_name='triangle', blank=True)),
                ('word_picture_fifteen_score', models.IntegerField(null=True, verbose_name='fifteen', blank=True)),
                ('word_picture_purple_score', models.IntegerField(null=True, verbose_name='purple', blank=True)),
                ('word_picture_seven_t_o_score', models.IntegerField(null=True, verbose_name='seven-twenty-one', blank=True)),
                ('word_picture_dripping_score', models.IntegerField(null=True, verbose_name='dripping', blank=True)),
                ('word_picture_brown_score', models.IntegerField(null=True, verbose_name='brown', blank=True)),
                ('word_picture_smoking_score', models.IntegerField(null=True, verbose_name='smoking', blank=True)),
                ('bostonAphasia', models.OneToOneField(to='evaluation.BostonAphasia')),
            ],
        ),
        migrations.CreateModel(
            name='BostonAphasiaWordRecognition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_recognition_a_score', models.IntegerField(null=True, verbose_name='boat', blank=True)),
                ('word_recognition_b_score', models.IntegerField(null=True, verbose_name='frog', blank=True)),
                ('word_recognition_c_score', models.IntegerField(null=True, verbose_name='hammock', blank=True)),
                ('word_recognition_d_score', models.IntegerField(null=True, verbose_name='yours', blank=True)),
                ('word_recognition_e_score', models.IntegerField(null=True, verbose_name='mass', blank=True)),
                ('word_recognition_f_score', models.IntegerField(null=True, verbose_name='key', blank=True)),
                ('word_recognition_g_score', models.IntegerField(null=True, verbose_name='sum', blank=True)),
                ('word_recognition_h_score', models.IntegerField(null=True, verbose_name='want', blank=True)),
                ('bostonAphasia', models.OneToOneField(to='evaluation.BostonAphasia')),
            ],
        ),
        migrations.CreateModel(
            name='VonFrey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('obs', models.TextField(max_length=500, null=True, blank=True)),
                ('sensibility1_forearm_right', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility1_forearm_left', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility1_thenar_right', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility1_thenar_left', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility2_forearm_right', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility2_forearm_left', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility2_thenar_right', models.DecimalField(max_digits=5, decimal_places=2)),
                ('sensibility2_thenar_left', models.DecimalField(max_digits=5, decimal_places=2)),
                ('algometer1_forearm_right', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer1_forearm_left', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer1_thenar_right', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer1_thenar_left', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer2_forearm_right', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer2_forearm_left', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer2_thenar_right', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer2_thenar_left', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer3_forearm_right', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer3_forearm_left', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer3_thenar_right', models.DecimalField(max_digits=5, decimal_places=1)),
                ('algometer3_thenar_left', models.DecimalField(max_digits=5, decimal_places=1)),
                ('patient', models.ForeignKey(verbose_name='Patient', to='evaluation.Patient')),
                ('period', models.ForeignKey(verbose_name='Period', to='evaluation.Period')),
            ],
            options={
                'verbose_name': 'Von Frey - Algometer',
                'verbose_name_plural': 'Von Frey = Algometer',
            },
        ),
    ]
