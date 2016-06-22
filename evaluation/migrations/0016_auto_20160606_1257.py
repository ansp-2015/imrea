# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0015_clin'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuglMeyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ue_reflex_activity_flex', models.IntegerField(help_text='Flexors: biceps and finger flexors', choices=[(0, 'None'), (2, 'Can be elicited')])),
                ('ue_reflex_activity_ext', models.IntegerField(help_text='Extensors: triceps', choices=[(0, 'None'), (2, 'Can be elicited')])),
                ('ue_vol_mov_syn_flex_shoulder_retrac', models.IntegerField(help_text='Shoulder retraction', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_flex_shoulder_elev', models.IntegerField(help_text='Shoulder elevation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_flex_shoulder_abd', models.IntegerField(help_text='Shoulder abduction (90)', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_flex_shoulder_rot', models.IntegerField(help_text='Shoulder external rotation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_flex_elbow_flex', models.IntegerField(help_text='Elbow flexion', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_flex_forearm_sup', models.IntegerField(help_text='Forearm supination', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_flex_obs', models.TextField(max_length=500, null=True, blank=True)),
                ('ue_vol_mov_syn_ext_shoulder', models.IntegerField(help_text='shoulder adduction / internal rotation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_ext_elbow', models.IntegerField(help_text='elbow extension', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_ext_forearm', models.IntegerField(help_text='forearm pronation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_syn_ext_obs', models.TextField(max_length=500, null=True, blank=True)),
                ('vol_mov_mix_hand_spine', models.IntegerField(help_text='Hand to lumbar spine', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('vol_mov_mix_shoulder_flex', models.IntegerField(help_text='Shoulder flexion 0-90 elbow at 0 pronation-supination 0', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('vol_mov_mix_pron_sup', models.IntegerField(help_text='Pronation-supination elbow at 90 shoulder at 0', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_no_syn_shoulder_abd', models.IntegerField(help_text='Shoulder abduction 0 - 90 elbow at 0 forearm pronated', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_no_syn_shoulder_flex', models.IntegerField(help_text='Shoulder flexion 90- 180 elbow at 0pronation-supination 0', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_vol_mov_no_syn_pron_sup', models.IntegerField(help_text='Pronation/supinationelbow at 0 shoulder at 30-90 flexion', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_normal_reflex_activity', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_normal_reflex_obs', models.TextField(max_length=500, null=True, blank=True)),
                ('ue_wrist_stab_elbow_90', models.IntegerField(help_text='Stability at 15 dorsiflexion elbow at 90, forearm pronated shoulder at 0', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_wrist_flex_elbow_90', models.IntegerField(help_text='Repeated dorsifexion / volar flexion elbow at 90, forearm pronated shoulder at 0, slight finger flexion', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_wrist_stab_elbow_0', models.IntegerField(help_text='Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_wrist_flex_elbow_0', models.IntegerField(help_text='Repeated dorsifexion / volar flexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_wrist_circumduction', models.IntegerField(help_text='Circumduction', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_mass_flex', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_mass_ext', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_flex_pip_dip', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_thumb_adduction', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_thumb_opposition', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_cylinder_grip', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_hand_spherical_grip', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_coord_speed_tremor', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_coord_speed_dysmetria', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('ue_coord_speed_time', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_reflex_activity_achilles', models.IntegerField(choices=[(0, 'None'), (2, 'Full')])),
                ('le_reflex_activity_pattelar', models.IntegerField(choices=[(0, 'None'), (2, 'Full')])),
                ('le_reflex_activity_achilles_pattelar', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_hip_flexion', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_knee_flexion', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_ankle_dorsiflexion', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_hip_extension', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_hip_adduction', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_knee_extension', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_syn_ankle_flexion', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_mix_syn_knee', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_mix_syn_ankle', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_no_syn_knee', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_vol_mov_no_syn_ankle', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_coord_speed_tremor', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_coord_speed_dysmetria', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
                ('le_coord_speed_time', models.IntegerField(choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')])),
            ],
        ),
        migrations.AlterField(
            model_name='baseevaluation',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Last update'),
        ),
    ]
