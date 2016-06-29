from django.contrib import admin
from .kviq_admin import KVIQAdmin
from .sis_admin import SISAdmin
from .bostonaphasia_admin import BostonAphasiaAdmin
from .eeg_admin import EegAdmin
from .fim_admin import FIMAdmin
from .clin_admin import ClinAdmin
from .fuglmeyer_admin import FuglMeyerAdmin
from .had_admin import HADAdmin
from .hamilton_admin import HamiltonAdmin
from .patient_admin import PatientAdmin
from .base_admin import BaseAdmin

from evaluation.models import Period

admin.site.register(Period)