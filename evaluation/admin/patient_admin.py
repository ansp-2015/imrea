from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion_compare.helpers import patch_admin
from evaluation.models.patient import Patient


class PatientAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('name', 'birthdate'),
            'description': {'fieldset': '_1col_panel'}
        }),
        (_(u'Social characteristics'), {
            'fields': ('age', 'gender', 'marital_status', 'profession', 'occupation',
                       'schooling_level', 'social_insurance_status', 'transportation_status'),
            'description': {'fieldset': '_1col_panel'}
        }),
        (_(u'Family support'), {
            'fields': ('fammily_ref_therapy', 'fammily_ref_home', 'fammily_composition',
                       'quantity_ppl_home'),
            'description': {'fieldset': '_1col_panel'}
        }),
        (_(u'Family support'), {
            'fields': ('fammily_ref_therapy', 'fammily_ref_home', 'fammily_composition',
                       'quantity_ppl_home'),
            'description': {'fieldset': '_1col_panel'}
        }),
        (_(u'Economic aspects'), {
            'fields': ('family_income', 'family_income_average',),
            'description': {'fieldset': '_1col_panel'}
        }),
        (_(u'Demographic data'), {
            'fields': ('origin_city', 'conducting_source',),
            'description': {'fieldset': '_1col_panel'}
        }),
    )

    # for removing add another option
    def has_add_permission(self, request):
        return True


admin.site.register(Patient, PatientAdmin)
# Registrando no reversion-compare
#patch_admin(Patient)


