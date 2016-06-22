# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from . import BaseEvaluation 

class Hamilton(BaseEvaluation):
    """
    Hamilton Test
    """

    MOOD = (
        (0, _('Absent')),
        (1, _('These feelings are indicated only on questioning')),
        (2, _('These feelings are spontaneously reported verbally')),
        (3, _('Communicates feelings non-verbally i.e., through facial expression, posture, voice, and tendency to '
              'weep')),
        (4, _('Patient reports VIRTUALLY ONLY these feelings in his spontaneous verbal and non-verbal communication')),
    )
    mood = models.IntegerField(_('depressed mood (sadness, hopeless, helpless, worthless)'), choices=MOOD)

    GUILT = (
        (0, _('Absent')),
        (1, _('Self reproach, feels he has let people down')),
        (2, _('Ideas of guilt or rumination over past errors or sinful deed')),
        (3, _('Present illness is a punishmnent. Delusions of guilt')),
        (4, _('Hears accusatory or denunciatory voices and/or experiences threatening visual hallucinations')),
    )
    guilt = models.IntegerField(_('feelings of guilt'), choices=GUILT)

    SUICIDE = (
        (0, _('Absent')),
        (1, _('Feels life is not worth living')),
        (2, _('Wishes he were dead or any thoughts of possible death to self')),
        (3, _('Suicide ideas or gesture')),
        (4, _('Attempts at suicide (any serious attempt rates)')),
    )
    suicide = models.IntegerField(_('suicide'), choices=SUICIDE)

    INSOMINIA_EARLY = (
        (0, _('No difficulty falling asleep')),
        (1, _('Complains of occasional difficulty falling asleep - more than 1/2 hour')),
        (2, _('Complains of nightly difficulty falling asleep')),
    )
    insomnia_early = models.IntegerField(_('insomnia early'), choices=INSOMINIA_EARLY)

    INSOMINIA_MIDDLE = (
        (0, _('No difficulty')),
        (1, _('Patient complains of being restless and disturbed during the night')),
        (2, _('Waking during the night - any getting out of bed (except for purposes of voiding)')),
    )
    insomnia_middle = models.IntegerField(_('insomnia middle'), choices=INSOMINIA_MIDDLE)

    INSOMINIA_LATE = (
        (0, _('No difficulty')),
        (1, _('Waking in early hours of the morning but goes back to sleep')),
        (2, _('Unable to fall asleep again if he gets out of bed')),
    )
    insomnia_late = models.IntegerField(_('insomnia late'), choices=INSOMINIA_LATE)

    WORK = (
        (0, _('No difficulty')),
        (1, _('Thoughts and feelings of incapacity, fatigue or weakness related to activities (work or hobbies)')),
        (2, _('Loss of interest in activities (hobbies or work) - either directly reported by patient, or indirectly '
              'in listlessness, indecision and vacillation (feels he has to push himself to work or do activities)')),
        (3, _('Decrease in actual time spent in activities or decrease in productivity. In hospital, if patient does '
              'not spend at least three hours a day in activities (hospital job or hobbies) exclusive of ward chores')),
        (4, _('Stopped working because of present illness. In hospital, if patient engages in no activities except '
              'ward chores, or if patient fails to perform ward chores unassisted')),
    )
    work = models.IntegerField(_('work and activities'), choices=WORK)

    RETARDATION = (
        (0, _('Normal speech and thought')),
        (1, _('Slight retardation at interview')),
        (2, _('Obvious retardation at interview')),
        (3, _('Interview difficult')),
        (4, _('Complete stupor')),
    )
    retardation = models.IntegerField(_('retardation: psychomotor (slowness of thought and speech; impaired ability to concentrate; decreased motor activity)'), choices=RETARDATION)

    AGITATION = (
        (0, _('None')),
        (1, _('Fidgetiness')),
        (2, _('Playing with hands, hair,etc')),
        (3, _('Moving about, can\'t sit still')),
        (4, _('Hand wringing, nail biting, hair-pulling, biting of lips')),
    )
    agitation = models.IntegerField(_('agitation'), choices=AGITATION)

    ANXIETY_PSYCHIC = (
        (0, _('No difficulty')),
        (1, _('Subjective tension and irritability')),
        (2, _('Worrying about minor matters')),
        (3, _('Apprehensive attitude apparent in face or speech')),
        (4, _('Fears expressed without questioning')),
    )
    anxiety_psychic = models.IntegerField(_('anxiety: psychic'), choices=ANXIETY_PSYCHIC)

    ANXIETY_SOMATIC = (
        (0, _('Absent')),
        (1, _('Mild')),
        (2, _('Moderate')),
        (3, _('Severe')),
        (4, _('Incapacitating')),
    )
    anxiety_somatic = models.IntegerField(_('anxiety: somatic (physiological concomitants of anxiety, such as - gastro-intestinal: dry mouth, wind, indigestion, diarrhea, cramps, belching. - cardio-vascular : palpitations, headaches. - respiratory: hyperventilation, sighing. - urinary frequency - sweating)'), choices=ANXIETY_SOMATIC)

    GASTRO = (
        (0, _('None')),
        (1, _('Loss of appetite but eating without staff encouragement. Heavy feelings in abdomen')),
        (2, _('Difficulty eating without staff urging. Requests or requires laxatives or medication for bowels or medication for gastro-intestinal symptoms')),
    )
    gastro = models.IntegerField(_('somatic symptoms: gastrointestinal'), choices=GASTRO)

    GENERAL = (
        (0, _('None')),
        (1, _('Heaviness in limbs, back or head. Backaches, headache, muscle aches. Loss of energy and fatigability')),
        (2, _('Any clear-cut symptom')),
    )
    general = models.IntegerField(_('somatic symptoms: general'), choices=GENERAL)

    GENITAL = (
        (0, _('Absent')),
        (1, _('Mild')),
        (2, _('Severe')),
    )
    genital = models.IntegerField(_('genital symptoms (loss of libido, menstrual disturbances)'), choices=GENITAL)

    HYPOCHONDRIASIS = (
        (0, _('Not present')),
        (1, _('Self-absorption (bodily)')),
        (2, _('Preoccupation with health')),
        (3, _('Frequent complaints, requests for help, etc. ...')),
        (4, _('Hypochondriacal delusions')),
    )
    hypochondriasis = models.IntegerField(_('hypochondriasis'), choices=HYPOCHONDRIASIS)

    WEIGHT_HISTORY = (
        (0, _('No weight loss')),
        (1, _('Probable weight loss associated with present illness')),
        (2, _('Definite (according to patient) weight loss')),
        (3, _('Not assessed')),
    )
    weight_history = models.IntegerField(_('loss of weight'), choices=WEIGHT_HISTORY)

    WEIGHT_WEEKLY = (
        (0, _('No weight loss')),
        (1, _('Probable weight loss associated with present illness (>500g/week)')),
        (2, _('Definite weight loss(>1kg/week)')),
    )
    weight_weekly = models.IntegerField(_('loss of weight'), choices=WEIGHT_WEEKLY)

    INSIGHT = (
        (0, _('Not depressed (based on above items) OR Acknowledges being depressed and ill')),
        (1, _('Acknowledges illness but attributes cause to bad food, climate, overwork, virus, need for rest, etc.')),
        (2, _('Denies being ill at all')),
    )
    insight = models.IntegerField(_('insight'), choices=INSIGHT)

    class Meta:
        verbose_name = _('Hamilton')
        verbose_name_plural = _('Hamiltons')