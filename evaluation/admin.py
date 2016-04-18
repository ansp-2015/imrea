# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import KVIQ, Patient
from .models import CHOICES_CINE_IMAGES, CHOICES_VISUAL_IMAGES
from .forms import KVIQAdminForm
from django.utils.translation import ugettext_lazy as _
# Register your models here.


class KVIQAdmin(admin.ModelAdmin):

    form = KVIQAdminForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient',),
        }),
        (_(u'Neck'), {
            'fields': ('visual_images', 'cine_images'),
        })
    )

admin.site.register(KVIQ, KVIQAdmin)
admin.site.register(Patient)