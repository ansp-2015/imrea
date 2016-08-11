# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_auto_20160726_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nihss',
            old_name='facil_palsy',
            new_name='facial_palsy',
        ),
        migrations.AlterField(
            model_name='nihss',
            name='extinction',
            field=models.IntegerField(verbose_name='11. Extinction and Inattention (formerly Neglect)', choices=[(0, 'No abnormality.'), (1, 'Visual, tactile, auditory, spatial, or personal inattention or extinction to bilateral simultaneous stimulation in one of the sensory modalities.'), (2, 'Profound hemi-inattention or extinction to more than one modality; does not recognize own hand or orients to only one side of space. ')]),
        ),
    ]
