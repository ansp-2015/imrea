# -*- coding: utf-8 -*-
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from . import BaseEvaluation
from ..util import choice_numbers


class MoCA(BaseEvaluation):
    """
    MoCA - Montreal Cognitive Assessment
    """

    # Visuospatial/executive
    alternate_trail = models.PositiveIntegerField(_('Alternating trail making'), choices=choice_numbers(1))
    cube = models.PositiveIntegerField(_('Cube'), choices=choice_numbers(1))
    clock_contour = models.PositiveIntegerField(_('Contour'), choices=choice_numbers(1))
    clock_numbers = models.PositiveIntegerField(_('Numbers'), choices=choice_numbers(1))
    clock_hands = models.PositiveIntegerField(pgettext_lazy('clock hands', 'Hands'), choices=choice_numbers(1))

    # Naming
    naming_lion = models.PositiveIntegerField(_('Lion'), choices=choice_numbers(1))
    naming_rhino = models.PositiveIntegerField(_('Rhino'), choices=choice_numbers(1))
    naming_camel = models.PositiveIntegerField(_('Camel'), choices=choice_numbers(1))

    # Memory
    memory_face_1 = models.PositiveIntegerField(_('1st trial'), choices=choice_numbers(1))
    memory_velvet_1 = models.PositiveIntegerField(_('Velvet'), choices=choice_numbers(1))
    memory_church_1 = models.PositiveIntegerField(_('Church'), choices=choice_numbers(1))
    memory_daisy_1 = models.PositiveIntegerField(_('Daisy'), choices=choice_numbers(1))
    memory_red_1 = models.PositiveIntegerField(_('Red'), choices=choice_numbers(1))
    memory_face_2 = models.PositiveIntegerField(_('2nd trial'), choices=choice_numbers(1))
    memory_velvet_2 = models.PositiveIntegerField(_('Velvet'), choices=choice_numbers(1))
    memory_church_2 = models.PositiveIntegerField(_('Church'), choices=choice_numbers(1))
    memory_daisy_2 = models.PositiveIntegerField(_('Daisy'), choices=choice_numbers(1))
    memory_red_2 = models.PositiveIntegerField(_('Red'), choices=choice_numbers(1))

    # Attention
    forward_digit_span = models.PositiveIntegerField(_('Forward digit span'), choices=choice_numbers(1))
    backward_digit_span = models.PositiveIntegerField(_('Backward digit span'), choices=choice_numbers(1))
    vigilance = models.PositiveIntegerField(_('Vigilance'), choices=choice_numbers(1))
    serial_7s_93 = models.PositiveIntegerField(_('93'), choices=choice_numbers(1))
    serial_7s_86 = models.PositiveIntegerField(_('86'), choices=choice_numbers(1))
    serial_7s_79 = models.PositiveIntegerField(_('79'), choices=choice_numbers(1))
    serial_7s_72 = models.PositiveIntegerField(_('72'), choices=choice_numbers(1))
    serial_7s_65 = models.PositiveIntegerField(_('65'), choices=choice_numbers(1))

    # Language
    repeat_1 = models.PositiveIntegerField(choices=choice_numbers(1))
    repeat_2 = models.PositiveIntegerField(choices=choice_numbers(1))
    verbal_fluency = models.PositiveIntegerField(choices=choice_numbers(1))

    # Abstraction
    abstraction_1 = models.PositiveIntegerField(choices=choice_numbers(1))
    abstraction_2 = models.PositiveIntegerField(choices=choice_numbers(1))

    # Delayed memory (recall)
    late_memory_face_no_cue = models.PositiveIntegerField(_('With no cue'), choices=choice_numbers(1))
    late_memory_velvet_no_cue = models.PositiveIntegerField(_('Velvet'), choices=choice_numbers(1))
    late_memory_church_no_cue = models.PositiveIntegerField(_('Church'), choices=choice_numbers(1))
    late_memory_daisy_no_cue = models.PositiveIntegerField(_('Daisy'), choices=choice_numbers(1))
    late_memory_red_no_cue = models.PositiveIntegerField(_('Red'), choices=choice_numbers(1))
    late_memory_face_category = models.PositiveIntegerField(_('Categorie cue'), choices=choice_numbers(1),
                                                            null=True, blank=True)
    late_memory_velvet_category = models.PositiveIntegerField(_('Velvet'), choices=choice_numbers(1),
                                                              null=True, blank=True)
    late_memory_church_category = models.PositiveIntegerField(_('Church'), choices=choice_numbers(1),
                                                              null=True, blank=True)
    late_memory_daisy_category = models.PositiveIntegerField(_('Daisy'), choices=choice_numbers(1),
                                                             null=True, blank=True)
    late_memory_red_category = models.PositiveIntegerField(_('Red'), choices=choice_numbers(1),
                                                           null=True, blank=True)
    late_memory_face_multiple_choice = models.PositiveIntegerField(_('Multiple choice cue'), choices=choice_numbers(1),
                                                                   null=True, blank=True)
    late_memory_velvet_multiple_choice = models.PositiveIntegerField(_('Velvet'), choices=choice_numbers(1),
                                                                     null=True, blank=True)
    late_memory_church_multiple_choice = models.PositiveIntegerField(_('Church'), choices=choice_numbers(1),
                                                                     null=True, blank=True)
    late_memory_daisy_multiple_choice = models.PositiveIntegerField(_('Daisy'), choices=choice_numbers(1),
                                                                    null=True, blank=True)
    late_memory_red_multiple_choice = models.PositiveIntegerField(_('Red'), choices=choice_numbers(1),
                                                                  null=True, blank=True)

    # Orientation
    orientation_date = models.PositiveIntegerField(_('Date'), choices=choice_numbers(1))
    orientation_month = models.PositiveIntegerField(_('Month'), choices=choice_numbers(1))
    orientation_year = models.PositiveIntegerField(_('Year'), choices=choice_numbers(1))
    orientation_day = models.PositiveIntegerField(_('Day'), choices=choice_numbers(1))
    orientation_place = models.PositiveIntegerField(_('Place'), choices=choice_numbers(1))
    orientation_city = models.PositiveIntegerField(_('City'), choices=choice_numbers(1))

    class Meta:
        verbose_name = _('MoCA')
        verbose_name_plural = _('MoCA')

    def total(self):
        """
        Calculates the total score of the test
        :return: The total score
        """
        tot = self.alternate_trail + self.cube + self.clock_contour + self.clock_numbers + self.clock_hands
        tot += self.naming_lion + self.naming_rhino + self.naming_camel + self.forward_digit_span
        tot += self.backward_digit_span + self.vigilance + self.repeat_1 + self.repeat_2
        tot += self.abstraction_1 + self.abstraction_2 + self.late_memory_face_no_cue + self.late_memory_velvet_no_cue
        tot += self.late_memory_church_no_cue + self.late_memory_daisy_no_cue + self.late_memory_red_no_cue
        tot += self.orientation_date + self.orientation_month + self.orientation_year + self.orientation_day
        tot += self.orientation_place + self.orientation_city
        serial_7s = self.serial_7s_93 + self.serial_7s_86 + self.serial_7s_79 + self.serial_7s_72 + self.serial_7s_65
        if serial_7s < 2:
            tot += serial_7s
        elif serial_7s < 4:
            tot += 2
        else:
            tot += 3

        if self.verbal_fluency > 10:
            tot += 1

        return tot
