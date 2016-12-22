# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0020_auto_20161216_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epworth',
            name='car_passenger',
            field=models.IntegerField(verbose_name='As a passenger in a car for an hour without a break', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='car_traffic',
            field=models.IntegerField(verbose_name='In a car, while stopped for a few minutes in the traffic', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='lying_down',
            field=models.IntegerField(verbose_name='Lying down to rest in the afternoon when circumstances permit', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='sitting_inactive_public',
            field=models.IntegerField(verbose_name='Sitting, inactive in a public place (e.g. a theatre or a meeting)', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='sitting_quietly_lunch',
            field=models.IntegerField(verbose_name='Sitting quietly after a lunch without alcohol', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='sitting_reading',
            field=models.IntegerField(verbose_name='Sitting and reading', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='sitting_talking',
            field=models.IntegerField(verbose_name='Sitting and talking to someone', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='epworth',
            name='watching_tv',
            field=models.IntegerField(verbose_name='Watching TV', choices=[(0, 'would never doze'), (1, 'slight chance of dozing'), (2, 'moderate chance of dozing'), (3, 'high chance of dozing'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Scoring Dysmetria', choices=[(0, 'Dismetria evidente ou assistem\xe1tico'), (1, 'Dismetria leve ou sistem\xe1tica'), (2, 'Sem dismetria'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_time',
            field=models.IntegerField(verbose_name='Scoring Speed', choices=[(0, '6 segundos mais lento que o lado n\xe3o afetado'), (1, '2 a 5 segundos mais lento que o lado afetado'), (2, 'Menos de 2 segundos de diferen\xe7a'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_coord_speed_tremor',
            field=models.IntegerField(verbose_name='Scoring Tremor', choices=[(0, 'Tremor marcante'), (1, 'Tremor leve'), (2, 'Sem tremor'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles',
            field=models.IntegerField(verbose_name='Achilles', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa pode ser avaliada'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_achilles_pattelar',
            field=models.IntegerField(verbose_name='Achilles and patellar reflexes', choices=[(0, '2 ou 3 reflexos est\xe3o marcadamente hiperativos'), (1, '1 reflexo esta hiperativo ou 2 est\xe3o vivos'), (2, 'N\xe3o mais que um reflexo esta vivo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_reflex_activity_pattelar',
            field=models.IntegerField(verbose_name='Patellar', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa pode ser avaliada'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion sitting', choices=[(0, 'Sem movimento ativo'), (1, 'Com dosriflex\xe3o limitada'), (2, 'Completa dorsiflex\xe3o ativa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_mix_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion sitting', choices=[(0, 'Sem movimento ativo'), (1, 'O joelho pode ativamente ser fletido at\xe9 90\xb0 (palpar os tend\xf5es dos flexores do joelho)'), (2, 'O joelho pode ser fletido al\xe9m de 90\xb0'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_ankle',
            field=models.IntegerField(verbose_name='Ankle Dorsiflexion standing', choices=[(0, 'Sem movimenta\xe7\xe3o ativa'), (1, 'Limita\xe7\xe3o de dorsiflex\xe3o'), (2, 'Dorsiflex\xe3o completa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_no_syn_knee',
            field=models.IntegerField(verbose_name='Knee Flexion standing', choices=[(0, 'O joelho n\xe3o pode ser fletido se o quadril n\xe3o \xe9 fletido simultaneamente'), (1, 'Menos do que 90\xb0 do joelho ou se realiza com flex\xe3o de quadril'), (2, 'At\xe9 90\xb0 de flex\xe3o sem flex\xe3o simultanea do quadril'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_ankle_dorsiflexion',
            field=models.IntegerField(verbose_name='Ankle dorsiflexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_ankle_flexion',
            field=models.IntegerField(verbose_name='Ankle plantarflexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_adduction',
            field=models.IntegerField(verbose_name='Hip adduction', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_extension',
            field=models.IntegerField(verbose_name='Hip extension', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_hip_flexion',
            field=models.IntegerField(verbose_name='Hip flexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_knee_extension',
            field=models.IntegerField(verbose_name='Knee extension', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='le_vol_mov_syn_knee_flexion',
            field=models.IntegerField(verbose_name='Knee flexion', choices=[(0, 'N\xe3o realiza'), (1, 'Realiza parcialmente'), (2, 'Completamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_dysmetria',
            field=models.IntegerField(verbose_name='Dysmetria', choices=[(0, 'Pronunciada ou assistem\xe1tica'), (1, 'Leve e sistem\xe1tica'), (2, 'Nenhuma'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_time',
            field=models.IntegerField(verbose_name='Speed', choices=[(0, 'Mais do que 5 segundos mais lento do que o lado n\xe3o acometido'), (1, '2-5 segundos mais lento'), (2, 'Diferen\xe7a m\xe1xima de 01 segundo entre os lados'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_coord_speed_tremor',
            field=models.IntegerField(verbose_name='Tremor', choices=[(0, 'Pronunciada ou assistem\xe1tica'), (1, 'Leve e sistem\xe1tica'), (2, 'Nenhuma'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_cylinder_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to grasp a small can (placed upright on a table without stabilization) by opening the fingers and opposing the volar surfaces of the thumb and digits. The arm may be supported but the tester may not assist with hand function. Test this grip against resistance by asking the patient to hold as you attempt to pull the can out with a slight tug.<strong>Hold the object and keep it steady</strong>', verbose_name='Cylinder shaped object (small can)tug upward, opposition in digits I and II', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_flex_pip_dip',
            field=models.IntegerField(help_text='Hold my finger and keep it stuck between your fingers', verbose_name='Flexion in PIP and DIP (digits II-V)extension in MCP II-V', choices=[(0, 'A posi\xe7\xe3o requerida n\xe3o pode ser adquirida'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'A preens\xe3o pode ser mantida contra a resist\xeancia'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_mass_ext',
            field=models.IntegerField(help_text='Open your hand. The therapist can help get the starting position with your fingers in flexion', verbose_name='Mass flexion from full active or passive flexion', choices=[(0, 'N\xe3o ocorre extens\xe3o'), (1, 'O sujeito libera ativamente a flex\xe3o em massa'), (2, 'Extens\xe3o ativa completa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_mass_flex',
            field=models.IntegerField(help_text='Close your hand. The therapist can help get the starting position with your fingers in extension', verbose_name='Mass flexion from full active or passive extension', choices=[(0, 'Nenhuma flex\xe3o ocorre'), (1, 'Alguma flex\xe3o com ADM incompleta'), (2, 'Flex\xe3o ativa completa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_spherical_grip',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to perform a spherical grasp by grasping a tennis ball. The tester may support the patient\u2019s arm but may not assist with the hand function required for the retrieval task. Test this grip against resistance by asking the patient to hold as you attempt to pull the ball out with a slight tug. <strong>Hold the ball and keep it steady</strong>', verbose_name='Fingers in abduction/flexion, thumb opposed, tennis ball', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_thumb_adduction',
            field=models.IntegerField(help_text='Ask the patient to perform pure thumb adduction with the scrap of paper interposed between the thumb and first digit. Test this grip against resistance by asking the patient to hold as you attempt to pull the paper out with a slight tug. <strong>Hold the paper between the thumb and forefinger</strong>', verbose_name='Thumb adduction', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_hand_thumb_opposition',
            field=models.IntegerField(help_text='Subject is sitting with arm on bedside table. Instruct the patient to grasp a pen by opposing the thumb and index finger pads around the pen. The pen may not be stabilized by the therapist or the patient\u2019s other hand. Test this grip against resistance by asking the patient to hold as you attempt to pull the pencil out with a slight tug. <strong>Hold the pen and keep it steady</strong>', verbose_name='Opposition pulpa of the thumb against the pulpa of 2-nd finger,pencil, tug upward', choices=[(0, 'Fun\xe7\xe3o n\xe3o pode ser realizada'), (1, 'Mant\xe9m posi\xe7\xe3o sem resist\xeancia'), (2, 'Mant\xe9m posi\xe7\xe3o contra resit\xeancia'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_normal_reflex_activity',
            field=models.IntegerField(verbose_name='Normal reflex activity', choices=[(0, 'No m\xednimo dois dos tr\xeas reflexos f\xe1sicos s\xe3o marcadamente hiperativos'), (1, 'Um reflexo est\xe1 marcadamente hiperativo, ou no m\xednimo dois reflexos est\xe3o vivos'), (2, 'N\xe3o mais que um reflexo est\xe1 vivo, e nenhum est\xe1 hiperativo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_ext',
            field=models.IntegerField(verbose_name='Extensors: triceps', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa presente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_reflex_activity_flex',
            field=models.IntegerField(verbose_name='Flexors: biceps and finger flexors', choices=[(0, 'Sem atividade reflexa'), (2, 'Atividade reflexa presente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_hand_spine',
            field=models.IntegerField(verbose_name='M\xe3o \xe0 coluna lombar', choices=[(0, 'Nenhuma a\xe7\xe3o espec\xedfica realizada'), (1, 'A m\xe3o ultrapassa a espinha il\xedaca \xe2ntero-superior'), (2, 'A\xe7\xe3o realizada completamente (m\xe3o chega a coluna lombar)'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_pron_sup',
            field=models.IntegerField(verbose_name='Prona\xe7\xe3o/Supina\xe7\xe3o antebra\xe7o cotovelo em 90 e ombro em 0', choices=[(0, 'Posi\xe7\xe3o correta do ombro e cotovelo n\xe3o pode ser atingida, e/ou prona\xe7\xe3o ou supina\xe7\xe3o n\xe3o pode ser realizada totalmente'), (1, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S'), (2, 'Mant\xe9m posi\xe7\xe3o com P/S completa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_mix_shoulder_flex',
            field=models.IntegerField(verbose_name='Flex\xe3o de ombro 0 - 90, cotovelo 0 e antebra\xe7o prona\xe7\xe3o/ supina\xe7\xe3o (P/S)  0', choices=[(0, 'Imediata abdu\xe7\xe3o ombro e/ ou flex\xe3o de cotovelo'), (1, 'Abdu\xe7\xe3o e/ou  flex\xe3o de cotovelo durante o movimento'), (2, 'Flex\xe3o completa 90\xb0 e  mant\xe9m extens\xe3o cotovelo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_pron_sup',
            field=models.IntegerField(verbose_name='Prona\xe7\xe3o/Supina\xe7\xe3o antebra\xe7o cotovelo em 90 e ombro em 0', choices=[(0, 'Posi\xe7\xe3o inicial n\xe3o pode ser alcan\xe7ada e/ou n\xe3o realiza P/S'), (1, 'Mant\xe9m posi\xe7\xe3o com ADM limitada de P/S'), (2, 'Mant\xe9m posi\xe7\xe3o com P/S completa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_shoulder_abd',
            field=models.IntegerField(verbose_name='Abdu\xe7\xe3o do ombro a 90 com o cotovelo 0 e antebra\xe7o em prona\xe7\xe3o', choices=[(0, 'Imediata supina\xe7\xe3o e/ ou flex\xe3o de cotovelo'), (1, 'Supina\xe7\xe3o e/ou flex\xe3o de cotovelo durante o movimento'), (2, 'Abdu\xe7\xe3o completa 90 e mant\xe9m extens\xe3o cotovelo e prona\xe7\xe3o'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_no_syn_shoulder_flex',
            field=models.IntegerField(verbose_name='Flex\xe3o do ombro de 90 - 180, cotovelo em 0, e antebra\xe7o P/S em 0', choices=[(0, 'Imediata abdu\xe7\xe3o ombro e/ ou flex\xe3o de cotovelo'), (1, 'Abdu\xe7\xe3o e/ou flex\xe3o de cotovelo durante o movimento'), (2, 'Flex\xe3o completa 90 e mant\xe9m extens\xe3o cotovelo'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_elbow',
            field=models.IntegerField(verbose_name='Cotovelo - extens\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_forearm',
            field=models.IntegerField(verbose_name='Antebra\xe7o - prona\xe7\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_ext_shoulder',
            field=models.IntegerField(verbose_name='Ombro - adu\xe7\xe3o e rota\xe7\xe3o interna', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_elbow_flex',
            field=models.IntegerField(verbose_name='Cotovelo - Flex\xe3o de cotovelo', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_forearm_sup',
            field=models.IntegerField(verbose_name='Antebra\xe7o - supina\xe7\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_abd',
            field=models.IntegerField(verbose_name='Ombro - Abdu\xe7\xe3o 90\xb0', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_elev',
            field=models.IntegerField(verbose_name='Ombro - eleva\xe7\xe3o', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_retrac',
            field=models.IntegerField(verbose_name='Ombro - Retra\xe7\xe3o de ombro', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_vol_mov_syn_flex_shoulder_rot',
            field=models.IntegerField(verbose_name='Ombro - Rota\xe7\xe3o externa', choices=[(0, 'Tarefa n\xe3o pode ser realizada completamente '), (1, 'Tarefa pode ser realizada parcialmente'), (2, 'Tarefa \xe9 realizada perfeitamente'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_circumduction',
            field=models.IntegerField(verbose_name='Circumduction', choices=[(0, 'N\xe3o realiza movimento ativo'), (1, 'Movimento incompleto e/ou movimentos oscilantes'), (2, 'Movimento completo, com exatid\xe3o'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_flex_elbow_0',
            field=models.IntegerField(verbose_name='Repeated dorsifexion / volar flexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'N\xe3o ocorre movimento volunt\xe1rio'), (1, 'Movimento ativo com ADM incompleta'), (2, 'Movimento ativo com ADM completa'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_flex_elbow_90',
            field=models.IntegerField(verbose_name='Repeated dorsifexion / volar flexion elbow at 90, forearm pronated shoulder at 0, slight finger flexion', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho ate 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Posi\xe7\xe3o pode ser mantida contra resist\xeancia (leve)'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_0',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 0, forearm pronated slight shoulder flexion/abduction', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho at\xe9 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Mant\xe9m 15\xb0 dorsiflex\xe3o contra resist\xeancia'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='fuglmeyer',
            name='ue_wrist_stab_elbow_90',
            field=models.IntegerField(verbose_name='Stability at 15 dorsiflexion elbow at 90, forearm pronated shoulder at 0', choices=[(0, 'Sujeito n\xe3o pode dorsifletir o punho ate 15\xb0'), (1, 'Alcan\xe7a 15\xb0 dorsiflex\xe3o sem resist\xeancia'), (2, 'Posi\xe7\xe3o pode ser mantida contra resist\xeancia (leve)'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='attention_calc',
            field=models.IntegerField(help_text='Subtrair 100-7, 7 vezes sucessivamente ( ponto para cada c\xe1lculo correto)<br>Alternativamente, soletrar MUNDO de tr\xe1s para frente.', verbose_name='Aten\xe7\xe3o e c\xe1lculo', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_command',
            field=models.IntegerField(verbose_name="Comando: 'pegue este papel com a m\xe3o direita dobre ao meio e coloque no ch\xe3o' (3 pontos)", choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_copy',
            field=models.IntegerField(verbose_name='Copiar um desenho (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_read',
            field=models.IntegerField(verbose_name="Ler e obedecer 'feche os olhos' (1 ponto)", choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_repeat',
            field=models.IntegerField(verbose_name="Repetir 'nem aqui, nem ali, nem l\xe1' (1 ponto)", choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_watch_pen',
            field=models.IntegerField(verbose_name='Nomear um rel\xf3gio e uma caneta (2 pontos)', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='language_write',
            field=models.IntegerField(verbose_name='Escrever uma frase (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_city',
            field=models.IntegerField(verbose_name='Cidade (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_day_month',
            field=models.IntegerField(verbose_name='Dia do m\xeas (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_district',
            field=models.IntegerField(verbose_name='Bairro ou rua pr\xf3xima (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_institution',
            field=models.IntegerField(verbose_name='Institui\xe7\xe3o (resid\xeancia, hospital, cl\xednica) (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_month',
            field=models.IntegerField(verbose_name='M\xeas (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_place',
            field=models.IntegerField(verbose_name='Local espec\xedfico (aposento ou setor) (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_state',
            field=models.IntegerField(verbose_name='Estado (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_time',
            field=models.IntegerField(verbose_name='Hora aproximada (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='orientation_year',
            field=models.IntegerField(verbose_name='Ano (1 ponto)', choices=[(0, b'0'), (1, b'1'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='recall_words',
            field=models.IntegerField(help_text='Pergunte pelas 3 palavras ditas anteriormente (1 ponto por palavra)', verbose_name='Evoca\xe7\xe3o', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='mmse',
            name='registration_words',
            field=models.IntegerField(help_text='Fale 3 palavras n\xe3o relacionadas. Posteriormente pergunte ao paciente pelas 3 palavras. D\xea 1 ponto para cada palavra certa. <br>Depois repita as palavras e certifique-se de que o paciente as aprendeu, pois mais adiante voc\xea ir\xe1 pergunt\xe1-las novamente', verbose_name='Mem\xf3ria imediata', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='best_gaze',
            field=models.IntegerField(verbose_name='2. Best Gaze', choices=[(0, 'Normal.'), (1, 'Partial gaze palsy; gaze is abnormal in one or both eyes, but forced deviation or total gaze paresis is not present.'), (2, 'Forced deviation, or total gaze paresis not overcome by the oculocephalic maneuver.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='best_language',
            field=models.IntegerField(verbose_name='9. Best Language', choices=[(0, 'No aphasia; normal.'), (1, "Mild-to-moderate aphasia; some obvious loss of fluency or facility of comprehension, without significant limitation on ideas expressed or form of expression. Reduction of speech and/or comprehension, however, makes conversation about provided materials difficult or impossible. For example, in conversation about provided materials, examiner can identify picture or naming card content from patient's response."), (2, 'Severe aphasia; all communication is through fragmentary expression; great need for inference, questioning, and guessing by the listener. Range of information that can be exchanged is limited; listener carries burden of communication. Examiner cannot identify materials provided from patient response.'), (3, 'Mute, global aphasia; no usable speech or auditory comprehension.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='dysarthria',
            field=models.IntegerField(verbose_name='10. Dysarthria', choices=[(0, 'Normal.'), (1, 'Mild-to-moderate dysarthria; patient slurs at least some words and, at worst, can be understood with some difficulty.'), (2, "Severe dysarthria; patient's speech is so slurred as to be unintelligible in the absence of or out of proportion to any dysphasia, or is mute/anarthric."), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='extinction',
            field=models.IntegerField(verbose_name='11. Extinction and Inattention (formerly Neglect)', choices=[(0, 'No abnormality.'), (1, 'Visual, tactile, auditory, spatial, or personal inattention or extinction to bilateral simultaneous stimulation in one of the sensory modalities.'), (2, 'Profound hemi-inattention or extinction to more than one modality; does not recognize own hand or orients to only one side of space. '), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='facial_palsy',
            field=models.IntegerField(verbose_name='4. Facial Palsy', choices=[(0, 'Normal symmetrical movements.'), (1, 'Minor paralysis (flattened nasolabial fold, asymmetry on smiling).'), (2, 'Partial paralysis (total or near-total paralysis of lower face).'), (3, 'Complete paralysis of one or both sides (absence of facial movement in the upper and lower face). '), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='limb_ataxia',
            field=models.IntegerField(verbose_name='7. Limb Ataxia', choices=[(0, 'Absent.'), (1, 'Present in one limb.'), (2, 'Present in two limbs.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='loc',
            field=models.IntegerField(verbose_name='1a. Level of Consciousness', choices=[(0, 'Alert; keenly responsive.'), (1, 'Not alert; but arousable by minor stimulation to obey, answer, or respond.'), (2, 'Not alert; requires repeated stimulation to attend, or is obtunded and requires strong or painful stimulation to make movements (not stereotyped).'), (3, 'Responds only with reflex motor or autonomic effects or totally unresponsive, flaccid, and areflexic.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='loc_commands',
            field=models.IntegerField(verbose_name='1c. LOC Commands', choices=[(0, 'Performs both tasks correctly.'), (1, 'Performs one task correctly.'), (2, 'Performs neither task correctly.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='loc_questions',
            field=models.IntegerField(verbose_name='1b. LOC Questions', choices=[(0, 'Answers both questions correctly.'), (1, 'Answers one question correctly.'), (2, 'Answers neither question correctly.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_arm_left',
            field=models.IntegerField(verbose_name='5. Motor arm', choices=[(0, 'No drift; limb holds 90 (or 45) degrees for full 10 seconds.'), (1, 'Drift; limb holds 90 (or 45) degrees, but drifts down before full 10 seconds; does not hit bed or other support.'), (2, 'Some effort against gravity; limb cannot get to or maintain (if cued) 90 (or 45) degrees, drifts down to bed, but has some effort against gravity.'), (3, 'No effort against gravity; limb falls.'), (4, 'No movement'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_arm_right',
            field=models.IntegerField(choices=[(0, 'No drift; limb holds 90 (or 45) degrees for full 10 seconds.'), (1, 'Drift; limb holds 90 (or 45) degrees, but drifts down before full 10 seconds; does not hit bed or other support.'), (2, 'Some effort against gravity; limb cannot get to or maintain (if cued) 90 (or 45) degrees, drifts down to bed, but has some effort against gravity.'), (3, 'No effort against gravity; limb falls.'), (4, 'No movement'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_leg_left',
            field=models.IntegerField(verbose_name='6. Motor leg', choices=[(0, 'No drift; leg holds 30-degree position for full 5 seconds.'), (1, 'Drift; leg falls by the end of the 5-second period but does not hit bed.'), (2, 'Some effort against gravity; leg falls to bed by 5 seconds, but has some effort against gravity.'), (3, 'No effort against gravity; leg falls to bed immediately.'), (4, 'No movement.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='motor_leg_right',
            field=models.IntegerField(choices=[(0, 'No drift; leg holds 30-degree position for full 5 seconds.'), (1, 'Drift; leg falls by the end of the 5-second period but does not hit bed.'), (2, 'Some effort against gravity; leg falls to bed by 5 seconds, but has some effort against gravity.'), (3, 'No effort against gravity; leg falls to bed immediately.'), (4, 'No movement.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='sensory',
            field=models.IntegerField(verbose_name='8. Sensory', choices=[(0, 'Normal; no sensory loss.'), (1, 'Mild-to-moderate sensory loss; patient feels pinprick is less sharp or is dull on the affected side; or there is a loss of superficial pain with pinprick, but patient is aware of being touched.'), (2, 'Severe to total sensory loss; patient is not aware of being touched in the face, arm, and leg.'), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='nihss',
            name='visual',
            field=models.IntegerField(verbose_name='3. Visual', choices=[(0, 'No visual loss.'), (1, 'Partial hemianopia.'), (2, 'Complete hemianopia.'), (3, 'Bilateral hemianopia (blind including cortical blindness). '), (-10000, 'NT')]),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer1_forearm_left',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer1_forearm_right',
            field=models.DecimalField(verbose_name='(Pain) Algometer 1', max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer1_thenar_left',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer1_thenar_right',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer2_forearm_left',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer2_forearm_right',
            field=models.DecimalField(verbose_name='(Pain) Algometer 2', max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer2_thenar_left',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer2_thenar_right',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer3_forearm_left',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer3_forearm_right',
            field=models.DecimalField(verbose_name='(Pain) Algometer 3', max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer3_thenar_left',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='algometer3_thenar_right',
            field=models.DecimalField(max_digits=7, decimal_places=1),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility1_forearm_left',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility1_forearm_right',
            field=models.DecimalField(verbose_name='Sensibility 1', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility1_thenar_left',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility1_thenar_right',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility2_forearm_left',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility2_forearm_right',
            field=models.DecimalField(verbose_name='Sensibility 2', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility2_thenar_left',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vonfrey',
            name='sensibility2_thenar_right',
            field=models.DecimalField(max_digits=7, decimal_places=2),
        ),
    ]
