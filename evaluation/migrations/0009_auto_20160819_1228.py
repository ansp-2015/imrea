# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0008_vas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vas',
            name='anxiety',
            field=models.FloatField(verbose_name='Anxiety'),
        ),
        migrations.AlterField(
            model_name='vas',
            name='pain',
            field=models.FloatField(verbose_name='Pain'),
        ),
    ]
