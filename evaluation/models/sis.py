# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from evaluation.models.patient import Patient
from . import BaseEvaluation


class SIS(BaseEvaluation):
    # 1
    CHOICES_STRENGTH = (
        (5, pgettext("CHOICES_STRENGTH", u'A lot of strength')),
        (4, pgettext("CHOICES_STRENGTH", u'Quite a bit of strength')),
        (3, pgettext("CHOICES_STRENGTH", u'Some strength')),
        (2, pgettext("CHOICES_STRENGTH", u'A little strength')),
        (1, pgettext("CHOICES_STRENGTH", u'No strength at all'))
    )
    strength_arm = models.IntegerField(_('a. Arm that was most affected'), choices=CHOICES_STRENGTH)
    strength_hand = models.IntegerField(_('b. Grip of your hand that was most affected'), choices=CHOICES_STRENGTH)
    strength_leg = models.IntegerField(_('c. Leg that was most affected'), choices=CHOICES_STRENGTH)
    strength_foot = models.IntegerField(_('d. Foot/ankle that was most affected'), choices=CHOICES_STRENGTH)

    # 2
    CHOICES_DIFICULTY = (
        (5, pgettext("CHOICES_DIFICULTY", u'Not difficult at all')),
        (4, pgettext("CHOICES_DIFICULTY", u'A little difficult')),
        (3, pgettext("CHOICES_DIFICULTY", u'Somewhat difficult')),
        (2, pgettext("CHOICES_DIFICULTY", u'Very difficult')),
        (1, pgettext("CHOICES_DIFICULTY", u'Extremely difficult'))
    )
    dificulty_remember_ppl_told = models.IntegerField(_('a. Remember things that people just told you?'), choices=CHOICES_DIFICULTY)
    dificulty_remember_happ_day_bef = models.IntegerField(_('b. Remember things that happened the day before?'), choices=CHOICES_DIFICULTY)
    dificulty_remember_do_things = models.IntegerField(_('c. Remember to do things (e.g. keep scheduled appointments or take medication)?'), choices=CHOICES_DIFICULTY)
    dificulty_remember_day_week = models.IntegerField(_('d. Remember the day of the week?'), choices=CHOICES_DIFICULTY)
    dificulty_concentrate = models.IntegerField(_('e. Concentrate?'), choices=CHOICES_DIFICULTY)
    dificulty_think_quickly = models.IntegerField(_('f. Think quickly?'), choices=CHOICES_DIFICULTY)
    dificulty_solve_problems = models.IntegerField(_('g. Solve everyday problems?'), choices=CHOICES_DIFICULTY)

    # 3
    CHOICES_MOOD = (
        (5, pgettext("CHOICES_MOOD", u'None of the time')),
        (4, pgettext("CHOICES_MOOD", u'A little of the time')),
        (3, pgettext("CHOICES_MOOD", u'Some of the time')),
        (2, pgettext("CHOICES_MOOD", u'Most of the time')),
        (1, pgettext("CHOICES_MOOD", u'All of the time'))
    )
    mood_feel_sad = models.IntegerField(_('a. Feel sad?'), choices=CHOICES_MOOD)
    mood_nobody_close = models.IntegerField(_('b. Feel that there is nobody you are close to?'), choices=CHOICES_MOOD)
    mood_burden = models.IntegerField(_('c. Feel that you are a burden to others?'), choices=CHOICES_MOOD)
    mood_nothing_to_look_fwd = models.IntegerField(_('d. Feel that you have nothing to look forward to?'), choices=CHOICES_MOOD)
    mood_blame_mistakes = models.IntegerField(_('e. Blame yourself for mistakes that you made?'), choices=CHOICES_MOOD)
    mood_enjoy_things = models.IntegerField(_('f. Enjoy things as much as ever?'), choices=CHOICES_MOOD)
    mood_feel_nervous = models.IntegerField(_('g. Feel quite nervous?'), choices=CHOICES_MOOD)
    mood_feel_worth_living = models.IntegerField(_('h. Feel that life is worth living?'), choices=CHOICES_MOOD)
    mood_smile_laugh = models.IntegerField(_('i. Smile and laugh at least once a day?'), choices=CHOICES_MOOD)

    # 4
    CHOICES_COMMUNICATION = (
        (5, pgettext("CHOICES_COMMUNICATION", u'Not difficult at all')),
        (4, pgettext("CHOICES_COMMUNICATION", u'A little difficult')),
        (3, pgettext("CHOICES_COMMUNICATION", u'Somewhat difficult')),
        (2, pgettext("CHOICES_COMMUNICATION", u'Very difficult')),
        (1, pgettext("CHOICES_COMMUNICATION", u'Extremely difficult'))
    )
    communication_say_name = models.IntegerField(_('a. Say the name of someone who was in front of you?'), choices=CHOICES_COMMUNICATION)
    communication_understand = models.IntegerField(_('b. Understand what was being said to you in a conversation?'), choices=CHOICES_COMMUNICATION)
    communication_reply = models.IntegerField(_('c. Reply to questions?'), choices=CHOICES_COMMUNICATION)
    communication_name_objs = models.IntegerField(_('d. Correctly name objects?'), choices=CHOICES_COMMUNICATION)
    communication_group_conversation = models.IntegerField(_('e. Participate in a conversation with a group of people?'), choices=CHOICES_COMMUNICATION)
    communication_tel_conversation = models.IntegerField(_('f. Have a conversation on the telephone? '), choices=CHOICES_COMMUNICATION)
    communication_tel_call = models.IntegerField(_('g. Call another person on the telephone, including selecting the correct phone number and dialing?'), choices=CHOICES_COMMUNICATION)

    # 5
    CHOICES_ACTIVITIES = (
        (5, pgettext("CHOICES_ACTIVITIES", u'Not difficult at all')),
        (4, pgettext("CHOICES_ACTIVITIES", u'A little difficult')),
        (3, pgettext("CHOICES_ACTIVITIES", u'Somewhat difficult')),
        (2, pgettext("CHOICES_ACTIVITIES", u'Very difficult')),
        (1, pgettext("CHOICES_ACTIVITIES", u'Could not do at all'))
    )
    activities_cut_food = models.IntegerField(_('a. Cut your food with a knife and fork?'), choices=CHOICES_ACTIVITIES)
    activities_dress = models.IntegerField(_('b. Dress the top part of your body?'), choices=CHOICES_ACTIVITIES)
    activities_bathe = models.IntegerField(_('c. Bathe yourself?'), choices=CHOICES_ACTIVITIES)
    activities_clip_toenails = models.IntegerField(_('d. Clip your toenails?'), choices=CHOICES_ACTIVITIES)
    activities_toilet = models.IntegerField(_('e. Get to the toilet on time?'), choices=CHOICES_ACTIVITIES)
    activities_control_bladder = models.IntegerField(_('f. Control your bladder (not have an accident)?'), choices=CHOICES_ACTIVITIES)
    activities_control_bowels = models.IntegerField(_('g. Control your bowels (not have an accident)?'), choices=CHOICES_ACTIVITIES)
    activities_light_household = models.IntegerField(_('h. Do light household tasks/chores(e.g. dust, make a bed, take out garbage, do the dishes)?'), choices=CHOICES_ACTIVITIES)
    activities_shopping = models.IntegerField(_('i. Go shopping?'), choices=CHOICES_ACTIVITIES)
    activities_heavy_household = models.IntegerField(_('j. Do heavy household chores (e.g.vacuum, laundry or yard work)?'), choices=CHOICES_ACTIVITIES)

    # 6
    CHOICES_MOBILE = (
        (5, pgettext("CHOICES_MOBILE", u'Not difficult at all')),
        (4, pgettext("CHOICES_MOBILE", u'A little difficult')),
        (3, pgettext("CHOICES_MOBILE", u'Somewhat difficult')),
        (2, pgettext("CHOICES_MOBILE", u'Very difficult')),
        (1, pgettext("CHOICES_MOBILE", u'Could not do at all'))
    )
    mobile_sitting = models.IntegerField(_('a. Stay sitting without losing your balance?'), choices=CHOICES_MOBILE)
    mobile_standing = models.IntegerField(_('b. Stay standing without losing your balance?'), choices=CHOICES_MOBILE)
    mobile_walk_balance = models.IntegerField(_('c. Walk without losing your balance?'), choices=CHOICES_MOBILE)
    mobile_bed_chair = models.IntegerField(_('d. Move from a bed to a chair?'), choices=CHOICES_MOBILE)
    mobile_walk_one_block = models.IntegerField(_('e. Walk one block?'), choices=CHOICES_MOBILE)
    mobile_walk_fast = models.IntegerField(_('f. Walk fast?'), choices=CHOICES_MOBILE)
    mobile_climb_one_flight = models.IntegerField(_('g. Climb one flight of stairs?'), choices=CHOICES_MOBILE)
    mobile_climb_several_flights = models.IntegerField(_('h. Climb several flights of stairs?'), choices=CHOICES_MOBILE)
    mobile_in_out_car = models.IntegerField(_('i. Get in and out of a car?'), choices=CHOICES_MOBILE)

    # 7
    CHOICES_HAND = (
        (5, pgettext("CHOICES_HAND", u'Not difficult at all')),
        (4, pgettext("CHOICES_HAND", u'A little difficult')),
        (3, pgettext("CHOICES_HAND", u'Somewhat difficult')),
        (2, pgettext("CHOICES_HAND", u'Very difficult')),
        (1, pgettext("CHOICES_HAND", u'Could not do at all'))
    )
    hand_carry_heavy_objs = models.IntegerField(_('a. Carry heavy objects (e.g. bag of groceries)?'), choices=CHOICES_HAND)
    hand_turn_doorknob = models.IntegerField(_('b. Turn a doorknob?'), choices=CHOICES_HAND)
    hand_open_jar = models.IntegerField(_('c. Open a can or jar?'), choices=CHOICES_HAND)
    hand_tie_shoe_lace = models.IntegerField(_('d. Tie a shoe lace?'), choices=CHOICES_HAND)
    hand_pick_dime = models.IntegerField(_('e. Pick up a dime?'), choices=CHOICES_HAND)

    # 8
    CHOICES_TIME = (
        (5, pgettext("CHOICES_TIME", u'None of the time')),
        (4, pgettext("CHOICES_TIME", u'A little of the time')),
        (3, pgettext("CHOICES_TIME", u'Some of the time')),
        (2, pgettext("CHOICES_TIME", u'Most of the time')),
        (1, pgettext("CHOICES_TIME", u'All of the time'))
    )
    time_work = models.IntegerField(_('a. Your work (paid, voluntary or other)'), choices=CHOICES_TIME)
    time_social = models.IntegerField(_('b. Your social activities?'), choices=CHOICES_TIME)
    time_quiet_recreation = models.IntegerField(_('c. Quiet recreation (crafts, reading)?'), choices=CHOICES_TIME)
    time_active_recreation = models.IntegerField(_('d. Active recreation (sports, outings,travel)?'), choices=CHOICES_TIME)
    time_family = models.IntegerField(_('e. Your role as a family member and/or friend?'), choices=CHOICES_TIME)
    time_spiritual = models.IntegerField(_('f. Your participation in spiritual or religious activities?'), choices=CHOICES_TIME)
    time_control_life = models.IntegerField(_('g. Your ability to control your life as you wish?'), choices=CHOICES_TIME)
    time_help_others = models.IntegerField(_('h. Your ability to help others?'), choices=CHOICES_TIME)

    # 9
    scale_recovery = models.IntegerField(_(u'Stroke Recovery scale'))

