# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0006_eeg'),
    ]

    operations = [
        migrations.CreateModel(
            name='FIM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('self_care_eating', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('self_care_grooming', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('self_care_bathing', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('self_care_dressing_upper_body', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('self_care_dressing_lower_body', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('self_care_toileting', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('sphincter_bladder_mgt', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('sphincter_bowel_mgt', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('transfer_wheelchair', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('transfer_toilet', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('transfer_shower', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('locomotion_wheelchair', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('locomotion_stairs', models.IntegerField(choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')])),
                ('patient', models.ForeignKey(to='evaluation.Patient')),
            ],
        ),
    ]
