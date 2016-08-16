# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from . import BaseEvaluation


class NIHSS(BaseEvaluation):
    """
    National Institutes of Health Stroke Scale
    """

    ### Descriptions
    NIH_LOC_DESCRIPTION = _(u'The investigator must choose a response if a full evaluation is prevented by such '
                            u'obstacles as an endotracheal tube, language barrier, orotracheal trauma/bandages. A '
                            u'3 is scored only if the patient makes no movement (other than reflexive posturing) in '
                            u'response to noxious stimulation.')

    NIH_LOC_QUESTIONS_DESCRIPTION = _(u'The patient is asked the month and his/her age. The answer must be correct - '
                                      u'there is no partial credit for being close. Aphasic and stuporous patients '
                                      u'who do not comprehend the questions will score 2. Patients unable to speak '
                                      u'because of endotracheal intubation, orotracheal trauma, severe dysarthria '
                                      u'from any cause, language barrier, or any other problem not secondary to '
                                      u'aphasia are given a 1. It is important that only the initial answer be graded '
                                      u'and that the examiner not "help" the patient with verbal or non-verbal cues.')

    NIH_LOC_COMMANDS_DESCRIPTION = _(u'The patient is asked to open and close the eyes and then to grip and release '
                                     u'the non-paretic hand. Substitute another one step command if the hands cannot '
                                     u'be used. Credit is given if an unequivocal attempt is made but not completed '
                                     u'due to weakness. If the patient does not respond to command, the task should '
                                     u'be demonstrated to him or her (pantomime), and the result scored (i.e., '
                                     u'follows none, one or two commands). Patients with trauma, amputation, or other '
                                     u'physical impediments should be given suitable one-step commands. Only the '
                                     u'first attempt is scored.')

    NIH_BEST_GAZE_DESCRIPTION = _(u'Only horizontal eye movements will be tested. Voluntary or reflexive '
                                  u'(oculocephalic) eye movements will be scored, but caloric testing is not done. If '
                                  u'the patient has a conjugate deviation of the eyes that can be overcome by '
                                  u'voluntary or reflexive activity, the score will be 1. If a patient has an isolated '
                                  u'peripheral nerve paresis (CN III, IV or VI), score a 1. Gaze is testable in all '
                                  u'aphasic patients. Patients with ocular trauma, bandages, pre-existing blindness, '
                                  u'or other disorder of visual acuity or fields should be tested with reflexive '
                                  u'movements, and a choice made by the investigator. Establishing eye contact and '
                                  u'then moving about the patient from side to side will occasionally clarify the '
                                  u'presence of a partial gaze palsy.')

    NIH_VISUAL_DESCRIPTION = _(u'Visual fields (upper and lower quadrants) are tested by confrontation, using finger '
                               u'counting or visual threat, as appropriate. Patients may be encouraged, but if they '
                               u'look at the side of the moving fingers appropriately, this can be scored as normal. '
                               u'If there is unilateral blindness or enucleation, visual fields in the remaining eye '
                               u'are scored. Score 1 only if a clear-cut asymmetry, including quadrantanopia, is '
                               u'found. If patient is blind from any cause, score 3. Double simultaneous stimulation '
                               u'is performed at this point. If there is extinction, patient receives a 1, and the '
                               u'results are used to respond to item 11.')

    NIH_FACIAL_PALSY_DESCRIPTION = _(u'Ask – or use pantomime to encourage – the patient to show teeth or raise eyebrows and close '
                                     u'eyes. Score symmetry of grimace in response to noxious stimuli in the poorly responsive or '
                                     u'non-comprehending patient. If facial trauma/bandages, orotracheal tube, tape or other '
                                     u'physical barriers obscure the face, these should be removed to the extent possible.')

    NIH_MOTOR_ARM_DESCRIPTION = _(u'The limb is placed in the appropriate position: extend the arms (palms down) 90 '
                                  u'degrees (if sitting) or 45 degrees (if supine). Drift is scored if the arm falls '
                                  u'before 10 seconds. The aphasic patient is encouraged using urgency in the voice '
                                  u'and pantomime, but not noxious stimulation. Each limb is tested in turn, beginning '
                                  u'with the non-paretic arm. Only in the case of amputation or joint fusion at the '
                                  u'shoulder, the examiner should record the score as untestable (UN), and clearly '
                                  u'write the explanation for this choice.')

    NIH_MOTOR_LEG_DESCRIPTION = _(u'The limb is placed in the appropriate position: hold the leg at 30 degrees (always '
                                  u'tested supine). Drift is scored if the leg falls before 5 seconds. The aphasic '
                                  u'patient is encouraged using urgency in the voice and pantomime, but not noxious '
                                  u'stimulation. Each limb is tested in turn, beginning with the non-paretic leg. Only '
                                  u'in the case of amputation or joint fusion at the hip, the examiner should record '
                                  u'the score as untestable (UN), and clearly write the explanation for this choice.')

    NIH_LIMB_ATAXIA_DESCRIPTION = _(u'This item is aimed at finding evidence of a unilateral cerebellar lesion. Test '
                                    u'with eyes open. In case of visual defect, ensure testing is done in intact '
                                    u'visual field. The finger-nose-finger and heel-shin tests are performed on both '
                                    u'sides, and ataxia is scored only if present out of proportion to weakness. '
                                    u'Ataxia is absent in the patient who cannot understand or is paralyzed. Only in '
                                    u'the case of amputation or joint fusion, the examiner should record the score as '
                                    u'untestable (UN), and clearly write the explanation for this choice. In case of '
                                    u'blindness, test by having the patient touch nose from extended arm position. ')

    NIH_SENSORY_DESCRIPTION = _(u'Sensation or grimace to pinprick when tested, or withdrawal from noxious stimulus in '
                                u'the obtunded or aphasic patient. Only sensory loss attributed to stroke is scored as '
                                u'abnormal and the examiner should test as many body areas (arms [not hands], legs, '
                                u'trunk, face) as needed to accurately check for hemisensory loss. A score of 2, '
                                u'"severe or total sensory loss," should only be given when a severe or total loss of '
                                u'sensation can be clearly demonstrated. Stuporous and aphasic patients will, '
                                u'therefore, probably score 1 or 0. The patient with brainstem stroke who has '
                                u'bilateral loss of sensation is scored 2. If the patient does not respond and is '
                                u'quadriplegic, score 2. Patients in a coma (item 1a=3) are automatically given a 2 on '
                                u'this item.')

    NIH_BEST_LANGUAGE_DESCRIPTION = _(u'A great deal of information about comprehension will be obtained during the '
                                      u'preceding sections of the examination. For this scale item, the patient is '
                                      u'asked to describe what is happening in the attached picture, to name the items '
                                      u'on the attached naming sheet and to read from the attached list of sentences. '
                                      u'Comprehension is judged from responses here, as well as to all of the commands '
                                      u'in the preceding general neurological exam. If visual loss interferes with the '
                                      u'tests, ask the patient to identify objects placed in the hand, repeat, and '
                                      u'produce speech. The intubated patient should be asked to write. The patient in '
                                      u'a coma (item 1a=3) will automatically score 3 on this item. The examiner must '
                                      u'choose a score for the patient with stupor or limited cooperation, but a score '
                                      u'of 3 should be used only if the patient is mute and follows no one-step '
                                      u'commands. ')

    NIH_DYSARTHRIA_DESCRIPTION = _(u'If patient is thought to be normal, an adequatesample of speech must be obtained '
                                   u'by asking patient to read or repeat words from the attached list. If the patient '
                                   u'has severe aphasia, the clarity of articulation of spontaneous speech can be '
                                   u'rated. Only if the patient is intubated or has other physical barriers to '
                                   u'producing speech, the examiner should record the score as untestable (UN), and '
                                   u'clearly write an explanation for this choice. Do not tell the patient why he or '
                                   u'she is being tested.')

    NIH_EXTINCTION_DESCRIPTION = _(u'Sufficient information to identify neglect may be obtained during the prior '
                                   u'testing. If the patient has a severe visual loss preventing visual double '
                                   u'simultaneous stimulation, and the cutaneous stimuli are normal, the score is '
                                   u'normal. If the patient has aphasia but does appear to attend to both sides, the '
                                   u'score is normal. The presence of visual spatial neglect or anosagnosia may also '
                                   u'be taken as evidence of abnormality. Since the abnormality is scored only if '
                                   u'present, the item is never untestable.')

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
    motor_arm_left = models.IntegerField(_('5. Motor arm'), choices=NIH_MOTOR_ARM)
    motor_arm_right = models.IntegerField(choices=NIH_MOTOR_ARM)
    motor_arm_left_un_explanation = models.TextField(null=True, blank=True)
    motor_arm_right_un_explanation = models.TextField(null=True, blank=True)

    NIH_MOTOR_LEG = (
        (0, _('No drift; leg holds 30-degree position for full 5 seconds.')),
        (1, _('Drift; leg falls by the end of the 5-second period but does not hit bed.')),
        (2, _('Some effort against gravity; leg falls to bed by 5 seconds, but has some effort against gravity.')),
        (3, _('No effort against gravity; leg falls to bed immediately.')),
        (4, _('No movement.')),
    )
    motor_leg_left = models.IntegerField(_('6. Motor leg'), choices=NIH_MOTOR_LEG)
    motor_leg_right = models.IntegerField(choices=NIH_MOTOR_LEG)
    motor_leg_left_un_explanation = models.TextField(null=True, blank=True)
    motor_leg_right_un_explanation = models.TextField(null=True, blank=True)

    NIH_LIMB_ATAXIA = (
        (0, _('Absent.')),
        (1, _('Present in one limb.')),
        (2, _('Present in two limbs.')),
    )
    limb_ataxia = models.IntegerField(_('7. Limb Ataxia'), choices=NIH_LIMB_ATAXIA)
    limb_ataxia_un_explanation = models.TextField(null=True, blank=True)

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
    dysarthria_un_explanation = models.TextField(null=True, blank=True)

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
