# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0007_auto_20160815_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='VAS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('obs', models.TextField(max_length=500, null=True, blank=True)),
                ('side', models.IntegerField(verbose_name='More painful side', choices=[(0, 'Left'), (1, 'Right')])),
                ('pain', models.IntegerField(verbose_name='Pain')),
                ('anxiety', models.IntegerField(verbose_name='Anxiety')),
                ('patient', models.ForeignKey(verbose_name='Patient', to='evaluation.Patient')),
                ('period', models.ForeignKey(verbose_name='Period', to='evaluation.Period')),
            ],
            options={
                'verbose_name': 'VAS - Visual Analog Scale',
                'verbose_name_plural': 'VAS - Visual Analog Scales',
            },
        ),
    ]
