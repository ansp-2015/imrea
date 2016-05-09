# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import BaseEvaluation 

class FIM(BaseEvaluation):
    """
    FUNCTIONAL INDEPENDENCE MEASURE - FIM
    ou
    MEDIDA DE INDEPENDÊNCIA FUNCIONAL - MIF                                            
    """

    FIM_CHOICES_CATEGORY = (
        (7, _(u'Complete independence')),
        (6, _(u'Modified independence')),
        (5, _(u'Supervision')),
        (4, _(u'Minimal assistance')),
        (3,  _(u'Moderate assistance')),
        (2, _(u'Maximal assistance')),
        (1, _(u'Total assistance'))
    )
    # Cuidados pessoais
    self_care_eating = models.IntegerField(_('Eating'), choices=FIM_CHOICES_CATEGORY)
    self_care_grooming = models.IntegerField(_('Grooming'), choices=FIM_CHOICES_CATEGORY)
    self_care_bathing = models.IntegerField(_('Bathing/showering'), choices=FIM_CHOICES_CATEGORY)
    self_care_dressing_upper_body = models.IntegerField(_('Dressing upper body'), choices=FIM_CHOICES_CATEGORY)
    self_care_dressing_lower_body = models.IntegerField(_('Dressing lower body'), choices=FIM_CHOICES_CATEGORY)
    self_care_toileting = models.IntegerField(_('Toileting'), choices=FIM_CHOICES_CATEGORY)
    # Controle esfincteriano
    sphincter_bladder_mgt = models.IntegerField(_('Bladder management'), choices=FIM_CHOICES_CATEGORY)
    sphincter_bowel_mgt = models.IntegerField(_('Bowel management'), choices=FIM_CHOICES_CATEGORY)
    # Mobilidade / Transferências
    transfer_wheelchair = models.IntegerField(_('Transfers bed/chair/wheelchair'), choices=FIM_CHOICES_CATEGORY)
    transfer_toilet = models.IntegerField(_('Transfers toilet'), choices=FIM_CHOICES_CATEGORY)
    transfer_shower = models.IntegerField(_('Transfers bathtub/shower'), choices=FIM_CHOICES_CATEGORY)
    # Locomoção
    locomotion_wheelchair = models.IntegerField(_('Locomotion walking/wheelchair'), choices=FIM_CHOICES_CATEGORY)
    locomotion_stairs = models.IntegerField(_('Locomotion stairs'), choices=FIM_CHOICES_CATEGORY)

    class Meta:
        verbose_name = _('FIM')
        verbose_name_plural = _('FIMs')