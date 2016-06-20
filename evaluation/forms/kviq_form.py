# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioSelect
from ..mixin import ControlNTFormMixin
from ..models.kviq import CHOICES_VISUAL_IMAGES, CHOICES_CINE_IMAGES

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

    neck_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                           choices=CHOICES_VISUAL_IMAGES)
    neck_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                         choices=CHOICES_CINE_IMAGES)
    shoulder_elevation_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                         choices=CHOICES_VISUAL_IMAGES)
    shoulder_elevation_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                       choices=CHOICES_CINE_IMAGES)
    shoulder_flexion_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                           choices=CHOICES_VISUAL_IMAGES)
    shoulder_flexion_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                         choices=CHOICES_CINE_IMAGES)
    shoulder_flexion_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                               choices=CHOICES_VISUAL_IMAGES)
    shoulder_flexion_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                             choices=CHOICES_CINE_IMAGES)
    elbow_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                choices=CHOICES_VISUAL_IMAGES)
    elbow_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                              choices=CHOICES_CINE_IMAGES)
    elbow_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                    choices=CHOICES_VISUAL_IMAGES)
    elbow_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                  choices=CHOICES_CINE_IMAGES)
    thumb_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                choices=CHOICES_VISUAL_IMAGES)
    thumb_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                              choices=CHOICES_CINE_IMAGES)
    thumb_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                    choices=CHOICES_VISUAL_IMAGES)
    thumb_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                  choices=CHOICES_CINE_IMAGES)
    trunk_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                            choices=CHOICES_VISUAL_IMAGES)
    trunk_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                          choices=CHOICES_CINE_IMAGES)
    knee_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                               choices=CHOICES_VISUAL_IMAGES)
    knee_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                             choices=CHOICES_CINE_IMAGES)
    knee_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                   choices=CHOICES_VISUAL_IMAGES)
    knee_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                 choices=CHOICES_CINE_IMAGES)
    hip_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                              choices=CHOICES_VISUAL_IMAGES)
    hip_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                            choices=CHOICES_CINE_IMAGES)
    hip_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                  choices=CHOICES_VISUAL_IMAGES)
    hip_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                choices=CHOICES_CINE_IMAGES)
    foot_tapping_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                       choices=CHOICES_VISUAL_IMAGES)
    foot_tapping_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                     choices=CHOICES_CINE_IMAGES)
    foot_tapping_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                           choices=CHOICES_VISUAL_IMAGES)
    foot_tapping_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                         choices=CHOICES_CINE_IMAGES)
    foot_rotation_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                        choices=CHOICES_VISUAL_IMAGES)
    foot_rotation_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                      choices=CHOICES_CINE_IMAGES)
    foot_rotation_not_dom_visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                            choices=CHOICES_VISUAL_IMAGES)
    foot_rotation_not_dom_cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                                          choices=CHOICES_CINE_IMAGES)

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }
