# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0019_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eegfile',
            options={'verbose_name': 'Arquivo EEG', 'verbose_name_plural': 'Arquivos EEG'},
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1a',
            field=models.IntegerField(verbose_name='Neglect 1a', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1b',
            field=models.IntegerField(verbose_name='Neglect 1b', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1c',
            field=models.IntegerField(verbose_name='Neglect 1c', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_1d',
            field=models.IntegerField(verbose_name='Neglect 1d', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2a',
            field=models.IntegerField(verbose_name='Neglect 2a', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2b',
            field=models.IntegerField(verbose_name='Neglect 2b', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2c',
            field=models.IntegerField(verbose_name='Neglect 2c', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_2d',
            field=models.IntegerField(verbose_name='Neglect 2d', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3a',
            field=models.IntegerField(verbose_name='Neglect 3a', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3b',
            field=models.IntegerField(verbose_name='Neglect 3b', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3c',
            field=models.IntegerField(verbose_name='Neglect 3c', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_3d',
            field=models.IntegerField(verbose_name='Neglect 3d', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4a',
            field=models.IntegerField(verbose_name='Neglect 4a', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4b',
            field=models.IntegerField(verbose_name='Neglect 4b', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4c',
            field=models.IntegerField(verbose_name='Neglect 4c', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='clin',
            name='neglect_4d',
            field=models.IntegerField(verbose_name='Neglect 4d', choices=[(1, 'Yes'), (2, 'No'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_stairs',
            field=models.IntegerField(verbose_name='Locomotion stairs', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='locomotion_wheelchair',
            field=models.IntegerField(verbose_name='Locomotion walking/wheelchair', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_bathing',
            field=models.IntegerField(verbose_name='Bathing/showering', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_lower_body',
            field=models.IntegerField(verbose_name='Dressing lower body', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_dressing_upper_body',
            field=models.IntegerField(verbose_name='Dressing upper body', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_eating',
            field=models.IntegerField(verbose_name='Eating', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_grooming',
            field=models.IntegerField(verbose_name='Grooming', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='self_care_toileting',
            field=models.IntegerField(verbose_name='Toileting', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bladder_mgt',
            field=models.IntegerField(verbose_name='Bladder management', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='sphincter_bowel_mgt',
            field=models.IntegerField(verbose_name='Bowel management', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_shower',
            field=models.IntegerField(verbose_name='Transfers bathtub/shower', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_toilet',
            field=models.IntegerField(verbose_name='Transfers toilet', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fim',
            name='transfer_wheelchair',
            field=models.IntegerField(verbose_name='Transfers bed/chair/wheelchair', choices=[(1, 'Total assistance'), (2, 'Maximal assistance'), (3, 'Moderate assistance'), (4, 'Minimal assistance'), (5, 'Supervision'), (6, 'Modified independence'), (7, 'Complete independence'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Scoring Dysmetria', choices=[(0, 'Dismetria evidente ou assistem\xe1tico'), (1, 'Dismetria leve ou sistem\xe1tica'), (2, 'Sem dismetria')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_time',
            field=models.IntegerField(verbose_name='Scoring Speed', choices=[(0, '6 segundos mais lento que o lado n\xe3o afetado'), (1, '2 a 5 segundos mais lento que o lado afetado'), (2, 'Menos de 2 segundos de diferen\xe7a')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_tremor',
            field=models.IntegerField(verbose_name='Scoring Tremor', choices=[(0, 'Tremor marcante'), (1, 'Tremor leve'), (2, 'Sem tremor')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles',
            field=models.IntegerField(verbose_name='Achilles', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa pode ser avaliada')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles_pattelar',
            field=models.IntegerField(verbose_name='Achilles and patellar reflexes', choices=[(0, '2 ou 3 reflexos est\xe3o marcadamente hiperativos'), (1, '1 reflexo esta hiperativo ou 2 est\xe3o vivos'), (2, 'N\xe3o mais que um reflexo esta vivo')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles_pattelar_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_pattelar',
            field=models.IntegerField(verbose_name='Patellar', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa pode ser avaliada')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_total_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion sitting', choices=[(0, 'Sem movimento ativo'), (1, 'Com dosriflex\xe3o limitada'), (2, 'Completa dorsiflex\xe3o ativa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion sitting', choices=[(0, 'Sem movimento ativo'), (1, 'O joelho pode ativamente ser fletido at\xe9 90\xb0 (palpar os tend\xf5es dos flexores do joelho)'), (2, 'O joelho pode ser fletido al\xe9m de 90\xb0')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion standing', choices=[(0, 'Sem movimenta\xe7\xe3o ativa'), (1, 'Limita\xe7\xe3o de dorsiflex\xe3o'), (2, 'Dorsiflex\xe3o completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion standing', choices=[(0, 'O joelho n\xe3o pode ser fletido se o quadril n\xe3o \xe9 fletido simultaneamente'), (1, 'Menos do que 90\xb0 do joelho ou se realiza com flex\xe3o de quadril'), (2, 'At\xe9 90\xb0 de flex\xe3o sem flex\xe3o simultanea do quadril')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_ankle_dorsiflexion',
            field=models.IntegerField(verbose_name='Ankle dorsiflexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_ankle_flexion',
            field=models.IntegerField(verbose_name='Ankle plantarflexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_extension_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_flexion_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_adduction',
            field=models.IntegerField(verbose_name='Hip adduction', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_extension',
            field=models.IntegerField(verbose_name='Hip extension', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_flexion',
            field=models.IntegerField(verbose_name='Hip flexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_knee_extension',
            field=models.IntegerField(verbose_name='Knee extension', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_knee_flexion',
            field=models.IntegerField(verbose_name='Knee flexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Dysmetria', choices=[(0, 'Pronunciada ou assistem\xe1tica'), (1, 'Leve e sistem\xe1tica'), (2, 'Nenhuma')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_time',
            field=models.IntegerField(verbose_name='Speed', choices=[(0, 'Mais do que 5 segundos mais lento do que o lado n\xe3o acometido'), (1, '2-5 segundos mais lento'), (2, 'Diferen\xe7a m\xe1xima de 01 segundo entre os lados')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_tremor',
            field=models.IntegerField(verbose_name='Tremor', choices=[(0, 'Pronunciada ou assistem\xe1tica'), (1, 'Leve e sistem\xe1tica'), (2, 'Nenhuma')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_cylinder_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to grasp a small can (placed upright on a table without stabilization) by opening the fingers and opposing the volar surfaces of the thumb and digits. The arm may be supported but the tester may not assist with hand function. Test this grip against resistance by asking the patient to hold as you attempt to pull the can out with a slight tug.<strong>Hold the object and keep it steady</strong>', verbose_name='Cylinder shaped object (small can)tug upward, opposition in digits I and II', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_flex_pip_dip',
            field=models.IntegerField(help_text='Hold my finger and keep it stuck between your fingers', verbose_name='Flexion in PIP and DIP (digits II-V)extension in MCP II-V', choices=[(0, 'A posi\xe7\xe3o requerida n\xe3o pode ser adquirida'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'A preens\xe3o pode ser mantida contra a resist\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_mass_ext',
            field=models.IntegerField(help_text='Open your hand. The therapist can help get the starting position with your fingers in flexion', verbose_name='Mass flexion from full active or passive flexion', choices=[(0, 'N\xe3o ocorre extens\xe3o'), (1, 'O sujeito libera ativamente a flex\xe3o em massa'), (2, 'Extens\xe3o ativa completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_mass_flex',
            field=models.IntegerField(help_text='Close your hand. The therapist can help get the starting position with your fingers in extension', verbose_name='Mass flexion from full active or passive extension', choices=[(0, 'Nenhuma flex\xe3o ocorre'), (1, 'Alguma flex\xe3o com ADM incompleta'), (2, 'Flex\xe3o ativa completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_spherical_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to perform a spherical grasp by grasping a tennis ball. The tester may support the patient\u2019s arm but may not assist with the hand function required for the retrieval task. Test this grip against resistance by asking the patient to hold as you attempt to pull the ball out with a slight tug. <strong>Hold the ball and keep it steady</strong>', verbose_name='Fingers in abduction/flexion, thumb opposed, tennis ball', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_thumb_adduction',
            field=models.IntegerField(help_text='Ask the patient to perform pure thumb adduction with the scrap of paper interposed between the thumb and first digit. Test this grip against resistance by asking the patient to hold as you attempt to pull the paper out with a slight tug. <strong>Hold the paper between the thumb and forefinger</strong>', verbose_name='Thumb adduction', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_thumb_opposition',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to grasp a pen by opposing the thumb and index finger pads around the pen. The pen may not be stabilized by the therapist or the patient\u2019s other hand. Test this grip against resistance by asking the patient to hold as you attempt to pull the pencil out with a slight tug. <strong>Hold the pen and keep it steady</strong>', verbose_name='Opposition pulpa of the thumb against the pulpa of 2-nd finger,pencil, tug upward', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_normal_reflex_activity',
            field=models.IntegerField(verbose_name='Normal reflex activity', choices=[(0, 'No m\xednimo dois dos tr\xeas reflexos f\xe1sicos s\xe3o marcadamente hiperativos'), (1, 'Um reflexo est\xe1 marcadamente hiperativo, ou no m\xednimo dois reflexos est\xe3o vivos'), (2, 'N\xe3o mais que um reflexo est\xe1 vivo, e nenhum est\xe1 hiperativo')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_normal_reflex_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_ext',
            field=models.IntegerField(verbose_name='Extensors: triceps', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa presente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_flex',
            field=models.IntegerField(verbose_name='Flexors: biceps and finger flexors', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa presente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_total_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_hand_spine',
            field=models.IntegerField(verbose_name='M\xe3o \xe0 coluna lombar', choices=[(0, 'Nenhuma a\xe7\xe3o espec\xedfica realizada'), (1, 'A m\xe3o ultrapassa a espinha il\xedaca \xe2ntero-superior'), (2, 'A\xe7\xe3o realizada completamente (m\xe3o chega a coluna lombar)')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_pron_sup',
            field=models.IntegerField(verbose_name='Prona\xe7\xe3o/Supina\xe7\xe3o antebra\xe7o cotovelo em 90 e ombro em 0', choices=[(0, 'Posi\xe7\xe3o correta do ombro e cotovelo n\xe3o pode ser atingida, e/ou prona\xe7\xe3o ou supina\xe7\xe3o n\xe3o pode ser realizada totalmente'), (1, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S'), (2, 'Mant\xe9m posi\xe7\xe3o com P/S completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_shoulder_flex',
            field=models.IntegerField(verbose_name='Flex\xe3o de ombro 0 - 90, cotovelo 0 e antebra\xe7o prona\xe7\xe3o/ supina\xe7\xe3o (P/S)  0', choices=[(0, 'Imediata abdu\xe7\xe3o ombro e/ ou flex\xe3o de cotovelo'), (1, 'Abdu\xe7\xe3o e/ou  flex\xe3o de cotovelo durante o movimento'), (2, 'Flex\xe3o completa 90\xb0 e  mant\xe9m extens\xe3o cotovelo')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_pron_sup',
            field=models.IntegerField(verbose_name='Prona\xe7\xe3o/Supina\xe7\xe3o antebra\xe7o cotovelo em 90 e ombro em 0', choices=[(0, 'Posi\xe7\xe3o inicial n\xe3o pode ser alcan\xe7ada e/ou n\xe3o realiza P/S'), (1, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S'), (2, 'Mant\xe9m posi\xe7\xe3o com P/S completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_shoulder_abd',
            field=models.IntegerField(verbose_name='Abdu\xe7\xe3o do ombro a 90 com o cotovelo 0 e antebra\xe7o em prona\xe7\xe3o', choices=[(0, 'Imediata supina\xe7\xe3o e/ ou flex\xe3o de cotovelo'), (1, 'Supina\xe7\xe3o e/ou flex\xe3o de cotovelo durante o movimento'), (2, 'Abdu\xe7\xe3o completa 90 e mant\xe9m extens\xe3o cotovelo e prona\xe7\xe3o')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_shoulder_flex',
            field=models.IntegerField(verbose_name='Flex\xe3o do ombro de 90 - 180, cotovelo em 0, e antebra\xe7o P/S em 0', choices=[(0, 'Imediata abdu\xe7\xe3o ombro e/ ou flex\xe3o de cotovelo'), (1, 'Abdu\xe7\xe3o e/ou flex\xe3o de cotovelo durante o movimento'), (2, 'Flex\xe3o completa 90 e mant\xe9m extens\xe3o cotovelo')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_elbow',
            field=models.IntegerField(verbose_name='Cotovelo - extens\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_forearm',
            field=models.IntegerField(verbose_name='Antebra\xe7o - prona\xe7\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_shoulder',
            field=models.IntegerField(verbose_name='Ombro - adu\xe7\xe3o e rota\xe7\xe3o interna', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_elbow_flex',
            field=models.IntegerField(verbose_name='Cotovelo - Flex\xe3o de cotovelo', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_forearm_sup',
            field=models.IntegerField(verbose_name='Antebra\xe7o - supina\xe7\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_abd',
            field=models.IntegerField(verbose_name='Ombro - Abdu\xe7\xe3o 90\xb0', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_elev',
            field=models.IntegerField(verbose_name='Ombro - eleva\xe7\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_retrac',
            field=models.IntegerField(verbose_name='Ombro - Retra\xe7\xe3o de ombro', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_rot',
            field=models.IntegerField(verbose_name='Ombro - Rota\xe7\xe3o externa', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_circumduction',
            field=models.IntegerField(verbose_name='Circumduction', choices=[(0, 'N\xe3o realiza movimento ativo'), (1, 'Movimento incompleto e/ou movimentos oscilantes'), (2, 'Movimento completo, com exatid\xe3o')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_flex_elbow_0',
            field=models.IntegerField(verbose_name='Repeated dorsifexion / volar flexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'N\xe3o ocorre movimento volunt\xe1rio'), (1, 'Movimento ativo com ADM incompleta'), (2, 'Movimento ativo com ADM completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_flex_elbow_90',
            field=models.IntegerField(verbose_name='Repeated dorsifexion / volar flexion elbow at 90, forearm pronated shoulder at 0, slight finger flexion', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho ate 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Posi\xe7\xe3o pode ser mantida contra resist\xeancia (leve)')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_0',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho at\xe9 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Mant\xe9m 15\xb0 dorsiflex\xe3o contra resist\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_90',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 90, forearm pronated shoulder at 0', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho ate 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Posi\xe7\xe3o pode ser mantida contra resist\xeancia (leve)')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='appearance',
            field=models.IntegerField(verbose_name='I have lost interest in my appearance', choices=[(3, 'Definitely'), (2, "I don't take as much care as I should"), (1, 'I may not take quite as much care'), (0, 'I take just as much care as ever'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='book',
            field=models.IntegerField(verbose_name='I can enjoy a good book or radio or TV program', choices=[(3, 'Very seldom'), (2, 'Not often'), (1, 'Sometimes'), (0, 'Often'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='butterflies',
            field=models.IntegerField(verbose_name="I get a sort of frightened feeling like 'butterflies' in the stomach", choices=[(3, 'Very Often'), (2, 'Quite Often'), (1, 'Occasionally'), (0, 'Not at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='cheerful',
            field=models.IntegerField(verbose_name='I feel cheerful', choices=[(3, 'Not at all'), (2, 'Not often'), (1, 'Sometimes'), (0, 'Most of the time'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='ease',
            field=models.IntegerField(verbose_name='I can sit at ease and feel relaxed', choices=[(3, 'Not at all'), (2, 'Not often'), (1, 'Usually'), (0, 'Definitely'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='enjoy',
            field=models.IntegerField(verbose_name='I still enjoy the things I used to enjoy', choices=[(3, 'Hardly at all'), (2, 'Only a little'), (1, 'Not quite so much'), (0, 'Definitely as much'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='forward',
            field=models.IntegerField(verbose_name='I look forward with enjoyment to things', choices=[(3, 'Hardly at all'), (2, 'Definitely less than I used to'), (1, 'Rather less than I used to'), (0, 'As much as I ever did'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='frightened',
            field=models.IntegerField(verbose_name='I get a sort of frightened feeling as if something awful is about to happen', choices=[(3, 'Very definitely and quite badly'), (2, 'Yes, but not too badly'), (1, "A little, but it doesn't worry me"), (0, 'Not at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='laugh',
            field=models.IntegerField(verbose_name='I can laugh and see the funny side of things', choices=[(3, 'Not at all'), (2, 'Definitely not so much now'), (1, 'Not quite so much now'), (0, 'As much as I always could'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='panic',
            field=models.IntegerField(verbose_name='I get sudden feelings of panic', choices=[(3, 'Very often indeed'), (2, 'Quite often'), (1, 'Not very often'), (0, 'Not at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='restless',
            field=models.IntegerField(verbose_name='I feel restless as I have to be on the move', choices=[(3, 'Very much indeed'), (2, 'Quite a lot'), (1, 'Not very much'), (0, 'Not at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='slowed',
            field=models.IntegerField(verbose_name='I feel as if I am slowed down', choices=[(3, 'Nearly all the time'), (2, 'Very often'), (1, 'Sometimes'), (0, 'Not at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='tension',
            field=models.IntegerField(verbose_name='I feel tense or "wound up"', choices=[(3, 'Most of the time'), (2, 'A lot of time'), (1, 'From time to time, occasionally'), (0, 'Not at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='worry',
            field=models.IntegerField(verbose_name='Worrying thoughts go through my mind', choices=[(3, 'A great deal of the time'), (2, 'A lot of the time'), (1, 'From time to time, but not too often'), (0, 'Only occasionally'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='agitation',
            field=models.IntegerField(verbose_name='agitation', choices=[(0, 'None'), (1, 'Fidgetiness'), (2, 'Playing with hands, hair,etc'), (3, "Moving about, can't sit still"), (4, 'Hand wringing, nail biting, hair-pulling, biting of lips'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='anxiety_psychic',
            field=models.IntegerField(verbose_name='Anxiety: psychic', choices=[(0, 'No difficulty'), (1, 'Subjective tension and irritability'), (2, 'Worrying about minor matters'), (3, 'Apprehensive attitude apparent in face or speech'), (4, 'Fears expressed without questioning'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='anxiety_somatic',
            field=models.IntegerField(verbose_name='Anxiety: somatic', choices=[(0, 'Absent'), (1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Incapacitating'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='gastro',
            field=models.IntegerField(verbose_name='somatic symptoms: gastrointestinal', choices=[(0, 'None'), (1, 'Loss of appetite but eating without staff encouragement. Heavy feelings in abdomen'), (2, 'Difficulty eating without staff urging. Requests or requires laxatives or medication for bowels or medication for gastro-intestinal symptoms'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='general',
            field=models.IntegerField(verbose_name='somatic symptoms: general', choices=[(0, 'None'), (1, 'Heaviness in limbs, back or head. Backaches, headache, muscle aches. Loss of energy and fatigability'), (2, 'Any clear-cut symptom'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='genital',
            field=models.IntegerField(verbose_name='genital symptoms (loss of libido, menstrual disturbances)', choices=[(0, 'Absent'), (1, 'Mild'), (2, 'Severe'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='guilt',
            field=models.IntegerField(verbose_name='feelings of guilt', choices=[(0, 'Absent'), (1, 'Self reproach, feels he has let people down'), (2, 'Ideas of guilt or rumination over past errors or sinful deed'), (3, 'Present illness is a punishmnent. Delusions of guilt'), (4, 'Hears accusatory or denunciatory voices and/or experiences threatening visual hallucinations'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='hypochondriasis',
            field=models.IntegerField(verbose_name='hypochondriasis', choices=[(0, 'Not present'), (1, 'Self-absorption (bodily)'), (2, 'Preoccupation with health'), (3, 'Frequent complaints, requests for help, etc. ...'), (4, 'Hypochondriacal delusions'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='insight',
            field=models.IntegerField(verbose_name='insight', choices=[(0, 'Not depressed (based on above items) OR Acknowledges being depressed and ill'), (1, 'Acknowledges illness but attributes cause to bad food, climate, overwork, virus, need for rest, etc.'), (2, 'Denies being ill at all'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='insomnia_early',
            field=models.IntegerField(verbose_name='insomnia early', choices=[(0, 'No difficulty falling asleep'), (1, 'Complains of occasional difficulty falling asleep - more than 1/2 hour'), (2, 'Complains of nightly difficulty falling asleep'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='insomnia_late',
            field=models.IntegerField(verbose_name='insomnia late', choices=[(0, 'No difficulty'), (1, 'Waking in early hours of the morning but goes back to sleep'), (2, 'Unable to fall asleep again if he gets out of bed'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='insomnia_middle',
            field=models.IntegerField(verbose_name='insomnia middle', choices=[(0, 'No difficulty'), (1, 'Patient complains of being restless and disturbed during the night'), (2, 'Waking during the night - any getting out of bed (except for purposes of voiding)'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='mood',
            field=models.IntegerField(verbose_name='depressed mood (sadness, hopeless, helpless, worthless)', choices=[(0, 'Absent'), (1, 'These feelings are indicated only on questioning'), (2, 'These feelings are spontaneously reported verbally'), (3, 'Communicates feelings non-verbally i.e., through facial expression, posture, voice, and tendency to weep'), (4, 'Patient reports VIRTUALLY ONLY these feelings in his spontaneous verbal and non-verbal communication'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='retardation',
            field=models.IntegerField(verbose_name='retardation: psychomotor (slowness of thought and speech; impaired ability to concentrate; decreased motor activity)', choices=[(0, 'Normal speech and thought'), (1, 'Slight retardation at interview'), (2, 'Obvious retardation at interview'), (3, 'Interview difficult'), (4, 'Complete stupor'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='suicide',
            field=models.IntegerField(verbose_name='suicide', choices=[(0, 'Absent'), (1, 'Feels life is not worth living'), (2, 'Wishes he were dead or any thoughts of possible death to self'), (3, 'Suicide ideas or gesture'), (4, 'Attempts at suicide (any serious attempt rates)'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='weight_history',
            field=models.IntegerField(verbose_name='loss of weight', choices=[(0, 'No weight loss'), (1, 'Probable weight loss associated with present illness'), (2, 'Definite (according to patient) weight loss'), (3, 'Not assessed'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='weight_weekly',
            field=models.IntegerField(verbose_name='loss of weight', choices=[(0, 'No weight loss'), (1, 'Probable weight loss associated with present illness (>500g/week)'), (2, 'Definite weight loss(>1kg/week)'), (3, 'Not assessed'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='hamilton',
            name='work',
            field=models.IntegerField(verbose_name='work and activities', choices=[(0, 'No difficulty'), (1, 'Thoughts and feelings of incapacity, fatigue or weakness related to activities (work or hobbies)'), (2, 'Loss of interest in activities (hobbies or work) - either directly reported by patient, or indirectly in listlessness, indecision and vacillation (feels he has to push himself to work or do activities)'), (3, 'Decrease in actual time spent in activities or decrease in productivity. In hospital, if patient does not spend at least three hours a day in activities (hospital job or hobbies) exclusive of ward chores'), (4, 'Stopped working because of present illness. In hospital, if patient engages in no activities except ward chores, or if patient fails to perform ward chores unassisted'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='attention_calc',
            field=models.IntegerField(help_text='Subtrair 100-7, 7 vezes sucessivamente ( ponto para cada c\xe1lculo correto)<br>Alternativamente, soletrar MUNDO de tr\xe1s para frente.', verbose_name='Aten\xe7\xe3o e c\xe1lculo', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_command',
            field=models.IntegerField(verbose_name="Comando: 'pegue este papel com a m\xe3o direita dobre ao meio e coloque no ch\xe3o' (3 pontos)", choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_copy',
            field=models.IntegerField(verbose_name='Copiar um desenho (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_read',
            field=models.IntegerField(verbose_name="Ler e obedecer 'feche os olhos' (1 ponto)", choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_repeat',
            field=models.IntegerField(verbose_name="Repetir 'nem aqui, nem ali, nem l\xe1' (1 ponto)", choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_watch_pen',
            field=models.IntegerField(verbose_name='Nomear um rel\xf3gio e uma caneta (2 pontos)', choices=[(0, b'0'), (1, b'1'), (2, b'2')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_write',
            field=models.IntegerField(verbose_name='Escrever uma frase (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_city',
            field=models.IntegerField(verbose_name='Cidade (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_day_month',
            field=models.IntegerField(verbose_name='Dia do m\xeas (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_day_week',
            field=models.IntegerField(verbose_name='Dia da semana (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_district',
            field=models.IntegerField(verbose_name='Bairro ou rua pr\xf3xima (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_institution',
            field=models.IntegerField(verbose_name='Institui\xe7\xe3o (resid\xeancia, hospital, cl\xednica) (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_month',
            field=models.IntegerField(verbose_name='M\xeas (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_place',
            field=models.IntegerField(verbose_name='Local espec\xedfico (aposento ou setor) (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_state',
            field=models.IntegerField(verbose_name='Estado (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_time',
            field=models.IntegerField(verbose_name='Hora aproximada (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_year',
            field=models.IntegerField(verbose_name='Ano (1 ponto)', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='recall_words',
            field=models.IntegerField(help_text='Pergunte pelas 3 palavras ditas anteriormente (1 ponto por palavra)', verbose_name='Evoca\xe7\xe3o', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='registration_words',
            field=models.IntegerField(help_text='Fale 3 palavras n\xe3o relacionadas. Posteriormente pergunte ao paciente pelas 3 palavras. D\xea 1 ponto para cada palavra certa. <br>Depois repita as palavras e certifique-se de que o paciente as aprendeu, pois mais adiante voc\xea ir\xe1 pergunt\xe1-las novamente', verbose_name='Mem\xf3ria imediata', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3')]),
        ),
        migrations.AlterField(
            model_name='moca',
            name='total_twelve_year_old',
            field=models.PositiveIntegerField(blank=True, help_text='Adicionar 1 ponto se \u2264 12 anos de escolaridade', null=True, verbose_name='Less than 12 yr edu', choices=[(0, b'0'), (1, b'1')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_dorsiflexion_left',
            field=models.IntegerField(verbose_name='Left dorsiflexion', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_dorsiflexion_right',
            field=models.IntegerField(verbose_name='Right dorsiflexion', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_dorsiflexion_subtalar_inversion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_gastrocnemius_g5_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_gastrocnemius_g5_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_gastrocnemius_g5_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_sole_g2_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_sole_g2_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_sole_g2_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_sole_g5_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_sole_g5_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_plantar_flexion_sole_g5_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_subtalar_inversion_left',
            field=models.IntegerField(verbose_name='Left inversion', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='ankle_subtalar_inversion_right',
            field=models.IntegerField(verbose_name='Right inversion', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='elbow_extension_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='elbow_extension_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='elbow_extension_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='elbow_flexion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='elbow_flexion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='elbow_flexion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='fingers_mp_extensor_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='fingers_mp_extensor_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='fingers_mp_extensor_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='fingers_mp_flexion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='fingers_mp_flexion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='fingers_mp_flexion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='forearm_pronation_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='forearm_pronation_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='forearm_pronation_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='forearm_supination_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='forearm_supination_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='forearm_supination_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_abduction_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_abduction_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_abduction_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_adduction_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_adduction_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_adduction_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_extension_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_extension_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_extension_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_flexion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_flexion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_flexion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_lateral_rotation_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_lateral_rotation_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_lateral_rotation_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_medial_rotation_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_medial_rotation_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='hip_medial_rotation_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_extension_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_extension_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_extension_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_biceps_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_biceps_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_biceps_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_semitendinosus_g2_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_semitendinosus_g2_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_semitendinosus_g2_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_semitendinosus_g5_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_semitendinosus_g5_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='knee_flexion_semitendinosus_g5_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_abduction_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_abduction_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_abduction_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_flexion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_flexion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_flexion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_lateral_rotation_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_lateral_rotation_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='shoulder_lateral_rotation_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='subtalar_eversion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='subtalar_eversion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='subtalar_eversion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='subtalar_inversion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='subtalar_inversion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='subtalar_inversion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='wrist_extension_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='wrist_extension_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='wrist_extension_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='wrist_flexion_left',
            field=models.IntegerField(verbose_name='Left', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='wrist_flexion_obs',
            field=models.TextField(null=True, verbose_name='Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='mrc',
            name='wrist_flexion_right',
            field=models.IntegerField(verbose_name='Right', choices=[(5, 'Grade 5'), (4, 'Grade 4'), (3, 'Grade 3'), (2, 'Grade 2'), (1, 'Grade 1'), (0, 'Grade 0')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Idade', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='conducting_source',
            field=models.CharField(max_length=100, null=True, verbose_name='Fonte encaminhadora', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_income',
            field=models.IntegerField(null=True, verbose_name='Renda familiar', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='family_income_average',
            field=models.IntegerField(null=True, verbose_name='Renda per capta', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fammily_composition',
            field=models.CharField(max_length=255, null=True, verbose_name='Composi\xe7\xe3o familiar', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fammily_ref_home',
            field=models.CharField(max_length=100, null=True, verbose_name='Retaguarda de familiar para a frequ\xeancia no tratamento', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fammily_ref_therapy',
            field=models.CharField(max_length=100, null=True, verbose_name='Retaguarda de transporte para a frequ\xeancia no tratamento', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=100, null=True, verbose_name='G\xeanero', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Estado civil', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(max_length=100, null=True, verbose_name='Ocupa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='origin_city',
            field=models.CharField(max_length=100, null=True, verbose_name='Cidade de proced\xeancia', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profession',
            field=models.CharField(max_length=100, null=True, verbose_name='Profiss\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='quantity_ppl_home',
            field=models.IntegerField(null=True, verbose_name='N. de pessoas no domic\xedlio', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='schooling_level',
            field=models.CharField(max_length=100, null=True, verbose_name='Escolaridade', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_insurance_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Situa\xe7\xe3o previdenci\xe1ria', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='transportation_status',
            field=models.CharField(max_length=100, null=True, verbose_name='Situa\xe7\xe3o previdenci\xe1ria', blank=True),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_bathe',
            field=models.IntegerField(verbose_name='c. Bathe yourself?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_clip_toenails',
            field=models.IntegerField(verbose_name='d. Clip your toenails?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_control_bladder',
            field=models.IntegerField(verbose_name='f. Control your bladder (not have an accident)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_control_bowels',
            field=models.IntegerField(verbose_name='g. Control your bowels (not have an accident)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_cut_food',
            field=models.IntegerField(verbose_name='a. Cut your food with a knife and fork?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_dress',
            field=models.IntegerField(verbose_name='b. Dress the top part of your body?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_heavy_household',
            field=models.IntegerField(verbose_name='j. Do heavy household chores (e.g.vacuum, laundry or yard work)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_light_household',
            field=models.IntegerField(verbose_name='h. Do light household tasks/chores(e.g. dust, make a bed, take out garbage, do the dishes)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_shopping',
            field=models.IntegerField(verbose_name='i. Go shopping?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_toilet',
            field=models.IntegerField(verbose_name='e. Get to the toilet on time?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_group_conversation',
            field=models.IntegerField(verbose_name='e. Participate in a conversation with a group of people?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_name_objs',
            field=models.IntegerField(verbose_name='d. Correctly name objects?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_reply',
            field=models.IntegerField(verbose_name='c. Reply to questions?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_say_name',
            field=models.IntegerField(verbose_name='a. Say the name of someone who was in front of you?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_tel_call',
            field=models.IntegerField(verbose_name='g. Call another person on the telephone, including selecting the correct phone number and dialing?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_tel_conversation',
            field=models.IntegerField(verbose_name='f. Have a conversation on the telephone? ', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_understand',
            field=models.IntegerField(verbose_name='b. Understand what was being said to you in a conversation?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_concentrate',
            field=models.IntegerField(verbose_name='e. Concentrate?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_day_week',
            field=models.IntegerField(verbose_name='d. Remember the day of the week?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_do_things',
            field=models.IntegerField(verbose_name='c. Remember to do things (e.g. keep scheduled appointments or take medication)?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_happ_day_bef',
            field=models.IntegerField(verbose_name='b. Remember things that happened the day before?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_ppl_told',
            field=models.IntegerField(verbose_name='a. Remember things that people just told you?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_solve_problems',
            field=models.IntegerField(verbose_name='g. Solve everyday problems?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_think_quickly',
            field=models.IntegerField(verbose_name='f. Think quickly?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_carry_heavy_objs',
            field=models.IntegerField(verbose_name='a. Carry heavy objects (e.g. bag of groceries)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_open_jar',
            field=models.IntegerField(verbose_name='c. Open a can or jar?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_pick_dime',
            field=models.IntegerField(verbose_name='e. Pick up a dime?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_tie_shoe_lace',
            field=models.IntegerField(verbose_name='d. Tie a shoe lace?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_turn_doorknob',
            field=models.IntegerField(verbose_name='b. Turn a doorknob?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_bed_chair',
            field=models.IntegerField(verbose_name='d. Move from a bed to a chair?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_climb_one_flight',
            field=models.IntegerField(verbose_name='g. Climb one flight of stairs?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_climb_several_flights',
            field=models.IntegerField(verbose_name='h. Climb several flights of stairs?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_in_out_car',
            field=models.IntegerField(verbose_name='i. Get in and out of a car?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_sitting',
            field=models.IntegerField(verbose_name='a. Stay sitting without losing your balance?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_standing',
            field=models.IntegerField(verbose_name='b. Stay standing without losing your balance?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_balance',
            field=models.IntegerField(verbose_name='c. Walk without losing your balance?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_fast',
            field=models.IntegerField(verbose_name='f. Walk fast?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_one_block',
            field=models.IntegerField(verbose_name='e. Walk one block?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_blame_mistakes',
            field=models.IntegerField(verbose_name='e. Blame yourself for mistakes that you made?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_burden',
            field=models.IntegerField(verbose_name='c. Feel that you are a burden to others?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_enjoy_things',
            field=models.IntegerField(verbose_name='f. Enjoy things as much as ever?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_nervous',
            field=models.IntegerField(verbose_name='g. Feel quite nervous?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_sad',
            field=models.IntegerField(verbose_name='a. Feel sad?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_worth_living',
            field=models.IntegerField(verbose_name='h. Feel that life is worth living?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_nobody_close',
            field=models.IntegerField(verbose_name='b. Feel that there is nobody you are close to?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_nothing_to_look_fwd',
            field=models.IntegerField(verbose_name='d. Feel that you have nothing to look forward to?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_smile_laugh',
            field=models.IntegerField(verbose_name='i. Smile and laugh at least once a day?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_arm',
            field=models.IntegerField(verbose_name='a. Arm that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_foot',
            field=models.IntegerField(verbose_name='d. Foot/ankle that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_hand',
            field=models.IntegerField(verbose_name='b. Grip of your hand that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_leg',
            field=models.IntegerField(verbose_name='c. Leg that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_active_recreation',
            field=models.IntegerField(verbose_name='d. Active recreation (sports, outings,travel)?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_control_life',
            field=models.IntegerField(verbose_name='g. Your ability to control your life as you wish?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_family',
            field=models.IntegerField(verbose_name='e. Your role as a family member and/or friend?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_help_others',
            field=models.IntegerField(verbose_name='h. Your ability to help others?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_quiet_recreation',
            field=models.IntegerField(verbose_name='c. Quiet recreation (crafts, reading)?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_social',
            field=models.IntegerField(verbose_name='b. Your social activities?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_spiritual',
            field=models.IntegerField(verbose_name='f. Your participation in spiritual or religious activities?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_work',
            field=models.IntegerField(verbose_name='a. Your work (paid, voluntary or other)', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo'), (-10000, 'NT')]),
        ),
    ]
