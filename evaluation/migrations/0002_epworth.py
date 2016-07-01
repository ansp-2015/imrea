# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epworth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('obs', models.TextField(max_length=500, null=True, blank=True)),
                ('sitting_reading', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('watching_tv', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('sitting_inactive_public', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('car_passenger', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('lying_down', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('sitting_talking', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('sitting_quietly_lunch', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('car_traffic', models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing')])),
                ('patient', models.ForeignKey(verbose_name='Patient', to='evaluation.Patient')),
                ('period', models.ForeignKey(verbose_name='Period', to='evaluation.Period')),
            ],
            options={
                'verbose_name': 'Epworth Sleepiness',
                'verbose_name_plural': 'Epwort Sleepiness',
            },
        ),
    ]
