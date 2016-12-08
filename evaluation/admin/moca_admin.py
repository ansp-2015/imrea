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
            }
        }),
        (_('Memory'), {
            'fields': (('memory_face_1', 'memory_velvet_1', 'memory_church_1', 'memory_daisy_1', 'memory_red_1'),
                       ('memory_face_2', 'memory_velvet_2', 'memory_church_2', 'memory_daisy_2', 'memory_red_2'),),
            'description': {
                'fieldset': '_table',
            }
        }),
        (_('Attention'), {
            'fields': (('forward_digit_span', 'backward_digit_span'), ('vigilance',),
                       ('serial_7s_93', 'serial_7s_86', 'serial_7s_79', 'serial_7s_72', 'serial_7s_65')),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Language'), {
            'fields': (('repeat_1', 'repeat_2'), ('verbal_fluency',)),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Abstraction'), {
            'fields': (('abstraction_1', 'abstraction_2'),),
            'description': {
                'fieldset': '_1col',
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
                'fieldset': '_table',
                'columns': ((0, ''), (1, _('Face')), (2, _('Velvet')), (3, _('Church')), (4, _('Daisy')), (5, _('Red')))
            }
        }),
        (_('Orientation'), {
            'fields': (('orientation_date', 'orientation_month', 'orientation_year', 'orientation_day',
                        'orientation_place', 'orientation_city'),),
            'description': {
                'fieldset': '_1col',
            }
        }),
    )
    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(MoCA, MoCAAdmin)
