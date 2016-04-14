from django.contrib import admin
from .models import KVIQ, CHOICES_CINE_IMAGES, CHOICES_VISUAL_IMAGES

# Register your models here.


class KVIQAdmin(admin.ModelAdmin):

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['choices_v_images'] = CHOICES_VISUAL_IMAGES
        extra_context['choices_c_images'] = CHOICES_CINE_IMAGES

        return super(KVIQAdmin, self).change_view(request, object_id, form_url, extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['choices_v_images'] = CHOICES_VISUAL_IMAGES
        extra_context['choices_c_images'] = CHOICES_CINE_IMAGES

        return super(KVIQAdmin, self).add_view(request, form_url, extra_context)

admin.site.register(KVIQ, KVIQAdmin)