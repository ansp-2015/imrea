# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from . import BaseEvaluation


class NIHSS(BaseEvaluation):
    """
    National Institutes of Health Stroke Scale
    """

    NIH_LOC = (
        (0, _('Alert; keenly responsive.')),
        (1, _('Not alert; but arousable by minor stimulation to obey, answer, or respond.')),
        (2, _('Not alert; requires repeated stimulation to attend, or is obtunded and requires strong or painful '
                'stimulation to make movements (not stereotyped).')),
        (3, _('Responds only with reflex motor or autonomic effects or totally unresponsive, flaccid, and areflexic.')),
    )
    loc = models.IntegerField(_('1a. Level of Consciousness'), choices=NIH_LOC)

    NIH_LOC_QUESTIONS = (
        (0, _('Answers both questions correctly.')),
        (1, _('Answers one question correctly.')),
        (2, _('Answers neither question correctly.')),
    )
    loc_questions = models.IntegerField(_('1b. LOC Questions'), choices=NIH_LOC_QUESTIONS)

    NIH_LOC_COMMANDS = (
        (0, _('Performs both tasks correctly.')),
        (1, _('Performs one task correctly.')),
        (2, _('Performs neither task correctly.')),
    )
    loc_commands = models.IntegerField(_('1c. LOC Commands'), choices=NIH_LOC_COMMANDS)

    NIH_BEST_GAZE = (
        (0, _('Normal.')),
        (1, _('Partial gaze palsy; gaze is abnormal in one or both eyes, but forced deviation or total gaze paresis '
              'is not present.')),
        (2, _('Forced deviation, or total gaze paresis not overcome by the oculocephalic maneuver.')),
    )
    best_gaze = models.IntegerField(_('2. Best Gaze'), choices=NIH_BEST_GAZE)

    NIH_VISUAL = (
        (0, _('No visual loss.')),
        (1, _('Partial hemianopia.')),
        (2, _('Complete hemianopia.')),
        (3, _('Bilateral hemianopia (blind including cortical blindness). ')),
    )
    visual = models.IntegerField(_('3. Visual'), choices=NIH_VISUAL)

    NIH_FACIAL_PALSY = (
        (0, _('Normal symmetrical movements.')),
        (1, _('Minor paralysis (flattened nasolabial fold, asymmetry on smiling).')),
        (2, _('Partial paralysis (total or near-total paralysis of lower face).')),
        (3, _('Complete paralysis of one or both sides (absence of facial movement in the upper and lower face). ')),
    )
    facial_palsy = models.IntegerField(_('4. Facial Palsy'), choices=NIH_FACIAL_PALSY)

    # TODO: Field for explain if unstestable
    NIH_MOTOR_ARM = (
        (0, _('No drift; limb holds 90 (or 45) degrees for full 10 seconds.')),
        (1, _('Drift; limb holds 90 (or 45) degrees, but drifts down before full 10 seconds; does not hit bed or '
              'other support.')),
        (2, _('Some effort against gravity; limb cannot get to or maintain (if cued) 90 (or 45) degrees, drifts down '
              'to bed, but has some effort against gravity.')),
        (3, _('No effort against gravity; limb falls.')),
        (4, _('No movement')),
    )
    motor_arm_left = models.IntegerField(_('5a. Left arm'), choices=NIH_MOTOR_ARM)
    motor_arm_right = models.IntegerField(_('5b. Right arm'), choices=NIH_MOTOR_ARM)

    NIH_MOTOR_LEG = (
        (0, _('No drift; leg holds 30-degree position for full 5 seconds.')),
        (1, _('Drift; leg falls by the end of the 5-second period but does not hit bed.')),
        (2, _('Some effort against gravity; leg falls to bed by 5 seconds, but has some effort against gravity.')),
        (3, _('No effort against gravity; leg falls to bed immediately.')),
        (4, _('No movement.')),
    )
    motor_leg_left = models.IntegerField(_('6a. Left leg'), choices=NIH_MOTOR_LEG)
    motor_leg_right = models.IntegerField(_('6b. Right leg'), choices=NIH_MOTOR_LEG)

    NIH_LIMB_ATAXIA = (
        (0, _('Absent.')),
        (1, _('Present in one limb.')),
        (2, _('Present in two limbs.')),
    )
    limb_ataxia = models.IntegerField(_('7. Limb Ataxia'), choices=NIH_LIMB_ATAXIA)

    NIH_SENSORY = (
        (0, _('Normal; no sensory loss.')),
        (1, _('Mild-to-moderate sensory loss; patient feels pinprick is less sharp or is dull on the affected side; or '
              'there is a loss of superficial pain with pinprick, but patient is aware of being touched.')),
        (2, _('Severe to total sensory loss; patient is not aware of being touched in the face, arm, and leg.')),
    )
    sensory = models.IntegerField(_('8. Sensory'), choices=NIH_SENSORY)

    NIH_BEST_LANGUAGE = (
        (0, _('No aphasia; normal.')),
        (1, _('Mild-to-moderate aphasia; some obvious loss of fluency or facility of comprehension, without '
              'significant limitation on ideas expressed or form of expression. Reduction of speech and/or '
              'comprehension, however, makes conversation about provided materials difficult or impossible. '
              'For example, in conversation about provided materials, examiner can identify picture or naming card '
              'content from patient\'s response.')),
        (2, _('Severe aphasia; all communication is through fragmentary expression; great need for inference, '
              'questioning, and guessing by the listener. Range of information that can be exchanged is limited; '
              'listener carries burden of communication. Examiner cannot identify materials provided from patient '
              'response.')),
        (3, _('Mute, global aphasia; no usable speech or auditory comprehension.')),
    )
    best_language = models.IntegerField(_('9. Best Language'), choices=NIH_BEST_LANGUAGE)

    NIH_DYSARTHRIA = (
        (0, _('Normal.')),
        (1, _('Mild-to-moderate dysarthria; patient slurs at least some words and, at worst, can be understood with '
              'some difficulty.')),
        (2, _('Severe dysarthria; patient\'s speech is so slurred as to be unintelligible in the absence of or out of '
              'proportion to any dysphasia, or is mute/anarthric.')),
    )
    dysarthria = models.IntegerField(_('10. Dysarthria'), choices=NIH_DYSARTHRIA)

    NIH_EXTINCTION = (
        (0, _('No abnormality.')),
        (1, _('Visual, tactile, auditory, spatial, or personal inattention or extinction to bilateral simultaneous '
              'stimulation in one of the sensory modalities.')),
        (2, _('Profound hemi-inattention or extinction to more than one modality; does not recognize own hand or '
              'orients to only one side of space. ')),
    )
    extinction = models.IntegerField(_('11. Extinction and Inattention (formerly Neglect)'), choices=NIH_EXTINCTION)

    class Meta:
        verbose_name = _('NIH Stroke Scale')
        verbose_name_plural = _('NIH Stroke Scales')
