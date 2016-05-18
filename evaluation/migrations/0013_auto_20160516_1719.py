# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_auto_20160510_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEvaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Last update')),
                ('patient', models.ForeignKey(verbose_name='Patient', to='evaluation.Patient')),
                ('period', models.ForeignKey(verbose_name='Period', to='evaluation.Period')),
            ],
            options={
                'ordering': ['patient'],
            },
        ),
        migrations.AlterModelOptions(
            name='bostonaphasia',
            options={},
        ),
        migrations.AlterModelOptions(
            name='eeg',
            options={},
        ),
        migrations.AlterModelOptions(
            name='kviq',
            options={},
        ),
        migrations.AlterModelOptions(
            name='sis',
            options={},
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='date',
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='id',
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='period',
        ),
        migrations.RemoveField(
            model_name='eeg',
            name='date',
        ),
        migrations.RemoveField(
            model_name='eeg',
            name='id',
        ),
        migrations.RemoveField(
            model_name='eeg',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='eeg',
            name='period',
        ),
        migrations.RemoveField(
            model_name='fim',
            name='date',
        ),
        migrations.RemoveField(
            model_name='fim',
            name='id',
        ),
        migrations.RemoveField(
            model_name='fim',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='fim',
            name='period',
        ),
        migrations.RemoveField(
            model_name='kviq',
            name='date',
        ),
        migrations.RemoveField(
            model_name='kviq',
            name='id',
        ),
        migrations.RemoveField(
            model_name='kviq',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='kviq',
            name='period',
        ),
        migrations.RemoveField(
            model_name='sis',
            name='date',
        ),
        migrations.RemoveField(
            model_name='sis',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sis',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='sis',
            name='period',
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_stairs',
            field=models.IntegerField(verbose_name='Locomotion stairs', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_wheelchair',
            field=models.IntegerField(verbose_name='Locomotion walking/wheelchair', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_bathing',
            field=models.IntegerField(verbose_name='Bathing/showering', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_lower_body',
            field=models.IntegerField(verbose_name='Dressing lower body', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_upper_body',
            field=models.IntegerField(verbose_name='Dressing upper body', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_eating',
            field=models.IntegerField(verbose_name='Eating', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_grooming',
            field=models.IntegerField(verbose_name='Grooming', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_toileting',
            field=models.IntegerField(verbose_name='Toileting', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bladder_mgt',
            field=models.IntegerField(verbose_name='Bladder management', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bowel_mgt',
            field=models.IntegerField(verbose_name='Bowel management', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_shower',
            field=models.IntegerField(verbose_name='Transfers bathtub/shower', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_toilet',
            field=models.IntegerField(verbose_name='Transfers toilet', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_wheelchair',
            field=models.IntegerField(verbose_name='Transfers bed/chair/wheelchair', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence')]),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='baseevaluation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),

        ),
        migrations.AddField(
            model_name='eeg',
            name='baseevaluation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),

        ),
        migrations.AddField(
            model_name='fim',
            name='baseevaluation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),

        ),
        migrations.AddField(
            model_name='kviq',
            name='baseevaluation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),

        ),
        migrations.AddField(
            model_name='sis',
            name='baseevaluation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),

        ),
    ]
