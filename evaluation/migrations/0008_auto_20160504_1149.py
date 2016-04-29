# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0007_fim'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bostonaphasia',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='eeg',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='fim',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='kviq',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='sis',
            options={'ordering': ['patient']},
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_stairs',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_wheelchair',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_bathing',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_lower_body',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_upper_body',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_eating',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_grooming',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_toileting',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bladder_mgt',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bowel_mgt',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_shower',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_toilet',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_wheelchair',
            field=models.IntegerField(choices=[(7, b'7'), (6, b'6'), (5, b'5'), (4, b'4'), (3, b'3'), (2, b'2'), (1, b'1')]),
        ),
    ]
