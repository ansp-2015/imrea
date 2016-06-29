# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0019_auto_20160615_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hamilton',
            old_name='weight',
            new_name='weight_weekly',
        ),
        migrations.AddField(
            model_name='hamilton',
            name='weight_history',
            field=models.IntegerField(default=0, verbose_name='loss of weight', choices=[(0, 'No weight loss'), (1, 'Probable weight loss associated with present illness'), (2, 'Definite (according to patient) weight loss'), (3, 'Not assessed')]),
            preserve_default=False,
        ),
    ]
