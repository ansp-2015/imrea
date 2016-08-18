# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0006_auto_20160805_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='nihss',
            name='dysarthria_un_explanation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nihss',
            name='limb_ataxia_un_explanation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nihss',
            name='motor_arm_left_un_explanation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nihss',
            name='motor_arm_right_un_explanation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nihss',
            name='motor_leg_left_un_explanation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='nihss',
            name='motor_leg_right_un_explanation',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_arm_left',
            field=models.IntegerField(verbose_name='5. Motor arm', choices=[(0, 'No drift; limb holds 90 (or 45) degrees for full 10 seconds.'), (1, 'Drift; limb holds 90 (or 45) degrees, but drifts down before full 10 seconds; does not hit bed or other support.'), (2, 'Some effort against gravity; limb cannot get to or maintain (if cued) 90 (or 45) degrees, drifts down to bed, but has some effort against gravity.'), (3, 'No effort against gravity; limb falls.'), (4, 'No movement')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_arm_right',
            field=models.IntegerField(choices=[(0, 'No drift; limb holds 90 (or 45) degrees for full 10 seconds.'), (1, 'Drift; limb holds 90 (or 45) degrees, but drifts down before full 10 seconds; does not hit bed or other support.'), (2, 'Some effort against gravity; limb cannot get to or maintain (if cued) 90 (or 45) degrees, drifts down to bed, but has some effort against gravity.'), (3, 'No effort against gravity; limb falls.'), (4, 'No movement')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_leg_left',
            field=models.IntegerField(verbose_name='6. Motor leg', choices=[(0, 'No drift; leg holds 30-degree position for full 5 seconds.'), (1, 'Drift; leg falls by the end of the 5-second period but does not hit bed.'), (2, 'Some effort against gravity; leg falls to bed by 5 seconds, but has some effort against gravity.'), (3, 'No effort against gravity; leg falls to bed immediately.'), (4, 'No movement.')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_leg_right',
            field=models.IntegerField(choices=[(0, 'No drift; leg holds 30-degree position for full 5 seconds.'), (1, 'Drift; leg falls by the end of the 5-second period but does not hit bed.'), (2, 'Some effort against gravity; leg falls to bed by 5 seconds, but has some effort against gravity.'), (3, 'No effort against gravity; leg falls to bed immediately.'), (4, 'No movement.')]),
        ),
    ]
