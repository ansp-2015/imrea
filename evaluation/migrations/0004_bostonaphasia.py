# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_sis'),
    ]

    operations = [
        migrations.CreateModel(
            name='BostonAphasia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('write_or_distribute_card_deck_left_hand', models.IntegerField()),
                ('write_or_distribute_card_deck_right_hand', models.IntegerField()),
                ('patient', models.ForeignKey(to='evaluation.Patient')),
            ],
        ),
    ]
