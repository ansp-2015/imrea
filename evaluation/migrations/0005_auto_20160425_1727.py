# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_bostonaphasia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bostonaphasia',
            name='write_or_distribute_card_deck_left_hand',
            field=models.IntegerField(verbose_name='Write or distribute a card deck'),
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='write_or_distribute_card_deck_right_hand',
            field=models.IntegerField(verbose_name='Write or distribute a card deck'),
        ),
        migrations.AlterField(
            model_name='kviq',
            name='cine_images',
            field=models.IntegerField(choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='kviq',
            name='visual_images',
            field=models.IntegerField(choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
        ),
    ]
