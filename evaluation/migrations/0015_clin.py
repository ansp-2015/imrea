# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0014_baseevaluation_obs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clin',
            fields=[
                ('baseevaluation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation')),
                ('neglect_1a', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_1b', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_1c', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_1d', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_2a', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_2b', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_2c', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_2d', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_3a', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_3b', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_3c', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_3d', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_4a', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_4b', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_4c', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
                ('neglect_4d', models.IntegerField(choices=[(1, 'Yes'), (2, 'No')])),
            ],
            bases=('evaluation.baseevaluation',),
        ),
    ]
