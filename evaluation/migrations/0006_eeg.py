# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import evaluation.models.eeg


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_auto_20160425_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eeg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eegtitle', models.CharField(max_length=250)),
                ('eegfile', models.FileField(upload_to=evaluation.models.eeg.user_directory_path)),
                ('patient', models.ForeignKey(to='evaluation.Patient')),
            ],
        ),
    ]
