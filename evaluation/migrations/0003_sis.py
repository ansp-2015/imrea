# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_auto_20160415_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='SIS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('strength_arm', models.IntegerField(choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')])),
                ('strength_hand', models.IntegerField(choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')])),
                ('strength_leg', models.IntegerField(choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')])),
                ('strength_foot', models.IntegerField(choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')])),
                ('patient', models.ForeignKey(to='evaluation.Patient')),
            ],
        ),
    ]
