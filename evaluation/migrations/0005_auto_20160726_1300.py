# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import evaluation.models.eeg


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_auto_20160705_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['name'], 'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Age', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='conducting_source',
            field=models.CharField(max_length=100, null=True, verbose_name='Conducting source', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='family_income',
            field=models.IntegerField(null=True, verbose_name='Family income', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='family_income_average',
            field=models.IntegerField(null=True, verbose_name='Average family income', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='fammily_composition',
            field=models.CharField(max_length=255, null=True, verbose_name='Family composition', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='fammily_ref_home',
            field=models.CharField(max_length=100, null=True, verbose_name='Family member reference at home', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='fammily_ref_therapy',
            field=models.CharField(max_length=100, null=True, verbose_name='Family member reference for therapy frequency', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=100, null=True, verbose_name='Gender', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Marital status', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='occupation',
            field=models.CharField(max_length=100, null=True, verbose_name='Occupation/work', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='origin_city',
            field=models.CharField(max_length=100, null=True, verbose_name='City of origin', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='profession',
            field=models.CharField(max_length=100, null=True, verbose_name='Profession', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='quantity_ppl_home',
            field=models.IntegerField(null=True, verbose_name='Number of people at home', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='schooling_level',
            field=models.CharField(max_length=100, null=True, verbose_name='Schooling level', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='social_insurance_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Social insurance status', blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='transportation_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Social insurance status', blank=True),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1a',
            field=models.IntegerField(verbose_name='Neglect 1a', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1b',
            field=models.IntegerField(verbose_name='Neglect 1b', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1c',
            field=models.IntegerField(verbose_name='Neglect 1c', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1d',
            field=models.IntegerField(verbose_name='Neglect 1d', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2a',
            field=models.IntegerField(verbose_name='Neglect 2a', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2b',
            field=models.IntegerField(verbose_name='Neglect 2b', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2c',
            field=models.IntegerField(verbose_name='Neglect 2c', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2d',
            field=models.IntegerField(verbose_name='Neglect 2d', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3a',
            field=models.IntegerField(verbose_name='Neglect 3a', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3b',
            field=models.IntegerField(verbose_name='Neglect 3b', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3c',
            field=models.IntegerField(verbose_name='Neglect 3c', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3d',
            field=models.IntegerField(verbose_name='Neglect 3d', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4a',
            field=models.IntegerField(verbose_name='Neglect 4a', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4b',
            field=models.IntegerField(verbose_name='Neglect 4b', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4c',
            field=models.IntegerField(verbose_name='Neglect 4c', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4d',
            field=models.IntegerField(verbose_name='Neglect 4d', choices=[(1, 'Yes'), (2, 'No')]),
        ),
        migrations.AlterField(
            model_name='eeg',
            name='eegfile',
            field=models.FileField(upload_to=evaluation.models.eeg.user_directory_path, verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='anxiety_psychic',
            field=models.IntegerField(verbose_name='Anxiety: psychic', choices=[(0, 'No difficulty'), (1, 'Subjective tension and irritability'), (2, 'Worrying about minor matters'), (3, 'Apprehensive attitude apparent in face or speech'), (4, 'Fears expressed without questioning')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='anxiety_somatic',
            field=models.IntegerField(verbose_name='Anxiety: somatic', choices=[(0, 'Absent'), (1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Incapacitating')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='weight_weekly',
            field=models.IntegerField(verbose_name='loss of weight', choices=[(0, 'No weight loss'), (1, 'Probable weight loss associated with present illness (>500g/week)'), (2, 'Definite weight loss(>1kg/week)'), (3, 'Not assessed')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(null=True, verbose_name='Date of birth', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
