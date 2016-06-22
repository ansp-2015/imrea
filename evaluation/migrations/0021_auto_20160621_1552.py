# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0020_auto_20160620_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_total_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='ue_total_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
    ]
