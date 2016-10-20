# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0012_auto_20160921_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='FTT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('obs', models.TextField(max_length=500, null=True, blank=True)),
                ('paretic_hand_first', models.IntegerField(verbose_name='First')),
                ('healthy_hand_first', models.IntegerField()),
                ('paretic_hand_second', models.IntegerField(verbose_name='Second')),
                ('healthy_hand_second', models.IntegerField()),
                ('paretic_hand_third', models.IntegerField(verbose_name='Third')),
                ('healthy_hand_third', models.IntegerField()),
                ('patient', models.ForeignKey(verbose_name='Patient', to='evaluation.Patient')),
                ('period', models.ForeignKey(verbose_name='Period', to='evaluation.Period')),
            ],
            options={
                'verbose_name': 'FTT - Finger Tapping Test',
                'verbose_name_plural': 'FTT - Finger Tapping Tests',
            },
        ),
        migrations.AlterField(
            model_name='jthft',
            name='healthy_hand_first',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='jthft',
            name='paretic_hand_first',
            field=models.DurationField(verbose_name='First'),
        ),
        migrations.AlterField(
            model_name='jthft',
            name='paretic_hand_second',
            field=models.DurationField(verbose_name='Second'),
        ),
        migrations.AlterField(
            model_name='jthft',
            name='paretic_hand_third',
            field=models.DurationField(verbose_name='Third'),
        ),
    ]
