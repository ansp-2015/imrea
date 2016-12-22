# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from ..util import choice_numbers
from . import BaseEvaluation

class MMSE(BaseEvaluation):
    """
    MINI MENTAL STATE EXAMINATION - MMSE
    ou
    MINI-EXAME DO ESTADO MENTAL - MEEM
    """

    MMSE_ORIENTATION_CHOICES = choice_numbers(1) + BaseEvaluation.UN
    MMSE_REGISTRATION_CHOICES = choice_numbers(3) + BaseEvaluation.UN
    MMSE_ATTENTION_CHOICES = choice_numbers(5) + BaseEvaluation.UN
    MMSE_RECALL_CHOICES = choice_numbers(3) + BaseEvaluation.UN
    MMSE_LANGUAGE_PEN_CHOICES = choice_numbers(2) + BaseEvaluation.UN
    MMSE_LANGUAGE_REPEAT_CHOICES = choice_numbers(1) + BaseEvaluation.UN
    MMSE_LANGUAGE_COMMAND_CHOICES = choice_numbers(3) + BaseEvaluation.UN
    MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES = choice_numbers(1) + BaseEvaluation.UN

    # ORIENTAÇÃO
    orientation_day_week = models.IntegerField(pgettext('MMSE', u'Day of the week'), choices=choice_numbers(1))
    orientation_day_month = models.IntegerField(pgettext('MMSE', u'Day of the month'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_month = models.IntegerField(pgettext('MMSE', u'Month'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_year = models.IntegerField(pgettext('MMSE', u'Year'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_time = models.IntegerField(pgettext('MMSE', u'Approximate time'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_place = models.IntegerField(pgettext('MMSE', u'Specific place (room or sector)'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_institution = models.IntegerField(pgettext('MMSE', u'Institution (home, hospital, clinic)'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_district = models.IntegerField(pgettext('MMSE', u'District or nearby street'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_city = models.IntegerField(pgettext('MMSE', u'City'), choices=MMSE_ORIENTATION_CHOICES)
    orientation_state = models.IntegerField(pgettext('MMSE', u'State'), choices=MMSE_ORIENTATION_CHOICES)
    # MEMÓRIA IMEDIATA
    registration_words = models.IntegerField(pgettext('MMSE', u'Registration'), choices=MMSE_REGISTRATION_CHOICES, help_text=pgettext('MMSE', 'Name 3 objects: 1 second to say each. Then ask the patient all 3 after you have said them. Give 1 point for each correct answer.Then repeat them until he/she learns all 3. Count trials and record'))
    # ATENÇÃO E CÁLCULO
    attention_calc = models.IntegerField(pgettext('MMSE', 'Attention and calculation'), choices=MMSE_ATTENTION_CHOICES, help_text=pgettext('MMSE', u'Count backward from 100 by sevens. 1 point for each correct answer. Stop after 5 answers. Alternatively spell "world" backward.'))
    # EVOCAÇÃO
    recall_words = models.IntegerField(pgettext('MMSE', u'Recall'), choices=MMSE_RECALL_CHOICES, help_text=pgettext('MMSE', u'Ask for the 3 objects repeated above. Give 1 point for each correct answer.'))
    # LINGUAGEM
    language_watch_pen = models.IntegerField(pgettext('MMSE', u'Name a pencil and watch.'), choices=MMSE_LANGUAGE_PEN_CHOICES)
    language_repeat = models.IntegerField(pgettext('MMSE', u'Repeat the following "No ifs, ands, or buts"'), choices=MMSE_LANGUAGE_REPEAT_CHOICES)
    language_command = models.IntegerField(pgettext('MMSE', u'Follow a 3-stage command. "Take a paper in your hand, fold it in half, and put it on the floor."'), choices=MMSE_LANGUAGE_COMMAND_CHOICES)
    language_read = models.IntegerField(pgettext('MMSE', u'Read and obey the following: CLOSE YOUR EYES'), choices=MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES)
    language_write = models.IntegerField(pgettext('MMSE', u'Write a sentence'), choices=MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES)
    language_copy = models.IntegerField(pgettext('MMSE', u'Copy the design shown'), choices=MMSE_LANGUAGE_READ_WRITE_COPY_CHOICES)

    class Meta:
        verbose_name = _('MMSE')
        verbose_name_plural = _('MMSE')
