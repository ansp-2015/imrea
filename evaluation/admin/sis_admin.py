# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from django.contrib.admin.utils import (unquote,)
from evaluation.models.sis import SIS
from ..forms import SISForm
from .base_admin import BaseAdmin


class SISAdmin(BaseAdmin):

    form = SISForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (_(u'These questions are about the physical problems which may have occurred as a result of your stroke.'), {
            'fields': ('strength_arm', 'strength_hand', 'strength_leg', 'strength_foot'),
            'description': {
                'columns': ((0, _(u'1. In the past week, how would you rate the strength of your....')),) +
                           SIS.CHOICES_STRENGTH,
                'fieldset': '_radio_grid',
            }
        }),
        (_(u'These questions are about your memory and thinking'), {
            'fields': (
                'dificulty_remember_ppl_told', 'dificulty_remember_happ_day_bef', 'dificulty_remember_do_things',
                'dificulty_remember_day_week', 'dificulty_concentrate', 'dificulty_think_quickly', 'dificulty_solve_problems',
            ),
            'description': {
                'columns': ((0, _(u'2. In the past week, how difficultwas it for you to...')),) +
                           SIS.CHOICES_DIFICULTY,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'These questions are about how you feel, about changes in your mood and about your ability to control your emotions since your stroke.'), {
            'fields': (
                'mood_feel_sad', 'mood_nobody_close', 'mood_burden', 'mood_nothing_to_look_fwd',
                'mood_blame_mistakes', 'mood_enjoy_things', 'mood_feel_nervous', 'mood_feel_worth_living',
                'mood_smile_laugh',
            ),
            'description': {
                'columns': ((0, _(u'3. In the past week, how often did you...')),) +
                           SIS.CHOICES_DIFICULTY,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'The following questions are about your ability to communicate with other people, as well as your ability to understand what you read and what you hear in a conversation.'), {
            'fields': (
                'communication_say_name', 'communication_understand', 'communication_reply',
                'communication_name_objs', 'communication_group_conversation', 'communication_tel_conversation',
                'communication_tel_call',
            ),
            'description': {
                'columns': ((0, _(u'4. In the past week, how difficult was it to... ')),) +
                           SIS.CHOICES_COMMUNICATION,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'The following questions ask about activities you might do during a typical day.'), {
            'fields': (
                'activities_cut_food', 'activities_dress', 'activities_bathe',
                'activities_clip_toenails', 'activities_toilet', 'activities_control_bladder',
                'activities_control_bowels', 'activities_light_household', 'activities_shopping',
                'activities_heavy_household',
            ),
            'description': {
                'columns': ((0, _(u'5. In the past 2 weeks, how difficultwas it to... ')),) +
                           SIS.CHOICES_ACTIVITIES,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'The following questions are about your ability to be mobile, at home and in the community.'), {
            'fields': (
                'mobile_sitting', 'mobile_standing', 'mobile_walk_balance',
                'mobile_bed_chair', 'mobile_walk_one_block', 'mobile_walk_fast',
                'mobile_climb_one_flight', 'mobile_climb_several_flights', 'mobile_in_out_car',
            ),
            'description': {
                'columns': ((0, _(u'6. In the past 2 weeks, how difficultwas it to...')),) +
                           SIS.CHOICES_MOBILE,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'The following questions are about your ability to use your hand that was MOST AFFECTED by your stroke.'), {
            'fields': (
                'hand_carry_heavy_objs', 'hand_turn_doorknob', 'hand_open_jar',
                'hand_tie_shoe_lace', 'hand_pick_dime',
            ),
            'description': {
                'columns': ((0, _(u'7. In the past 2 weeks, how difficult was it to use your hand that was most affected by your stroke to...')),) +
                           SIS.CHOICES_HAND,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'The following questions are about how stroke has affected your ability to participate in the activities that you usually do, things that are meaningful to you and help you to find purpose in life.'), {
            'fields': (
                'time_work', 'time_social', 'time_quiet_recreation',
                'time_active_recreation', 'time_family', 'time_spiritual',
                'time_control_life', 'time_help_others',
            ),
            'description': {
                'columns': ((0, _(u'8. During the past 4 weeks, how much of the time have you been limited in...')),) +
                           SIS.CHOICES_TIME,
                'fieldset': '_radio_grid'
            }
        }),
        (_(u'On a scale of 0 to 100, with 100 representing full recovery and 0 representing no recovery, how much have you recovered from your stroke?'), {
            'fields': ('scale_recovery',),
            'description': {
                'columns': ((0, _(u'9. Stroke Recovery ')),) +
                           SIS.CHOICES_TIME,
                'fieldset': '_1col'
            }
        }),

    )

    list_display = ('patient', 'get_patient_birthdate', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

    # Exibição do birthdate na lista de registros
    def get_patient_birthdate(self, obj):
        return obj.patient.birthdate
    get_patient_birthdate.short_description = _('Birthdate')
    get_patient_birthdate.admin_order_field = 'patient__birthdate'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        Override da view de modificação para adicionar algumas variáveis extras de contexto
        """
        extra_context = extra_context or {}

        # Campo read-only com a data de nascimento do paciente
        obj = self.get_object(request, unquote(object_id))
        extra_context['patient__birthdate'] = obj.patient.birthdate

        return super(SISAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        """
        :return: Retorna somente o patient e period como read-only na modificação
        """
        if obj:
            return ['patient', 'period']
        else:
            return []

admin.site.register(SIS, SISAdmin)
# Registrando no reversion-compare
patch_admin(SIS)

