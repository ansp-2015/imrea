# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from . import BaseEvaluation


class MRC(BaseEvaluation):
    """
    Medical Research Council Scale
    """

    # MRC_SCALE = (
    #     (5, _('Muscle contracts normally against full resistance.')),
    #     (4, _('Muscle strength is reduced but muscle contraction can still move joint against resistance.')),
    #     (3, _('Muscle strength is further reduced such that the joint can be moved only against gravity with'
    #           ' the examiner\'s resistance completely removed. As an example, the elbow can be moved from full'
    #           ' extension to full flexion starting with the arm hanging down at the side.')),
    #     (2, _('Muscle can move only if the resistance of gravity is removed. As an example, the elbow can be fully'
    #           ' flexed only if the arm is maintained in a horizontal plane.')),
    #     (1, _('Only a trace or flicker of movement is seen or felt in the muscle or fasciculations are observed in'
    #           ' the muscle.')),
    #     (0, _('No movement is observed.'))
    # )

    MRC_SCALE = (
        (5, _('Grade 5')),
        (4, _('Grade 4')),
        (3, _('Grade 3')),
        (2, _('Grade 2')),
        (1, _('Grade 1')),
        (0, _('Grade 0')),
    )
    shoulder_abduction_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    shoulder_abduction_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    shoulder_abduction_obs = models.TextField(_('Observation'), null=True, blank=True)
    shoulder_flexion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    shoulder_flexion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    shoulder_flexion_obs = models.TextField(_('Observation'), null=True, blank=True)
    shoulder_lateral_rotation_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    shoulder_lateral_rotation_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    shoulder_lateral_rotation_obs = models.TextField(_('Observation'), null=True, blank=True)
    elbow_flexion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    elbow_flexion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    elbow_flexion_obs = models.TextField(_('Observation'), null=True, blank=True)
    elbow_extension_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    elbow_extension_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    elbow_extension_obs = models.TextField(_('Observation'), null=True, blank=True)
    forearm_supination_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    forearm_supination_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    forearm_supination_obs = models.TextField(_('Observation'), null=True, blank=True)
    forearm_pronation_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    forearm_pronation_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    forearm_pronation_obs = models.TextField(_('Observation'), null=True, blank=True)
    wrist_flexion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    wrist_flexion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    wrist_flexion_obs = models.TextField(_('Observation'), null=True, blank=True)
    wrist_extension_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    wrist_extension_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    wrist_extension_obs = models.TextField(_('Observation'), null=True, blank=True)
    fingers_mp_flexion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    fingers_mp_flexion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    fingers_mp_flexion_obs = models.TextField(_('Observation'), null=True, blank=True)
    fingers_mp_extensor_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    fingers_mp_extensor_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    fingers_mp_extensor_obs = models.TextField(_('Observation'), null=True, blank=True)
    hip_flexion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    hip_flexion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    hip_flexion_obs = models.TextField(_('Observation'), null=True, blank=True)
    hip_extension_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    hip_extension_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    hip_extension_obs = models.TextField(_('Observation'), null=True, blank=True)
    hip_abduction_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    hip_abduction_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    hip_abduction_obs = models.TextField(_('Observation'), null=True, blank=True)
    hip_adduction_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    hip_adduction_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    hip_adduction_obs = models.TextField(_('Observation'), null=True, blank=True)
    hip_medial_rotation_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    hip_medial_rotation_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    hip_medial_rotation_obs = models.TextField(_('Observation'), null=True, blank=True)
    hip_lateral_rotation_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    hip_lateral_rotation_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    hip_lateral_rotation_obs = models.TextField(_('Observation'), null=True, blank=True)
    knee_extension_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    knee_extension_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    knee_extension_obs = models.TextField(_('Observation'), null=True, blank=True)
    knee_flexion_biceps_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    knee_flexion_biceps_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    knee_flexion_biceps_obs = models.TextField(_('Observation'), null=True, blank=True)
    knee_flexion_semitendinosus_g5_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    knee_flexion_semitendinosus_g5_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    knee_flexion_semitendinosus_g5_obs = models.TextField(_('Observation'), null=True, blank=True)
    knee_flexion_semitendinosus_g2_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    knee_flexion_semitendinosus_g2_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    knee_flexion_semitendinosus_g2_obs = models.TextField(_('Observation'), null=True, blank=True)
    ankle_plantar_flexion_gastrocnemius_g5_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    ankle_plantar_flexion_gastrocnemius_g5_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    ankle_plantar_flexion_gastrocnemius_g5_obs = models.TextField(_('Observation'), null=True, blank=True)
    ankle_plantar_flexion_sole_g5_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    ankle_plantar_flexion_sole_g5_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    ankle_plantar_flexion_sole_g5_obs = models.TextField(_('Observation'), null=True, blank=True)
    ankle_plantar_flexion_sole_g2_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    ankle_plantar_flexion_sole_g2_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    ankle_plantar_flexion_sole_g2_obs = models.TextField(_('Observation'), null=True, blank=True)
    ankle_dorsiflexion_left = models.IntegerField(_('Left dorsiflexion'), choices=MRC_SCALE)
    ankle_dorsiflexion_right = models.IntegerField(_('Right dorsiflexion'), choices=MRC_SCALE)
    ankle_subtalar_inversion_left = models.IntegerField(_('Left inversion'), choices=MRC_SCALE)
    ankle_subtalar_inversion_right = models.IntegerField(_('Right inversion'), choices=MRC_SCALE)
    ankle_dorsiflexion_subtalar_inversion_obs = models.TextField(_('Observation'), null=True, blank=True)
    subtalar_inversion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    subtalar_inversion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    subtalar_inversion_obs = models.TextField(_('Observation'), null=True, blank=True)
    subtalar_eversion_left = models.IntegerField(_('Left'), choices=MRC_SCALE)
    subtalar_eversion_right = models.IntegerField(_('Right'), choices=MRC_SCALE)
    subtalar_eversion_obs = models.TextField(_('Observation'), null=True, blank=True)

    class Meta:
        verbose_name = _('MRC')
        verbose_name_plural = _('MRCs')