# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.moca import MoCA
from ..forms import MoCAForm


class MoCAAdmin(BaseAdmin):
    """
    Visual Analog Scale
    """

    form = MoCAForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
            }
        }),
        (_('Visuospatial/Executive'), {
            'fields': (('alternate_trail', 'cube'), ('clock_contour', 'clock_numbers', 'clock_hands')),
            'description': {
                'fieldset': '_1col',
                'fieldset_total_points': 5,
                'fieldset_total_addend_fields': ('alternate_trail', 'cube', 'clock_contour', 'clock_numbers',
                                                 'clock_hands'),
                'fieldset_total_field': 'visuospatial_total',
            }
        }),
        (_('Naming'), {
            'fields': (('naming_lion', 'naming_rhino', 'naming_camel'),),
            'description': {
                'fieldset': '_1col',
                'fieldset_total_points': 3,
                'fieldset_total_addend_fields': ('naming_lion', 'naming_rhino', 'naming_camel'),
                'fieldset_total_field': 'naming_total',
            }
        }),
        (_('Memory'), {
            'fields': (('memory_face_1', 'memory_velvet_1', 'memory_church_1', 'memory_daisy_1', 'memory_red_1'),
                       ('memory_face_2', 'memory_velvet_2', 'memory_church_2', 'memory_daisy_2', 'memory_red_2'),),
            'description': {
                'text': _('Read list of words, subject must repeat them. Do 2 trials, even if 1st trial is successful. Do a recall after 5 minutes. FACE - VELVET - CHURCH - DAISY - RED'),
                'fieldset': '_table',
            }
        }),
        (_('Attention'), {
            'fields': (('forward_digit_span', 'backward_digit_span'), ('vigilance',)),
            'description': {
                'text': _('Read list of digits ( digit/sec.).'),
                'fieldset': '/moca/fieldset_attention',
                'fieldset_total_points': 3,
                'fieldset_total_addend_fields': ('forward_digit_span', 'backward_digit_span', 'vigilance'),
                'fieldset_total_field': 'attention_total',

            }
        }),

        (_('Attention serial'), {
            'fields': ((), ('serial_7s_93', 'serial_7s_86', 'serial_7s_79', 'serial_7s_72', 'serial_7s_65')),
            'description': {
                'text': _(u'Serial 7 subtraction starting at 100. 4 or 5 correct subtractions: <strong>3pts</strong>, 2 or 3 correct: <strong>2 pts</strong>, 1 correct: <strong>1 pt</strong>, 0 correct: <strong>0 pt</strong>.'),
                'fieldset': '/moca/fieldset_attention_serial',
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('serial_7s_93', 'serial_7s_86', 'serial_7s_79', 'serial_7s_72',
                                                 'serial_7s_65'),
                'fieldset_total_field': 'attention_serial_total',
                'fieldset_total_addend_field_prefix': '',
            }
        }),
        (_('Language'), {
            'fields': (('repeat_1', 'repeat_2'), ('verbal_fluency',)),
            'description': {
                'fieldset': '_1col',
                'column_width': 7,
                'fieldset_total_points': 3,
                'fieldset_total_addend_fields': ('repeat_1', 'repeat_2', 'verbal_fluency'),
                'fieldset_total_field': 'language_total',
            }
        }),
        (_('Abstraction'), {
            'fields': (('abstraction_1', 'abstraction_2'),),
            'description': {
                'fieldset': '_1col',
                'column_width': 4,
                'fieldset_total_points': 2,
                'fieldset_total_addend_fields': ('abstraction_1', 'abstraction_2'),
                'fieldset_total_field': 'abstraction_total',
            }
        }),
        (_('Delayed recall'), {
            'fields': (('late_memory_face_no_cue', 'late_memory_velvet_no_cue', 'late_memory_church_no_cue',
                        'late_memory_daisy_no_cue', 'late_memory_red_no_cue',),
                       ('late_memory_face_category', 'late_memory_velvet_category', 'late_memory_church_category',
                        'late_memory_daisy_category', 'late_memory_red_category',),
                       ('late_memory_face_multiple_choice', 'late_memory_velvet_multiple_choice',
                        'late_memory_church_multiple_choice', 'late_memory_daisy_multiple_choice',
                        'late_memory_red_multiple_choice',),
                       ),
            'description': {
                'text': _(u'Has to recall words'),
                'fieldset': '_table',
                'columns': ((0, ''), (1, _('Face')), (2, _('Velvet')), (3, _('Church')), (4, _('Daisy')), (5, _('Red'))),
                'fieldset_total_points': 5,
                'fieldset_total_addend_fields': ('late_memory_face_no_cue', 'late_memory_velvet_no_cue', 'late_memory_church_no_cue',
                        'late_memory_daisy_no_cue', 'late_memory_red_no_cue',),
                'fieldset_total_field': 'delayed_recall_total',
            }
        }),
        (_('Orientation'), {
            'fields': (('orientation_date', 'orientation_month', 'orientation_year', 'orientation_day',
                        'orientation_place', 'orientation_city'),),
            'description': {
                'fieldset': '_1col',
                'fieldset_total_points': 6,
                'fieldset_total_addend_fields': ('orientation_date', 'orientation_month', 'orientation_year', 'orientation_day',
                        'orientation_place', 'orientation_city'),
                'fieldset_total_field': 'orientation_total',
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(MoCA, MoCAAdmin)
