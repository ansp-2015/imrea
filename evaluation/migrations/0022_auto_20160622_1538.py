# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0021_auto_20160621_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseevaluation',
            old_name='date',
            new_name='last_update',
        ),
        migrations.AlterField(
            model_name='fim',
            name='baseevaluation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_0',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho at\xe9 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Mant\xe9m 15\xb0 dorsiflex\xe3o contra resist\xeancia')]),
        ),
    ]
