from django.contrib import admin
from .kviq_admin import KVIQAdmin
from .sis_admin import SISAdmin
from .bostonaphasia_admin import BostonAphasiaAdmin
from .eeg_admin import EegAdmin
from .fim_admin import FIMAdmin

from evaluation.models import Patient, Period

admin.site.register(Patient)
admin.site.register(Period)