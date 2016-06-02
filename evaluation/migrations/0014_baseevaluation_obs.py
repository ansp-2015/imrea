# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0013_auto_20160516_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseevaluation',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
