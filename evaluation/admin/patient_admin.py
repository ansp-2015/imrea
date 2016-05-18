from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from evaluation.models.patient import Patient


class PatientAdmin(admin.ModelAdmin):
    ## for removing add another option
    def has_add_permission(self, request):
        return True



admin.site.register(Patient, PatientAdmin)

