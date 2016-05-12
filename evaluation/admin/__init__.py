from django.contrib import admin
from .kviq_admin import KVIQAdmin
from .sis_admin import SISAdmin
from .bostonaphasia_admin import BostonAphasiaAdmin
from .eeg_admin import EegAdmin
from .fim_admin import FIMAdmin
from .patient_admin import PatientAdmin

from evaluation.models import Period

admin.site.register(Period)