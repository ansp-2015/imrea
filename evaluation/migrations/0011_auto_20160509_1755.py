# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0010_auto_20160505_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fim',
            options={'verbose_name': 'FIM', 'verbose_name_plural': 'FIMs'},
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_stairs',
            field=models.IntegerField(verbose_name='Locomotion stairs', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_wheelchair',
            field=models.IntegerField(verbose_name='Locomotion walking/wheelchair', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_bathing',
            field=models.IntegerField(verbose_name='Bathing/showering', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_lower_body',
            field=models.IntegerField(verbose_name='Dressing lower body', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_upper_body',
            field=models.IntegerField(verbose_name='Dressing upper body', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_eating',
            field=models.IntegerField(verbose_name='Eating', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_grooming',
            field=models.IntegerField(verbose_name='Grooming', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_toileting',
            field=models.IntegerField(verbose_name='Toileting', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bladder_mgt',
            field=models.IntegerField(verbose_name='Bladder management', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bowel_mgt',
            field=models.IntegerField(verbose_name='Bowel management', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_shower',
            field=models.IntegerField(verbose_name='Transfers bathtub/shower', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_toilet',
            field=models.IntegerField(verbose_name='Transfers toilet', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_wheelchair',
            field=models.IntegerField(verbose_name='Transfers bed/chair/wheelchair', choices=[(7, 'Complete independence'), (6, 'Modified independence'), (5, 'Supervision'), (4, 'Minimal assistance'), (3, 'Moderate assistance'), (2, 'Maximal assistance'), (1, 'Total assistance')]),
        ),
    ]
