from .kviq_admin import KVIQAdmin
from .sis_admin import SISAdmin
from .bostonaphasia_admin import BostonAphasiaAdmin
from .eeg_admin import EegAdmin
from .fim_admin import FIMAdmin

from django.contrib import admin
from evaluation.models import Patient

admin.site.register(Patient)