# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0018_auto_20160614_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_coord_speed_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles_pattelar_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_reflex_activity_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_extension_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_flexion_obs',
            field=models.TextField(max_length=500, null=True, verbose_name='Observa\xe7\xe3o', blank=True),
        ),
        migrations.AlterField(
            model_name='fim',
            name='baseevaluation_ptr',
            field=models.OneToOneField(primary_key=True, serialize=False, to='evaluation.BaseEvaluation'),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Scoring Dysmetria', choices=[(0, 'Dismetria evidente ou assistem\xe1tico'), (1, 'Dismetria leve ou sistem\xe1tica'), (2, 'Sem dismetria')]),
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
            name='le_reflex_activity_pattelar',
            field=models.IntegerField(verbose_name='Patellar', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa pode ser avaliada')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion sitting', choices=[(0, 'Sem movimento ativo'), (1, 'Com dosriflex\xe3o limitada'), (2, 'Completa dorsiflex\xe3o ativa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion sitting', choices=[(0, 'Sem movimento ativo'), (1, 'O joelho pode ativamente ser fletido at\xe9 90\xb0 (palpar os tend\xf5es dos flexores do joelho)'), (2, 'O joelho pode ser fletido al\xe9m de 90\xb0')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion standing', choices=[(0, 'Sem movimenta\xe7\xe3o ativa'), (1, 'Limita\xe7\xe3o de dorsiflex\xe3o'), (2, 'Dorsiflex\xe3o completa')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion standing', choices=[(0, 'O joelho n\xe3o pode ser fletido se o quadril n\xe3o \xe9 fletido simultaneamente'), (1, 'Menos do que 90\xb0 do joelho ou se realiza com flex\xe3o de quadril'), (2, 'At\xe9 90\xb0 de flex\xe3o sem flex\xe3o simultanea do quadril')]),
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
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to perform a spherical grasp by grasping a tennis ball The tester may support the patient\u2019s arm but may not assist with the hand function required for the retrieval task. Test this grip against resistance by asking the patient to hold as you attempt to pull the ball out with a slight tug. <strong>Hold the ball and keep it steady</strong>', verbose_name='Fingers in abduction/flexion, thumb opposed, tennis ball', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia')]),
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
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'Less than 15\xb0 active dorsiflexion'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Mant\xe9m 15\xb0 dorsiflex\xe3o contra resist\xeancia')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_90',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 90, forearm pronated shoulder at 0', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho ate 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Posi\xe7\xe3o pode ser mantida contra resist\xeancia (leve)')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='vol_mov_mix_hand_spine',
            field=models.IntegerField(verbose_name='M\xe3o \xe0 coluna lombar', choices=[(0, 'Nenhuma a\xe7\xe3o espec\xedfica realizada'), (1, 'A m\xe3o ultrapassa a espinha il\xedaca \xe2ntero-superior'), (2, 'A\xe7\xe3o realizada completamente (m\xe3o chega a coluna lombar)')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='vol_mov_mix_pron_sup',
            field=models.IntegerField(verbose_name='Prona\xe7\xe3o/Supina\xe7\xe3o antebra\xe7o cotovelo em 90 e ombro em 0', choices=[(0, 'Posi\xe7\xe3o correta do ombro e cotovelo n\xe3o pode ser atingida, e/ou prona\xe7\xe3o ou supina\xe7\xe3o n\xe3o pode ser realizada totalmente'), (1, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S'), (2, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='vol_mov_mix_shoulder_flex',
            field=models.IntegerField(verbose_name='Flex\xe3o de ombro 0 - 90, cotovelo 0 e antebra\xe7o prona\xe7\xe3o/ supina\xe7\xe3o (P/S)  0', choices=[(0, 'Imediata abdu\xe7\xe3o ombro e/ ou flex\xe3o de cotovelo'), (1, 'Abdu\xe7\xe3o e/ou  flex\xe3o de cotovelo durante o movimento'), (2, 'Flex\xe3o completa 90\xb0 e  mant\xe9m extens\xe3o cotovelo')]),
        ),
        migrations.AlterField(
            model_name='had',
            name='ease',
            field=models.IntegerField(verbose_name='I can sit at ease and feel relaxed', choices=[(3, 'Not at all'), (2, 'Not often'), (1, 'Usually'), (0, 'Definitely')]),
        ),
    ]
