# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.nihss import NIHSS


logger = logging.getLogger(__name__)

class NIHSSAdmin(BaseAdmin):
    pass

admin.site.register(NIHSS, NIHSSAdmin)
# Registrando no reversion-compare
patch_admin(NIHSS)
