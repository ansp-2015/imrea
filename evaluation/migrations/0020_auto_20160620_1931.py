# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0019_auto_20160616_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuglmeyer',
            old_name='vol_mov_mix_hand_spine',
            new_name='ue_vol_mov_mix_hand_spine',
        ),
        migrations.RenameField(
            model_name='fuglmeyer',
            old_name='vol_mov_mix_pron_sup',
            new_name='ue_vol_mov_mix_pron_sup',
        ),
        migrations.RenameField(
            model_name='fuglmeyer',
            old_name='vol_mov_mix_shoulder_flex',
            new_name='ue_vol_mov_mix_shoulder_flex',
        ),
    ]
