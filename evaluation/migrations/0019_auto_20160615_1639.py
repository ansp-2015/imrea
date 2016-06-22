# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0018_auto_20160614_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamilton',
            fields=[
                ('baseevaluation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='evaluation.BaseEvaluation')),
                ('mood', models.IntegerField(verbose_name='depressed mood (sadness, hopeless, helpless, worthless)', choices=[(0, 'Absent'), (1, 'These feelings are indicated only on questioning'), (2, 'These feelings are spontaneously reported verbally'), (3, 'Communicates feelings non-verbally i.e., through facial expression, posture, voice, and tendency to weep'), (4, 'Patient reports VIRTUALLY ONLY these feelings in his spontaneous verbal and non-verbal communication')])),
                ('guilt', models.IntegerField(verbose_name='feelings of guilt', choices=[(0, 'Absent'), (1, 'Self reproach, feels he has let people down'), (2, 'Ideas of guilt or rumination over past errors or sinful deed'), (3, 'Present illness is a punishmnent. Delusions of guilt'), (4, 'Hears accusatory or denunciatory voices and/or experiences threatening visual hallucinations')])),
                ('suicide', models.IntegerField(verbose_name='suicide', choices=[(0, 'Absent'), (1, 'Feels life is not worth living'), (2, 'Wishes he were dead or any thoughts of possible death to self'), (3, 'Suicide ideas or gesture'), (4, 'Attempts at suicide (any serious attempt rates)')])),
                ('insomnia_early', models.IntegerField(verbose_name='insomnia early', choices=[(0, 'No difficulty falling asleep'), (1, 'Complains of occasional difficulty falling asleep - more than 1/2 hour'), (2, 'Complains of nightly difficulty falling asleep')])),
                ('insomnia_middle', models.IntegerField(verbose_name='insomnia middle', choices=[(0, 'No difficulty'), (1, 'Patient complains of being restless and disturbed during the night'), (2, 'Waking during the night - any getting out of bed (except for purposes of voiding)')])),
                ('insomnia_late', models.IntegerField(verbose_name='insomnia late', choices=[(0, 'No difficulty'), (1, 'Waking in early hours of the morning but goes back to sleep'), (2, 'Unable to fall asleep again if he gets out of bed')])),
                ('work', models.IntegerField(verbose_name='work and activities', choices=[(0, 'No difficulty'), (1, 'Thoughts and feelings of incapacity, fatigue or weakness related to activities (work or hobbies)'), (2, 'Loss of interest in activities (hobbies or work) - either directly reported by patient, or indirectly in listlessness, indecision and vacillation (feels he has to push himself to work or do activities)'), (3, 'Decrease in actual time spent in activities or decrease in productivity. In hospital, if patient does not spend at least three hours a day in activities (hospital job or hobbies) exclusive of ward chores'), (4, 'Stopped working because of present illness. In hospital, if patient engages in no activities except ward chores, or if patient fails to perform ward chores unassisted')])),
                ('retardation', models.IntegerField(verbose_name='retardation: psychomotor (slowness of thought and speech; impaired ability to concentrate; decreased motor activity)', choices=[(0, 'Normal speech and thought'), (1, 'Slight retardation at interview'), (2, 'Obvious retardation at interview'), (3, 'Interview difficult'), (4, 'Complete stupor')])),
                ('agitation', models.IntegerField(verbose_name='agitation', choices=[(0, 'None'), (1, 'Fidgetiness'), (2, 'Playing with hands, hair,etc'), (3, "Moving about, can't sit still"), (4, 'Hand wringing, nail biting, hair-pulling, biting of lips')])),
                ('anxiety_psychic', models.IntegerField(verbose_name='anxiety: psychic', choices=[(0, 'No difficulty'), (1, 'Subjective tension and irritability'), (2, 'Worrying about minor matters'), (3, 'Apprehensive attitude apparent in face or speech'), (4, 'Fears expressed without questioning')])),
                ('anxiety_somatic', models.IntegerField(verbose_name='anxiety: somatic (physiological concomitants of anxiety, such as - gastro-intestinal: dry mouth, wind, indigestion, diarrhea, cramps, belching. - cardio-vascular : palpitations, headaches. - respiratory: hyperventilation, sighing. - urinary frequency - sweating)', choices=[(0, 'Absent'), (1, 'Mild'), (2, 'Moderate'), (3, 'Severe'), (4, 'Incapacitating')])),
                ('gastro', models.IntegerField(verbose_name='somatic symptoms: gastrointestinal', choices=[(0, 'None'), (1, 'Loss of appetite but eating without staff encouragement. Heavy feelings in abdomen'), (2, 'Difficulty eating without staff urging. Requests or requires laxatives or medication for bowels or medication for gastro-intestinal symptoms')])),
                ('general', models.IntegerField(verbose_name='somatic symptoms: general', choices=[(0, 'None'), (1, 'Heaviness in limbs, back or head. Backaches, headache, muscle aches. Loss of energy and fatigability'), (2, 'Any clear-cut symptom')])),
                ('genital', models.IntegerField(verbose_name='genital symptoms (loss of libido, menstrual disturbances)', choices=[(0, 'Absent'), (1, 'Mild'), (2, 'Severe')])),
                ('hypochondriasis', models.IntegerField(verbose_name='hypochondriasis', choices=[(0, 'Not present'), (1, 'Self-absorption (bodily)'), (2, 'Preoccupation with health'), (3, 'Frequent complaints, requests for help, etc. ...'), (4, 'Hypochondriacal delusions')])),
                ('weight', models.IntegerField(verbose_name='loss of weight', choices=[(0, 'No weight loss'), (1, 'Probable weight loss associated with present illness (>500g/week)'), (2, 'Definite weight loss(>1kg/week)')])),
                ('insight', models.IntegerField(verbose_name='insight', choices=[(0, 'Not depressed (based on above items) OR Acknowledges being depressed and ill'), (1, 'Acknowledges illness but attributes cause to bad food, climate, overwork, virus, need for rest, etc.'), (2, 'Denies being ill at all')])),
            ],
            options={
                'verbose_name': 'Hamilton',
                'verbose_name_plural': 'Hamiltons',
            },
            bases=('evaluation.baseevaluation',),
        ),
        migrations.AlterField(
            model_name='had',
            name='ease',
            field=models.IntegerField(verbose_name='I can sit at ease and feel relaxed', choices=[(3, 'Not at all'), (2, 'Not often'), (1, 'Usually'), (0, 'Definitely')]),
        ),
    ]
