# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0009_auto_20160505_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kviq',
            old_name='cine_images',
            new_name='elbow_dom_cine_images',
        ),
        migrations.RenameField(
            model_name='kviq',
            old_name='visual_images',
            new_name='elbow_dom_visual_images',
        ),
        migrations.AddField(
            model_name='kviq',
            name='dominant_limb',
            field=models.IntegerField(default=1, choices=[(0, 'Left'), (1, 'Right')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='elbow_not_dom_cine_images',
            field=models.IntegerField(default=0, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='elbow_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_rotation_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_rotation_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_rotation_not_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_rotation_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_tapping_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_tapping_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_tapping_not_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='foot_tapping_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='hip_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='hip_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='hip_not_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='hip_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='knee_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='knee_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='knee_not_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='knee_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='neck_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='neck_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='shoulder_elevation_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='shoulder_elevation_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='shoulder_flexion_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='shoulder_flexion_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='shoulder_flexion_not_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='shoulder_flexion_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='thumb_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='thumb_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='thumb_not_dom_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='thumb_not_dom_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='trunk_cine_images',
            field=models.IntegerField(default=1, choices=[(5, 'As intense as performing the action'), (4, 'Intense'), (3, 'Moderately intense'), (2, 'Slightly intense'), (1, 'No sensation'), (-10000, 'NT')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='trunk_visual_images',
            field=models.IntegerField(default=1, choices=[(5, 'Image as clear as seeing'), (4, 'Clear image'), (3, 'Moderately clear image'), (2, 'Blurred image'), (1, 'No image'), (-10000, 'NT')]),
            preserve_default=False,
        ),
    ]
