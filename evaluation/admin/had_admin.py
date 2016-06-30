# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from ..models import HAD
from ..forms import HADForm

logger = logging.getLogger(__name__)

class HADAdmin(BaseAdmin):

    form = HADForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {'fieldset': '_patient'}
        }),
        (None, {
            'fields': (('tension',),
                       ('enjoy',),
                       ('frightened',),
                       ('laugh',),
                       ('worry',),
                       ('cheerful',),
                       ('ease',),
                       ('slowed',),
                       ('butterflies',),
                       ('appearance',),
                       ('restless',),
                       ('forward',),
                       ('panic',),
                       ('book',)),
            'description': {
                'fieldset': '_1col_with_choices'
            }
        }),
    )


admin.site.register(HAD, HADAdmin)
# Registrando no reversion-compare
patch_admin(HAD)
