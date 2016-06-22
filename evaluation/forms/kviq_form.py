# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioSelect
from ..mixin import ControlNTFormMixin
from ..models.kviq import KVIQ, CHOICES_VISUAL_IMAGES, CHOICES_CINE_IMAGES, CHOICES_DOMINANT_LIMB

TEXT_VISUAL_IMAGES = u"""
<ol class="ol-container">
                          <li>Sente-se ereto com a cabeça e as mãos apoiadas sobre as coxas</li>
                          <li>Incline a cabeça, tanto quanto possível, primeiro para a frente e depois
                            para trás</li>
                          <li>Retorne à posição inicial. Agora imagine o movimento, concentra-se na
                            clareza da imagem</li>
                          <li>Indicar na escala da qualidade do movimento imaginado</li>
                        </ol>
"""
class KVIQForm(ControlNTFormMixin, forms.ModelForm):
    imrea_nt = {'fields': ('neck_visual_images', 'neck_cine_images'),}

    def __init__(self, *args, **kwargs):
        super(KVIQForm, self).__init__(*args, **kwargs)

        self.fields['dominant_limb'].choices = CHOICES_DOMINANT_LIMB

        self.fields['neck_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['neck_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['shoulder_elevation_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['shoulder_elevation_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['shoulder_flexion_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['shoulder_flexion_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['shoulder_flexion_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['shoulder_flexion_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['elbow_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['elbow_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['elbow_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['elbow_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['thumb_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['thumb_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['thumb_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['thumb_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['trunk_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['trunk_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['knee_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['knee_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['knee_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['knee_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['hip_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['hip_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['hip_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['hip_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['foot_tapping_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['foot_tapping_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['foot_tapping_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['foot_tapping_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['foot_rotation_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['foot_rotation_dom_cine_images'].choices = CHOICES_CINE_IMAGES

        self.fields['foot_rotation_not_dom_visual_images'].choices = CHOICES_VISUAL_IMAGES
        self.fields['foot_rotation_not_dom_cine_images'].choices = CHOICES_CINE_IMAGES

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = KVIQ
        fields = ['patient', 'period', ]
        widgets = {
            'dominant_limb': ButtonRadioSelect(),
            'neck_visual_images': ButtonRadioSelect(),
            'neck_cine_images': ButtonRadioSelect(),
            'shoulder_elevation_visual_images': ButtonRadioSelect(),
            'shoulder_elevation_cine_images': ButtonRadioSelect(),
            'shoulder_flexion_dom_visual_images': ButtonRadioSelect(),
            'shoulder_flexion_dom_cine_images': ButtonRadioSelect(),
            'shoulder_flexion_not_dom_visual_images': ButtonRadioSelect(),
            'shoulder_flexion_not_dom_cine_images': ButtonRadioSelect(),
            'elbow_dom_visual_images': ButtonRadioSelect(),
            'elbow_dom_cine_images': ButtonRadioSelect(),
            'elbow_not_dom_visual_images': ButtonRadioSelect(),
            'elbow_not_dom_cine_images': ButtonRadioSelect(),
            'thumb_dom_visual_images': ButtonRadioSelect(),
            'thumb_dom_cine_images': ButtonRadioSelect(),
            'thumb_not_dom_visual_images': ButtonRadioSelect(),
            'thumb_not_dom_cine_images': ButtonRadioSelect(),
            'trunk_visual_images': ButtonRadioSelect(),
            'trunk_cine_images': ButtonRadioSelect(),
            'knee_dom_visual_images': ButtonRadioSelect(),
            'knee_dom_cine_images': ButtonRadioSelect(),
            'knee_not_dom_visual_images': ButtonRadioSelect(),
            'knee_not_dom_cine_images': ButtonRadioSelect(),
            'hip_dom_visual_images': ButtonRadioSelect(),
            'hip_dom_cine_images': ButtonRadioSelect(),
            'hip_not_dom_visual_images': ButtonRadioSelect(),
            'hip_not_dom_cine_images': ButtonRadioSelect(),
            'foot_tapping_dom_visual_images': ButtonRadioSelect(),
            'foot_tapping_dom_cine_images': ButtonRadioSelect(),
            'foot_tapping_not_dom_visual_images': ButtonRadioSelect(),
            'foot_tapping_not_dom_cine_images': ButtonRadioSelect(),
            'foot_rotation_dom_visual_images': ButtonRadioSelect(),
            'foot_rotation_dom_cine_images': ButtonRadioSelect(),
            'foot_rotation_not_dom_visual_images': ButtonRadioSelect(),
            'foot_rotation_not_dom_cine_images': ButtonRadioSelect()
        }
