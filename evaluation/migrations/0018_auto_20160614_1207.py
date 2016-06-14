# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0017_auto_20160613_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='had',
            name='book',
            field=models.IntegerField(verbose_name='I can enjoy a good book or radio or TV program', choices=[(3, 'Very seldom'), (2, 'Not often'), (1, 'Sometimes'), (0, 'Often')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='butterflies',
            field=models.IntegerField(verbose_name="I get a sort of frightened feeling like 'butterflies' in the stomach", choices=[(3, 'Very Often'), (2, 'Quite Often'), (1, 'Occasionally'), (0, 'Not at all')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='ease',
            field=models.IntegerField(verbose_name='I can sit at ease and feel relaxed', choices=[(3, 'Not at all'), (2, 'Not Often'), (1, 'Usually'), (0, 'Definitely')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='forward',
            field=models.IntegerField(verbose_name='I look forward with enjoyment to things', choices=[(3, 'Hardly at all'), (2, 'Definitely less than I used to'), (1, 'Rather less than I used to'), (0, 'As much as I ever did')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='frightened',
            field=models.IntegerField(verbose_name='I get a sort of frightened feeling as if something awful is about to happen', choices=[(3, 'Very definitely and quite badly'), (2, 'Yes, but not too badly'), (1, "A little, but it doesn't worry me"), (0, 'Not at all')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='laugh',
            field=models.IntegerField(verbose_name='I can laugh and see the funny side of things', choices=[(3, 'Not at all'), (2, 'Definitely not so much now'), (1, 'Not quite so much now'), (0, 'As much as I always could')]),
        ),
    ]
