# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import evaluation.models.eeg


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_auto_20160726_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='EegFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=evaluation.models.eeg.user_directory_path, verbose_name='File')),
            ],
            options={
                'verbose_name': 'EEG File',
                'verbose_name_plural': 'EEG Files',
            },
        ),
        migrations.AlterModelOptions(
            name='eeg',
            options={'verbose_name': 'EEG', 'verbose_name_plural': 'EEGs'},
        ),
        migrations.RemoveField(
            model_name='eeg',
            name='eegfile',
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
            field=models.IntegerField(verbose_name='c. Bathe yourself?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_clip_toenails',
            field=models.IntegerField(verbose_name='d. Clip your toenails?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_control_bladder',
            field=models.IntegerField(verbose_name='f. Control your bladder (not have an accident)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_control_bowels',
            field=models.IntegerField(verbose_name='g. Control your bowels (not have an accident)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_cut_food',
            field=models.IntegerField(verbose_name='a. Cut your food with a knife and fork?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_dress',
            field=models.IntegerField(verbose_name='b. Dress the top part of your body?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_heavy_household',
            field=models.IntegerField(verbose_name='j. Do heavy household chores (e.g.vacuum, laundry or yard work)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_light_household',
            field=models.IntegerField(verbose_name='h. Do light household tasks/chores(e.g. dust, make a bed, take out garbage, do the dishes)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_shopping',
            field=models.IntegerField(verbose_name='i. Go shopping?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='activities_toilet',
            field=models.IntegerField(verbose_name='e. Get to the toilet on time?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_group_conversation',
            field=models.IntegerField(verbose_name='e. Participate in a conversation with a group of people?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_name_objs',
            field=models.IntegerField(verbose_name='d. Correctly name objects?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_reply',
            field=models.IntegerField(verbose_name='c. Reply to questions?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_say_name',
            field=models.IntegerField(verbose_name='a. Say the name of someone who was in front of you?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_tel_call',
            field=models.IntegerField(verbose_name='g. Call another person on the telephone, including selecting the correct phone number and dialing?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_tel_conversation',
            field=models.IntegerField(verbose_name='f. Have a conversation on the telephone? ', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='communication_understand',
            field=models.IntegerField(verbose_name='b. Understand what was being said to you in a conversation?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_concentrate',
            field=models.IntegerField(verbose_name='e. Concentrate?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_day_week',
            field=models.IntegerField(verbose_name='d. Remember the day of the week?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_do_things',
            field=models.IntegerField(verbose_name='c. Remember to do things (e.g. keep scheduled appointments or take medication)?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_happ_day_bef',
            field=models.IntegerField(verbose_name='b. Remember things that happened the day before?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_remember_ppl_told',
            field=models.IntegerField(verbose_name='a. Remember things that people just told you?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_solve_problems',
            field=models.IntegerField(verbose_name='g. Solve everyday problems?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='dificulty_think_quickly',
            field=models.IntegerField(verbose_name='f. Think quickly?', choices=[(5, 'nada dic\xedfil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'extremamente dif\xedcil')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_carry_heavy_objs',
            field=models.IntegerField(verbose_name='a. Carry heavy objects (e.g. bag of groceries)?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_open_jar',
            field=models.IntegerField(verbose_name='c. Open a can or jar?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_pick_dime',
            field=models.IntegerField(verbose_name='e. Pick up a dime?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_tie_shoe_lace',
            field=models.IntegerField(verbose_name='d. Tie a shoe lace?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='hand_turn_doorknob',
            field=models.IntegerField(verbose_name='b. Turn a doorknob?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_bed_chair',
            field=models.IntegerField(verbose_name='d. Move from a bed to a chair?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_climb_one_flight',
            field=models.IntegerField(verbose_name='g. Climb one flight of stairs?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_climb_several_flights',
            field=models.IntegerField(verbose_name='h. Climb several flights of stairs?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_in_out_car',
            field=models.IntegerField(verbose_name='i. Get in and out of a car?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_sitting',
            field=models.IntegerField(verbose_name='a. Stay sitting without losing your balance?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_standing',
            field=models.IntegerField(verbose_name='b. Stay standing without losing your balance?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_balance',
            field=models.IntegerField(verbose_name='c. Walk without losing your balance?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_fast',
            field=models.IntegerField(verbose_name='f. Walk fast?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mobile_walk_one_block',
            field=models.IntegerField(verbose_name='e. Walk one block?', choices=[(5, 'nada dif\xedcil'), (4, 'um pouco dif\xedcil'), (3, 'mais ou menos dif\xedcil'), (2, 'muito dif\xedcil'), (1, 'n\xe3o consigo realizar')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_blame_mistakes',
            field=models.IntegerField(verbose_name='e. Blame yourself for mistakes that you made?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_burden',
            field=models.IntegerField(verbose_name='c. Feel that you are a burden to others?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_enjoy_things',
            field=models.IntegerField(verbose_name='f. Enjoy things as much as ever?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_nervous',
            field=models.IntegerField(verbose_name='g. Feel quite nervous?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_sad',
            field=models.IntegerField(verbose_name='a. Feel sad?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_feel_worth_living',
            field=models.IntegerField(verbose_name='h. Feel that life is worth living?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_nobody_close',
            field=models.IntegerField(verbose_name='b. Feel that there is nobody you are close to?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_nothing_to_look_fwd',
            field=models.IntegerField(verbose_name='d. Feel that you have nothing to look forward to?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='mood_smile_laugh',
            field=models.IntegerField(verbose_name='i. Smile and laugh at least once a day?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_arm',
            field=models.IntegerField(verbose_name='a. Arm that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_foot',
            field=models.IntegerField(verbose_name='d. Foot/ankle that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_hand',
            field=models.IntegerField(verbose_name='b. Grip of your hand that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='strength_leg',
            field=models.IntegerField(verbose_name='c. Leg that was most affected', choices=[(5, 'muita for\xe7a'), (4, 'um pouco de for\xe7a'), (3, 'alguma for\xe7a'), (2, 'minima for\xe7a'), (1, 'nenhuma for\xe7a')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_active_recreation',
            field=models.IntegerField(verbose_name='d. Active recreation (sports, outings,travel)?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_control_life',
            field=models.IntegerField(verbose_name='g. Your ability to control your life as you wish?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_family',
            field=models.IntegerField(verbose_name='e. Your role as a family member and/or friend?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_help_others',
            field=models.IntegerField(verbose_name='h. Your ability to help others?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_quiet_recreation',
            field=models.IntegerField(verbose_name='c. Quiet recreation (crafts, reading)?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_social',
            field=models.IntegerField(verbose_name='b. Your social activities?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_spiritual',
            field=models.IntegerField(verbose_name='f. Your participation in spiritual or religious activities?', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AlterField(
            model_name='sis',
            name='time_work',
            field=models.IntegerField(verbose_name='a. Your work (paid, voluntary or other)', choices=[(5, 'nenhuma vez'), (4, 'poucas vezes'), (3, 'algumas vezes'), (2, 'a maioria das vezes'), (1, 'todo o tempo')]),
        ),
        migrations.AddField(
            model_name='eegfile',
            name='eeg',
            field=models.ForeignKey(default=None, to='evaluation.Eeg'),
        ),
    ]
