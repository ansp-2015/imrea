# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0011_auto_20160509_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='eeg',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='fim',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='kviq',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last update'),
        ),
        migrations.AlterField(
            model_name='period',
            name='parent',
            field=models.ForeignKey(related_name='child', verbose_name='Parent', blank=True, to='evaluation.Period', null=True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Last update'),
        ),
    ]
