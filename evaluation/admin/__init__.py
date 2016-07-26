from django.contrib import admin
from .patient_admin import PatientAdmin
from .base_admin import BaseAdmin
from ..util import all_evaluations

from evaluation.models import Period

for c in all_evaluations():
    exec('from .%s_admin import %sAdmin' % c[:2])

admin.site.register(Period)