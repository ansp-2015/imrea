# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KVIQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient', models.CharField(max_length=50)),
                ('visual_images', models.IntegerField(choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image')])),
                ('cine_images', models.IntegerField(choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation')])),
            ],
        ),
    ]
