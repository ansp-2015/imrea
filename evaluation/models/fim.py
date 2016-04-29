# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation 

FIM_CHOICES_CATEGORY = (
    (7, '7'), #'_(u'Complete independence')),
    (6, '6'), #_(u'Modified independence')),
    (5, '5'), #_(u'Supervision')),
    (4, '4'), #_(u'Minimal assistance')),
    (3, '3'), # _(u'Moderate assistance')),
    (2, '2'), #_(u'Maximal assistance')),
    (1, '1'), #_(u'Total assistance'))
)

class FIM(BaseEvaluation):
    """
    FUNCTIONAL INDEPENDENCE MEASURE - FIM
    ou
    MEDIDA DE INDEPENDÊNCIA FUNCIONAL - MIF                                            
    """
    self_care_eating = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    self_care_grooming = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    self_care_bathing = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    self_care_dressing_upper_body = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    self_care_dressing_lower_body = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    self_care_toileting = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    sphincter_bladder_mgt = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    sphincter_bowel_mgt = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    transfer_wheelchair = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    transfer_toilet = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    transfer_shower = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    locomotion_wheelchair = models.IntegerField(choices=FIM_CHOICES_CATEGORY)
    locomotion_stairs = models.IntegerField(choices=FIM_CHOICES_CATEGORY)

