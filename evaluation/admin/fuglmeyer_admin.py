# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from django.contrib.admin.utils import (unquote,)
from django.utils.safestring import mark_safe
from ..models.fuglmeyer import FuglMeyer
from ..forms import FuglMeyerForm
from .base_admin import BaseAdmin
import logging

logger = logging.getLogger(__name__)


class FuglMeyerAdmin(BaseAdmin):
    form = FuglMeyerForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'Reflex activity'), {
            'fields': ('ue_reflex_activity_flex', 'ue_reflex_activity_ext',
                       ),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_01_ue_reflex_activity'
            }
        }),
        (_(u'Volitional movement within synergies'), {
            'fields': (  # flexor
                        'ue_vol_mov_syn_flex_shoulder_retrac', 'ue_vol_mov_syn_flex_shoulder_elev',
                        'ue_vol_mov_syn_flex_shoulder_abd', 'ue_vol_mov_syn_flex_shoulder_rot', 'ue_vol_mov_syn_flex_elbow_flex',
                        'ue_vol_mov_syn_flex_forearm_sup', 'ue_vol_mov_syn_flex_obs',
                        # extensor
                        'ue_vol_mov_syn_ext_shoulder', 'ue_vol_mov_syn_ext_elbow',
                        'ue_vol_mov_syn_ext_forearm', 'ue_vol_mov_syn_ext_obs',
                       ),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_02_ue_vol_mov_syn',
            }
        }),
        (_(u'Volitional movement mixing synergies, without compensation'), {
            'fields': ('vol_mov_mix_hand_spine', 'vol_mov_mix_shoulder_flex', 'vol_mov_mix_pron_sup'
                      ),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_03_ue_vol_mov_mix',
            }
        }),
        (_(u'Volitional movement with little or no synergy'), {
            'fields': ('ue_vol_mov_no_syn_shoulder_abd', 'ue_vol_mov_no_syn_shoulder_flex', 'ue_vol_mov_no_syn_pron_sup'
                       ),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_04_ue_vol_mov_no_syn',
            }
        }),
        (_(u'Normal reflex activity'), {
            'fields': ('ue_normal_reflex_activity', 'ue_normal_reflex_obs'
                       ),
            'description': {
                'fieldset': '/fuglmeyer/fieldset_05_ue_normal_reflex',
            }
        }),




        (_(u''), {
            'fields': ('obs',),
            'description': {
                'fieldset': '_1col'
            }
        }),
    )

    def _add_context_variables(self, extra_context=None):
        extra_context = extra_context or {}
        sorted_choices = sorted(FuglMeyer.FUGLM_UE_REFLEX_ACTIVITY, key=lambda x: x[0], reverse=False)
        extra_context['FUGLM_UE_REFLEX_ACTIVITY'] = sorted_choices

        extra_context['UE_VOL_MOV_SYN_FLEX_TEXT'] = self.UE_VOL_MOV_SYN_FLEX_TEXT
        extra_context['UE_VOL_MOV_SYN_EXT_TEXT'] = self.UE_VOL_MOV_SYN_EXT_TEXT

        sorted_choices = sorted(FuglMeyer.FUGLM_UE_VOL_MOV_SYN_ACTIVITY, key=lambda x: x[0], reverse=False)
        extra_context['FUGLM_UE_VOL_MOV_SYN_ACTIVITY'] = sorted_choices

        extra_context['FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY'] = FuglMeyer.FUGLM_UE_VOL_MOV_MIX_HAND_SPINE_ACTIVITY
        extra_context['FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY'] = FuglMeyer.FUGLM_UE_VOL_MOV_MIX_SHOULDER_FLEX_ACTIVITY
        extra_context['FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY'] = FuglMeyer.FUGLM_UE_VOL_MOV_MIX_PRON_SUP_ACTIVITY

        extra_context['FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY'] = FuglMeyer.FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_ABD_ACTIVITY
        extra_context['FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY'] = FuglMeyer.FUGLM_UE_VOL_MOV_NO_SYN_SHOULDER_FLEX_ACTIVITY
        extra_context['FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY'] = FuglMeyer.FUGLM_UE_VOL_MOV_NO_SYN_PRON_SUP_ACTIVITY


        return extra_context

    def add_view(self, request, form_url='', extra_context=None):
        """
        Override da view de adição para adicionar algumas variáveis extras de contexto
        """
        extra_context = self._add_context_variables(extra_context)

        return super(FuglMeyerAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Override da view de modificação para adicionar algumas variáveis extras de contexto
        """
        extra_context = self._add_context_variables(extra_context)

        # Campo read-only com a data de nascimento do paciente
        obj = self.get_object(request, unquote(object_id))
        extra_context['patient__birthdate'] = obj.patient.birthdate

        return super(FuglMeyerAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)


    UE_VOL_MOV_SYN_FLEX_TEXT = '%s' % pgettext('UE_VOL_MOV_SYN_FLEX_TEXT', u"Hand from contralateral knee to ipsilateral ear. From extensor synergy (shoulder adduction/ internal rotation, elbow extension, forearm pronation) to flexor synergy (shoulder abduction/ external rotation, elbow flexion, forearm supination).")
    UE_VOL_MOV_SYN_EXT_TEXT = '%s' % pgettext('UE_VOL_MOV_SYN_EXT_TEXT',u"Hand from ipsilateral ear to the contralateral knee")



admin.site.register(FuglMeyer, FuglMeyerAdmin)

