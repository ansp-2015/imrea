# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0015_auto_20161111_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerbalFluency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('obs', models.TextField(max_length=500, null=True, blank=True)),
                ('fas_words', models.TextField(verbose_name=b'')),
                ('fas_count', models.IntegerField(verbose_name='Word count')),
                ('fas_obs', models.TextField(verbose_name='Observation')),
                ('animals_words', models.TextField(verbose_name=b'')),
                ('animals_count', models.IntegerField(verbose_name='Word count')),
                ('animals_obs', models.TextField(verbose_name='Observation')),
            ],
            options={
                'verbose_name': 'Verbal Fluency Test',
                'verbose_name_plural': 'Verbal Fluency Tests',
            },
        ),
        migrations.AlterModelOptions(
            name='eegfile',
            options={'verbose_name': 'EEG File', 'verbose_name_plural': 'EEG Files'},
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Scoring Dysmetria', choices=[(0, 'Pronounced or unsystematic dysmetria'), (1, 'Slight or systematic dysmetria'), (2, 'No dysmetria')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_time',
            field=models.IntegerField(verbose_name='Scoring Speed', choices=[(0, 'Activity is more than 6 seconds longer than unaffected leg'), (1, ' 2-5.9 seconds longer than unaffected leg'), (2, 'less than 2 seconds difference')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_tremor',
            field=models.IntegerField(verbose_name='Scoring Tremor', choices=[(0, 'Marked tremor'), (1, 'Slight tremor'), (2, 'No tremor')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles',
            field=models.IntegerField(verbose_name='Achilles', choices=[(0, 'No reflex activity can be elicited'), (2, 'Reflex activity can be elicited')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles_pattelar',
            field=models.IntegerField(verbose_name='Achilles and patellar reflexes', choices=[(0, 'At least 2 of the 3 phasic reflexes are markedly hyperactive'), (1, 'One reflex is markedly hyperactive or at least 2 reflexes are lively'), (2, 'No more than one reflex is lively and none are hyperactive')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles_pattelar_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_pattelar',
            field=models.IntegerField(verbose_name='Patellar', choices=[(0, 'No reflex activity can be elicited'), (2, 'Reflex activity can be elicited')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_total_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion sitting', choices=[(0, 'No active motion'), (1, 'Incomplete active flexion'), (2, 'Normal dorsiflexion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion sitting', choices=[(0, 'No active motion'), (1, 'From slightly extended position, knee can be flexed but not beyond 90\xb0'), (2, 'Knee flexion beyond 90\xb0')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion standing', choices=[(0, 'No active motion'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion standing', choices=[(0, 'Knee cannot flex without hip flexion'), (1, 'Knee flexion begins without hip flexion but does not reach to 90\xb0 or hip begins to flex in later phase of motion'), (2, 'Knee flexion beyond 90 degrees with hip maintained in extension')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_ankle_dorsiflexion',
            field=models.IntegerField(verbose_name='Ankle dorsiflexion', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_ankle_flexion',
            field=models.IntegerField(verbose_name='Ankle plantarflexion', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_extension_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_flexion_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_adduction',
            field=models.IntegerField(verbose_name='Hip adduction', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_extension',
            field=models.IntegerField(verbose_name='Hip extension', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_flexion',
            field=models.IntegerField(verbose_name='Hip flexion', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_knee_extension',
            field=models.IntegerField(verbose_name='Knee extension', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_knee_flexion',
            field=models.IntegerField(verbose_name='Knee flexion', choices=[(0, 'Cannot be performed at all'), (1, 'Partial motion'), (2, 'Full motion')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Dysmetria', choices=[(0, 'Pronounced or unsystematic dysmetria'), (1, 'Slight or systematic dysmetria'), (2, 'No dysmetria')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_time',
            field=models.IntegerField(verbose_name='Speed', choices=[(0, 'Activity is more than 5 seconds longer than unaffected hand'), (1, '(2-5) seconds longer than unaffected side'), (2, 'Less than 2 seconds difference')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_tremor',
            field=models.IntegerField(verbose_name='Tremor', choices=[(0, 'Marked tremor'), (1, 'Slight tremor'), (2, 'No tremor')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_cylinder_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to grasp a small can (placed upright on a table without stabilization) by opening the fingers and opposing the volar surfaces of the thumb and digits. The arm may be supported but the tester may not assist with hand function. Test this grip against resistance by asking the patient to hold as you attempt to pull the can out with a slight tug.<strong>Hold the object and keep it steady</strong>', verbose_name='Cylinder shaped object (small can)tug upward, opposition in digits I and II', choices=[(0, 'Function cannot be performed'), (1, 'A can interposed between the thumb and index finger can be kept in place, but not against a slight tug'), (2, 'Can is held firmly against a tug')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_flex_pip_dip',
            field=models.IntegerField(help_text='Hold my finger and keep it stuck between your fingers', verbose_name='Flexion in PIP and DIP (digits II-V)extension in MCP II-V', choices=[(0, 'Required position cannot be attained'), (1, 'Grasp is weak'), (2, 'Grasp can be maintained against relatively great resistance')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_mass_ext',
            field=models.IntegerField(help_text='Open your hand. The therapist can help get the starting position with your fingers in flexion', verbose_name='Mass flexion from full active or passive flexion', choices=[(0, 'No extension occurs'), (1, 'Patient can release an active mass flexion grasp'), (2, 'Full active extension')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_mass_flex',
            field=models.IntegerField(help_text='Close your hand. The therapist can help get the starting position with your fingers in extension', verbose_name='Mass flexion from full active or passive extension', choices=[(0, 'No flexion occurs'), (1, 'Some flexion, but not full motion'), (2, 'Completed active flexion ')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_spherical_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to perform a spherical grasp by grasping a tennis ball. The tester may support the patient\u2019s arm but may not assist with the hand function required for the retrieval task. Test this grip against resistance by asking the patient to hold as you attempt to pull the ball out with a slight tug. <strong>Hold the ball and keep it steady</strong>', verbose_name='Fingers in abduction/flexion, thumb opposed, tennis ball', choices=[(0, 'Function cannot be performed'), (1, 'A tennis ball can be kept in place with a spherical grasp, but not against a slight tug'), (2, 'Tennis ball is held firmly against a tug')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_thumb_adduction',
            field=models.IntegerField(help_text='Ask the patient to perform pure thumb adduction with the scrap of paper interposed between the thumb and first digit. Test this grip against resistance by asking the patient to hold as you attempt to pull the paper out with a slight tug. <strong>Hold the paper between the thumb and forefinger</strong>', verbose_name='Thumb adduction', choices=[(0, 'Function cannot be performed'), (1, 'Scrap of paper interposed between the thumb and index finger can be kept in place, but not against a slight tug'), (2, 'Paper is held firmly against a tug')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_thumb_opposition',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to grasp a pen by opposing the thumb and index finger pads around the pen. The pen may not be stabilized by the therapist or the patient\u2019s other hand. Test this grip against resistance by asking the patient to hold as you attempt to pull the pencil out with a slight tug. <strong>Hold the pen and keep it steady</strong>', verbose_name='Opposition pulpa of the thumb against the pulpa of 2-nd finger,pencil, tug upward', choices=[(0, 'Function cannot be performed'), (1, 'A pencil interposed between the thumb pad and the pad of the index finger can be kept in place, but not against a slight tug'), (2, 'Pencil is held firmly against a tug')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_normal_reflex_activity',
            field=models.IntegerField(verbose_name='Normal reflex activity', choices=[(0, '2 of 3 reflexes markedly hyperactive'), (1, '1 reflex markedly hyperactive or at least 2 reflexes lively'), (2, 'Maximum of 1 reflex lively, none hyperactive')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_normal_reflex_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_ext',
            field=models.IntegerField(verbose_name='Extensors: triceps', choices=[(0, 'No reflex activity can be elicited'), (2, 'Reflex activity can be elicited')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_flex',
            field=models.IntegerField(verbose_name='Flexors: biceps and finger flexors', choices=[(0, 'No reflex activity can be elicited'), (2, 'Reflex activity can be elicited')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_total_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_hand_spine',
            field=models.IntegerField(verbose_name='Hand to lumbar spine', choices=[(0, 'No specific action is performed (or patient moves but does not reach ASIS)'), (1, ' Hand must pass anterior superior iliac spine (performed partly)'), (2, ' Performed faultlessly (patient clears ASIS and can extend arm behind back towards sacrum')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_pron_sup',
            field=models.IntegerField(verbose_name='Pronation-supination elbow at 90 shoulder at 0', choices=[(0, 'No pronation/supination, starting position impossible'), (1, 'Limited pronation/supination, maintains position'), (2, 'Full pronation/supination, maintains elbow extension')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_shoulder_flex',
            field=models.IntegerField(verbose_name='Shoulder flexion 0-90 elbow at 0 pronation-supination 0', choices=[(0, 'Immediate abduction or elbow flexion'), (1, 'Abduction or elbow flexion during movement'), (2, 'Complete flexion 90\xb0, maintains 0\xb0 in elbow')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_pron_sup',
            field=models.IntegerField(verbose_name='Pronation/supinationelbow at 0 shoulder at 30-90 flexion', choices=[(0, 'No pronation/supination, starting position impossible'), (1, 'Limited pronation/supination, maintains extension'), (2, 'Full pronation/supination, maintains elbow extension')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_shoulder_abd',
            field=models.IntegerField(verbose_name='Shoulder abduction 0 - 90 elbow at 0 forearm pronated', choices=[(0, 'Immediate supination or elbow flexion'), (1, 'Supination or elbow flexion during movement'), (2, 'Abduction 90\xb0, maintains extension and pronation')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_shoulder_flex',
            field=models.IntegerField(verbose_name='Shoulder flexion 90- 180 elbow at 0pronation-supination 0', choices=[(0, 'Immediate abduction or elbow flexion'), (1, 'Abduction or elbow flexion during movement'), (2, 'Complete flexion, maintains 0\xb0 in elbow')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_elbow',
            field=models.IntegerField(verbose_name='elbow extension', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_forearm',
            field=models.IntegerField(verbose_name='forearm pronation', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_shoulder',
            field=models.IntegerField(verbose_name='shoulder adduction / internal rotation', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_elbow_flex',
            field=models.IntegerField(verbose_name='Elbow flexion', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_forearm_sup',
            field=models.IntegerField(verbose_name='Forearm supination', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_abd',
            field=models.IntegerField(verbose_name='Shoulder abduction (90)', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_elev',
            field=models.IntegerField(verbose_name='Shoulder elevation', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_retrac',
            field=models.IntegerField(verbose_name='Shoulder retraction', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_rot',
            field=models.IntegerField(verbose_name='Shoulder external rotation', choices=[(0, 'Cannot be performed at all'), (1, 'Performed partly'), (2, 'Performed faultlessly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_circumduction',
            field=models.IntegerField(verbose_name='Circumduction', choices=[(0, 'Cannot perform volitionally'), (1, 'Jerky movement or incomplete'), (2, 'Complete and smooth circumduction')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_flex_elbow_0',
            field=models.IntegerField(verbose_name='Repeated dorsifexion / volar flexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'Cannot perform volitionally'), (1, 'Limited active range of motion'), (2, 'Full active range of motion, smoothly')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_flex_elbow_90',
            field=models.IntegerField(verbose_name='Repeated dorsifexion / volar flexion elbow at 90, forearm pronated shoulder at 0, slight finger flexion', choices=[(0, 'Cannot be performed'), (1, 'Can hold position but weak'), (2, 'Maintains position against resistance')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_0',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'Less than 15\xb0 active dorsiflexion'), (1, 'Dorsiflexion 15\xb0, no resistance is taken'), (2, 'Maintains position against resistance')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_90',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 90, forearm pronated shoulder at 0', choices=[(0, 'Less than 15\xb0 active dorsiflexion'), (1, 'Dorsiflexion 15\xb0, no resistance is taken'), (2, 'Maintains position against resistance')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='attention_calc',
            field=models.IntegerField(help_text='Count backward from 100 by sevens. 1 point for each correct answer. Stop after 5 answers. Alternatively spell "world" backward.', verbose_name='Attention and calculation', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_command',
            field=models.IntegerField(verbose_name='Follow a 3-stage command. "Take a paper in your hand, fold it in half, and put it on the floor."', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_copy',
            field=models.IntegerField(verbose_name='Copy the design shown', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_read',
            field=models.IntegerField(verbose_name='Read and obey the following: CLOSE YOUR EYES', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_repeat',
            field=models.IntegerField(verbose_name='Repeat the following "No ifs, ands, or buts"', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_watch_pen',
            field=models.IntegerField(verbose_name='Name a pencil and watch.', choices=[(0, b'0'), (1, b'1'), (2, b'2')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_write',
            field=models.IntegerField(verbose_name='Write a sentence', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_city',
            field=models.IntegerField(verbose_name='City', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_day_month',
            field=models.IntegerField(verbose_name='Day of the month', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_day_week',
            field=models.IntegerField(verbose_name='Day of the week', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_district',
            field=models.IntegerField(verbose_name='District or nearby street', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_institution',
            field=models.IntegerField(verbose_name='Institution (home, hospital, clinic)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_month',
            field=models.IntegerField(verbose_name='Month', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_place',
            field=models.IntegerField(verbose_name='Specific place (room or sector)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_state',
            field=models.IntegerField(verbose_name='State', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_time',
            field=models.IntegerField(verbose_name='Approximate time', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_year',
            field=models.IntegerField(verbose_name='Year', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='recall_words',
            field=models.IntegerField(help_text='Ask for the 3 objects repeated above. Give 1 point for each correct answer.', verbose_name='Recall', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='registration_words',
            field=models.IntegerField(help_text='Name 3 objects: 1 second to say each. Then ask the patient all 3 after you have said them. Give 1 point for each correct answer.Then repeat them until he/she learns all 3. Count trials and record', verbose_name='Registration', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Age', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='conducting_source',
            field=models.CharField(max_length=100, null=True, verbose_name='Conducting source', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_income',
            field=models.IntegerField(null=True, verbose_name='Family income', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_income_average',
            field=models.IntegerField(null=True, verbose_name='Average family income', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fammily_composition',
            field=models.CharField(max_length=255, null=True, verbose_name='Family composition', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fammily_ref_home',
            field=models.CharField(max_length=100, null=True, verbose_name='Family member reference at home', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fammily_ref_therapy',
            field=models.CharField(max_length=100, null=True, verbose_name='Family member reference for therapy frequency', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=100, null=True, verbose_name='Gender', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Marital status', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(max_length=100, null=True, verbose_name='Occupation/work', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='origin_city',
            field=models.CharField(max_length=100, null=True, verbose_name='City of origin', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profession',
            field=models.CharField(max_length=100, null=True, verbose_name='Profession', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='quantity_ppl_home',
            field=models.IntegerField(null=True, verbose_name='Number of people at home', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='schooling_level',
            field=models.CharField(max_length=100, null=True, verbose_name='Schooling level', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_insurance_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Social insurance status', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='transportation_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Social insurance status', blank=True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_bathe',
            field=models.IntegerField(verbose_name='c. Bathe yourself?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_clip_toenails',
            field=models.IntegerField(verbose_name='d. Clip your toenails?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_control_bladder',
            field=models.IntegerField(verbose_name='f. Control your bladder (not have an accident)?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_control_bowels',
            field=models.IntegerField(verbose_name='g. Control your bowels (not have an accident)?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_cut_food',
            field=models.IntegerField(verbose_name='a. Cut your food with a knife and fork?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_dress',
            field=models.IntegerField(verbose_name='b. Dress the top part of your body?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_heavy_household',
            field=models.IntegerField(verbose_name='j. Do heavy household chores (e.g.vacuum, laundry or yard work)?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_light_household',
            field=models.IntegerField(verbose_name='h. Do light household tasks/chores(e.g. dust, make a bed, take out garbage, do the dishes)?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_shopping',
            field=models.IntegerField(verbose_name='i. Go shopping?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_toilet',
            field=models.IntegerField(verbose_name='e. Get to the toilet on time?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_group_conversation',
            field=models.IntegerField(verbose_name='e. Participate in a conversation with a group of people?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_name_objs',
            field=models.IntegerField(verbose_name='d. Correctly name objects?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_reply',
            field=models.IntegerField(verbose_name='c. Reply to questions?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_say_name',
            field=models.IntegerField(verbose_name='a. Say the name of someone who was in front of you?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_tel_call',
            field=models.IntegerField(verbose_name='g. Call another person on the telephone, including selecting the correct phone number and dialing?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_tel_conversation',
            field=models.IntegerField(verbose_name='f. Have a conversation on the telephone? ', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_understand',
            field=models.IntegerField(verbose_name='b. Understand what was being said to you in a conversation?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_concentrate',
            field=models.IntegerField(verbose_name='e. Concentrate?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_day_week',
            field=models.IntegerField(verbose_name='d. Remember the day of the week?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_do_things',
            field=models.IntegerField(verbose_name='c. Remember to do things (e.g. keep scheduled appointments or take medication)?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_happ_day_bef',
            field=models.IntegerField(verbose_name='b. Remember things that happened the day before?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_ppl_told',
            field=models.IntegerField(verbose_name='a. Remember things that people just told you?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_solve_problems',
            field=models.IntegerField(verbose_name='g. Solve everyday problems?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_think_quickly',
            field=models.IntegerField(verbose_name='f. Think quickly?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Extremely difficult')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_carry_heavy_objs',
            field=models.IntegerField(verbose_name='a. Carry heavy objects (e.g. bag of groceries)?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_open_jar',
            field=models.IntegerField(verbose_name='c. Open a can or jar?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_pick_dime',
            field=models.IntegerField(verbose_name='e. Pick up a dime?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_tie_shoe_lace',
            field=models.IntegerField(verbose_name='d. Tie a shoe lace?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_turn_doorknob',
            field=models.IntegerField(verbose_name='b. Turn a doorknob?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_bed_chair',
            field=models.IntegerField(verbose_name='d. Move from a bed to a chair?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_climb_one_flight',
            field=models.IntegerField(verbose_name='g. Climb one flight of stairs?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_climb_several_flights',
            field=models.IntegerField(verbose_name='h. Climb several flights of stairs?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_in_out_car',
            field=models.IntegerField(verbose_name='i. Get in and out of a car?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_sitting',
            field=models.IntegerField(verbose_name='a. Stay sitting without losing your balance?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_standing',
            field=models.IntegerField(verbose_name='b. Stay standing without losing your balance?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_balance',
            field=models.IntegerField(verbose_name='c. Walk without losing your balance?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_fast',
            field=models.IntegerField(verbose_name='f. Walk fast?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_one_block',
            field=models.IntegerField(verbose_name='e. Walk one block?', choices=[(5, 'Not difficult at all'), (4, 'A little difficult'), (3, 'Somewhat difficult'), (2, 'Very difficult'), (1, 'Could not do at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_blame_mistakes',
            field=models.IntegerField(verbose_name='e. Blame yourself for mistakes that you made?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_burden',
            field=models.IntegerField(verbose_name='c. Feel that you are a burden to others?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_enjoy_things',
            field=models.IntegerField(verbose_name='f. Enjoy things as much as ever?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_nervous',
            field=models.IntegerField(verbose_name='g. Feel quite nervous?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_sad',
            field=models.IntegerField(verbose_name='a. Feel sad?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_worth_living',
            field=models.IntegerField(verbose_name='h. Feel that life is worth living?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_nobody_close',
            field=models.IntegerField(verbose_name='b. Feel that there is nobody you are close to?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_nothing_to_look_fwd',
            field=models.IntegerField(verbose_name='d. Feel that you have nothing to look forward to?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_smile_laugh',
            field=models.IntegerField(verbose_name='i. Smile and laugh at least once a day?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_arm',
            field=models.IntegerField(verbose_name='a. Arm that was most affected', choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_foot',
            field=models.IntegerField(verbose_name='d. Foot/ankle that was most affected', choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_hand',
            field=models.IntegerField(verbose_name='b. Grip of your hand that was most affected', choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_leg',
            field=models.IntegerField(verbose_name='c. Leg that was most affected', choices=[(5, 'A lot of strength'), (4, 'Quite a bit of strength'), (3, 'Some strength'), (2, 'A little strength'), (1, 'No strength at all')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_active_recreation',
            field=models.IntegerField(verbose_name='d. Active recreation (sports, outings,travel)?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_control_life',
            field=models.IntegerField(verbose_name='g. Your ability to control your life as you wish?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_family',
            field=models.IntegerField(verbose_name='e. Your role as a family member and/or friend?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_help_others',
            field=models.IntegerField(verbose_name='h. Your ability to help others?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_quiet_recreation',
            field=models.IntegerField(verbose_name='c. Quiet recreation (crafts, reading)?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_social',
            field=models.IntegerField(verbose_name='b. Your social activities?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_spiritual',
            field=models.IntegerField(verbose_name='f. Your participation in spiritual or religious activities?', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_work',
            field=models.IntegerField(verbose_name='a. Your work (paid, voluntary or other)', choices=[(5, 'None of the time'), (4, 'A little of the time'), (3, 'Some of the time'), (2, 'Most of the time'), (1, 'All of the time')]),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer1_forearm_right',
            field=models.DecimalField(verbose_name='(Pain) Algometer 1', max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer2_forearm_right',
            field=models.DecimalField(verbose_name='(Pain) Algometer 2', max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer3_forearm_right',
            field=models.DecimalField(verbose_name='(Pain) Algometer 3', max_digits=5, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility1_forearm_right',
            field=models.DecimalField(verbose_name='Sensibility 1', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility2_forearm_right',
            field=models.DecimalField(verbose_name='Sensibility 2', max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='verbalfluency',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', to='evaluation.Patient'),
        ),
        migrations.AddField(
            model_name='verbalfluency',
            name='period',
            field=models.ForeignKey(verbose_name='Period', to='evaluation.Period'),
        ),
    ]
