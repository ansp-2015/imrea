# -*- coding: utf-8 -*-
from django import forms
from ..models.sis import SIS
from ..widgets import ButtonRadioGridSelect

class SISForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SISForm, self).__init__(*args, **kwargs)
        self.fields['strength_arm'].choices = SIS.CHOICES_STRENGTH
        self.fields['strength_hand'].choices = SIS.CHOICES_STRENGTH
        self.fields['strength_leg'].choices = SIS.CHOICES_STRENGTH
        self.fields['strength_foot'].choices = SIS.CHOICES_STRENGTH

        self.fields['dificulty_remember_ppl_told'].choices = SIS.CHOICES_DIFICULTY
        self.fields['dificulty_remember_happ_day_bef'].choices = SIS.CHOICES_DIFICULTY
        self.fields['dificulty_remember_do_things'].choices = SIS.CHOICES_DIFICULTY
        self.fields['dificulty_remember_day_week'].choices = SIS.CHOICES_DIFICULTY
        self.fields['dificulty_concentrate'].choices = SIS.CHOICES_DIFICULTY
        self.fields['dificulty_think_quickly'].choices = SIS.CHOICES_DIFICULTY
        self.fields['dificulty_solve_problems'].choices = SIS.CHOICES_DIFICULTY

        self.fields['mood_feel_sad'].choices = SIS.CHOICES_MOOD
        self.fields['mood_nobody_close'].choices = SIS.CHOICES_MOOD
        self.fields['mood_burden'].choices = SIS.CHOICES_MOOD
        self.fields['mood_nothing_to_look_fwd'].choices = SIS.CHOICES_MOOD
        self.fields['mood_blame_mistakes'].choices = SIS.CHOICES_MOOD
        self.fields['mood_enjoy_things'].choices = SIS.CHOICES_MOOD
        self.fields['mood_feel_nervous'].choices = SIS.CHOICES_MOOD
        self.fields['mood_feel_worth_living'].choices = SIS.CHOICES_MOOD
        self.fields['mood_smile_laugh'].choices = SIS.CHOICES_MOOD

        self.fields['communication_say_name'].choices = SIS.CHOICES_COMMUNICATION
        self.fields['communication_understand'].choices = SIS.CHOICES_COMMUNICATION
        self.fields['communication_reply'].choices = SIS.CHOICES_COMMUNICATION
        self.fields['communication_name_objs'].choices = SIS.CHOICES_COMMUNICATION
        self.fields['communication_group_conversation'].choices = SIS.CHOICES_COMMUNICATION
        self.fields['communication_tel_conversation'].choices = SIS.CHOICES_COMMUNICATION
        self.fields['communication_tel_call'].choices = SIS.CHOICES_COMMUNICATION

        self.fields['activities_cut_food'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_dress'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_bathe'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_clip_toenails'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_toilet'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_control_bladder'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_control_bowels'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_light_household'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_shopping'].choices = SIS.CHOICES_ACTIVITIES
        self.fields['activities_heavy_household'].choices = SIS.CHOICES_ACTIVITIES

        self.fields['mobile_sitting'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_standing'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_walk_balance'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_bed_chair'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_walk_one_block'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_walk_fast'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_climb_one_flight'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_climb_several_flights'].choices = SIS.CHOICES_MOBILE
        self.fields['mobile_in_out_car'].choices = SIS.CHOICES_MOBILE

        self.fields['hand_carry_heavy_objs'].choices = SIS.CHOICES_HAND
        self.fields['hand_turn_doorknob'].choices = SIS.CHOICES_HAND
        self.fields['hand_open_jar'].choices = SIS.CHOICES_HAND
        self.fields['hand_tie_shoe_lace'].choices = SIS.CHOICES_HAND
        self.fields['hand_pick_dime'].choices = SIS.CHOICES_HAND

        self.fields['time_work'].choices = SIS.CHOICES_TIME
        self.fields['time_social'].choices = SIS.CHOICES_TIME
        self.fields['time_quiet_recreation'].choices = SIS.CHOICES_TIME
        self.fields['time_active_recreation'].choices = SIS.CHOICES_TIME
        self.fields['time_family'].choices = SIS.CHOICES_TIME
        self.fields['time_spiritual'].choices = SIS.CHOICES_TIME
        self.fields['time_control_life'].choices = SIS.CHOICES_TIME
        self.fields['time_help_others'].choices = SIS.CHOICES_TIME

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = SIS
        fields = ['patient', 'period',
                  'strength_arm', 'strength_hand', 'strength_leg', 'strength_foot',

                  'dificulty_remember_ppl_told', 'dificulty_remember_happ_day_bef', 'dificulty_remember_do_things',
                  'dificulty_remember_day_week', 'dificulty_concentrate', 'dificulty_think_quickly', 'dificulty_solve_problems',

                  'mood_feel_sad', 'mood_nobody_close', 'mood_burden', 'mood_nothing_to_look_fwd',
                  'mood_blame_mistakes', 'mood_enjoy_things', 'mood_feel_nervous', 'mood_feel_worth_living',
                  'mood_smile_laugh',

                  'communication_say_name', 'communication_understand', 'communication_reply',
                  'communication_name_objs', 'communication_group_conversation', 'communication_tel_conversation',
                  'communication_tel_call',

                  'activities_cut_food', 'activities_dress', 'activities_bathe',
                  'activities_clip_toenails', 'activities_toilet', 'activities_control_bladder',
                  'activities_control_bowels', 'activities_light_household', 'activities_shopping',
                  'activities_heavy_household',

                  'mobile_sitting', 'mobile_standing', 'mobile_walk_balance',
                  'mobile_bed_chair', 'mobile_walk_one_block', 'mobile_walk_fast',
                  'mobile_climb_one_flight', 'mobile_climb_several_flights', 'mobile_in_out_car',

                  'hand_carry_heavy_objs', 'hand_turn_doorknob', 'hand_open_jar',
                  'hand_tie_shoe_lace', 'hand_pick_dime',

                  'time_work', 'time_social', 'time_quiet_recreation',
                  'time_active_recreation', 'time_family', 'time_spiritual',
                  'time_control_life', 'time_help_others',

                  'scale_recovery'
                  ]

        widgets = {
            'strength_arm': ButtonRadioGridSelect(),
            'strength_hand': ButtonRadioGridSelect(),
            'strength_leg': ButtonRadioGridSelect(),
            'strength_foot': ButtonRadioGridSelect(),

            'dificulty_remember_ppl_told': ButtonRadioGridSelect(),
            'dificulty_remember_happ_day_bef': ButtonRadioGridSelect(),
            'dificulty_remember_do_things': ButtonRadioGridSelect(),
            'dificulty_remember_day_week': ButtonRadioGridSelect(),
            'dificulty_concentrate': ButtonRadioGridSelect(),
            'dificulty_think_quickly': ButtonRadioGridSelect(),
            'dificulty_solve_problems': ButtonRadioGridSelect(),

            'mood_feel_sad': ButtonRadioGridSelect(),
            'mood_nobody_close': ButtonRadioGridSelect(),
            'mood_burden': ButtonRadioGridSelect(),
            'mood_nothing_to_look_fwd': ButtonRadioGridSelect(),
            'mood_blame_mistakes': ButtonRadioGridSelect(),
            'mood_enjoy_things': ButtonRadioGridSelect(),
            'mood_feel_nervous': ButtonRadioGridSelect(),
            'mood_feel_worth_living': ButtonRadioGridSelect(),
            'mood_smile_laugh': ButtonRadioGridSelect(),

            'communication_say_name': ButtonRadioGridSelect(),
            'communication_understand': ButtonRadioGridSelect(),
            'communication_reply': ButtonRadioGridSelect(),
            'communication_name_objs': ButtonRadioGridSelect(),
            'communication_group_conversation': ButtonRadioGridSelect(),
            'communication_tel_conversation': ButtonRadioGridSelect(),
            'communication_tel_call': ButtonRadioGridSelect(),

            'activities_cut_food': ButtonRadioGridSelect(),
            'activities_dress': ButtonRadioGridSelect(),
            'activities_bathe': ButtonRadioGridSelect(),
            'activities_clip_toenails': ButtonRadioGridSelect(),
            'activities_toilet': ButtonRadioGridSelect(),
            'activities_control_bladder': ButtonRadioGridSelect(),
            'activities_control_bowels': ButtonRadioGridSelect(),
            'activities_light_household': ButtonRadioGridSelect(),
            'activities_shopping': ButtonRadioGridSelect(),
            'activities_heavy_household': ButtonRadioGridSelect(),

            'mobile_sitting': ButtonRadioGridSelect(),
            'mobile_standing': ButtonRadioGridSelect(),
            'mobile_walk_balance': ButtonRadioGridSelect(),
            'mobile_bed_chair': ButtonRadioGridSelect(),
            'mobile_walk_one_block': ButtonRadioGridSelect(),
            'mobile_walk_fast': ButtonRadioGridSelect(),
            'mobile_climb_one_flight': ButtonRadioGridSelect(),
            'mobile_climb_several_flights': ButtonRadioGridSelect(),
            'mobile_in_out_car': ButtonRadioGridSelect(),

            'hand_carry_heavy_objs': ButtonRadioGridSelect(),
            'hand_turn_doorknob': ButtonRadioGridSelect(),
            'hand_open_jar': ButtonRadioGridSelect(),
            'hand_tie_shoe_lace': ButtonRadioGridSelect(),
            'hand_pick_dime': ButtonRadioGridSelect(),

            'time_work': ButtonRadioGridSelect(),
            'time_social': ButtonRadioGridSelect(),
            'time_quiet_recreation': ButtonRadioGridSelect(),
            'time_active_recreation': ButtonRadioGridSelect(),
            'time_family': ButtonRadioGridSelect(),
            'time_spiritual': ButtonRadioGridSelect(),
            'time_control_life': ButtonRadioGridSelect(),
            'time_help_others': ButtonRadioGridSelect(),
        }

