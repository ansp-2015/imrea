# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0016_auto_20160606_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='HAD',
            fields=[
                ('baseevaluation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation')),
                ('tension', models.IntegerField(verbose_name='I feel tense or "wound up"', choices=[(3, 'Most of the time'), (2, 'A lot of time'), (1, 'From time to time, occasionally'), (0, 'Not at all')])),
                ('enjoy', models.IntegerField(verbose_name='I still enjoy the things I used to enjoy', choices=[(3, 'Hardly at all'), (2, 'Only a little'), (1, 'Not quite so much'), (0, 'Definitely as much')])),
                ('frightened', models.IntegerField(verbose_name='I get a sort of frightened feeling as if something awful is about to happen')),
                ('laugh', models.IntegerField(verbose_name='I can laugh and see the funny side of things', choices=[(0, 'As much as I always could'), (1, 'Not quite so much now'), (2, 'Definitely not so much now'), (3, 'Not at all')])),
                ('worry', models.IntegerField(verbose_name='Worrying thoughts go through my mind', choices=[(3, 'A great deal of the time'), (2, 'A lot of the time'), (1, 'From time to time, but not too often'), (0, 'Only occasionally')])),
                ('cheerful', models.IntegerField(verbose_name='I feel cheerful', choices=[(3, 'Not at all'), (2, 'Not often'), (1, 'Sometimes'), (0, 'Most of the time')])),
                ('ease', models.IntegerField(verbose_name='I can sit at ease and feel relaxed', choices=[(0, 'Definitely'), (1, 'Usually'), (2, 'Not Often'), (3, 'Not at all')])),
                ('slowed', models.IntegerField(verbose_name='I feel as if I am slowed down', choices=[(3, 'Nearly all the time'), (2, 'Very often'), (1, 'Sometimes'), (0, 'Not at all')])),
                ('butterflies', models.IntegerField(verbose_name="I get a sort of frightened feeling like 'butterflies' in the stomach", choices=[(0, 'Not at all'), (1, 'Occasionally'), (2, 'Quite Often'), (3, 'Very Often')])),
                ('appearance', models.IntegerField(verbose_name='I have lost interest in my appearance', choices=[(3, 'Definitely'), (2, "I don't take as much care as I should"), (1, 'I may not take quite as much care'), (0, 'I take just as much care as ever')])),
                ('restless', models.IntegerField(verbose_name='I feel restless as I have to be on the move', choices=[(3, 'Very much indeed'), (2, 'Quite a lot'), (1, 'Not very much'), (0, 'Not at all')])),
                ('forward', models.IntegerField(verbose_name='I look forward with enjoyment to things', choices=[(0, 'As much as I ever did'), (1, 'Rather less than I used to'), (2, 'Definitely less than I used to'), (3, 'Hardly at all')])),
                ('panic', models.IntegerField(verbose_name='I get sudden feelings of panic', choices=[(3, 'Very often indeed'), (2, 'Quite often'), (1, 'Not very often'), (0, 'Not at all')])),
                ('book', models.IntegerField(verbose_name='I can enjoy a good book or radio or TV program', choices=[(0, 'Often'), (1, 'Sometimes'), (2, 'Not often'), (3, 'Very seldom')])),
            ],
            options={
                'verbose_name': 'HAD',
                'verbose_name_plural': 'HADs',
            },
            bases=('evaluation.baseevaluation',),
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
            field=models.IntegerField(verbose_name='Extensors: triceps', choices=[(0, 'None'), (2, 'Can be elicited')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_flex',
            field=models.IntegerField(verbose_name='Flexors: biceps and finger flexors', choices=[(0, 'None'), (2, 'Can be elicited')]),
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
            field=models.IntegerField(verbose_name='elbow extension', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_forearm',
            field=models.IntegerField(verbose_name='forearm pronation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_shoulder',
            field=models.IntegerField(verbose_name='shoulder adduction / internal rotation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_elbow_flex',
            field=models.IntegerField(verbose_name='Elbow flexion', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_forearm_sup',
            field=models.IntegerField(verbose_name='Forearm supination', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_abd',
            field=models.IntegerField(verbose_name='Shoulder abduction (90)', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_elev',
            field=models.IntegerField(verbose_name='Shoulder elevation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_retrac',
            field=models.IntegerField(verbose_name='Shoulder retraction', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_rot',
            field=models.IntegerField(verbose_name='Shoulder external rotation', choices=[(0, 'None'), (1, 'Partial'), (2, 'Full')]),
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
            model_name='fuglmeyer',
            name='vol_mov_mix_hand_spine',
            field=models.IntegerField(verbose_name='Hand to lumbar spine', choices=[(0, 'Cannot be performed, hand in front of SIAS'), (1, 'Hand behind of SIAS (without compensation)'), (2, 'Hand to lumbar spine (without compensation)')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='vol_mov_mix_pron_sup',
            field=models.IntegerField(verbose_name='Pronation-supination elbow at 90 shoulder at 0', choices=[(0, 'No pronation/supination, starting position impossible'), (1, 'Limited pronation/supination, maintains position'), (2, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='vol_mov_mix_shoulder_flex',
            field=models.IntegerField(verbose_name='Shoulder flexion 0-90 elbow at 0 pronation-supination 0', choices=[(0, 'Immediate abduction or elbow flexion'), (1, 'Abduction or elbow flexion during movement'), (2, 'Complete flexion 90\xb0, maintains 0\xb0 in elbow')]),
        ),
    ]
