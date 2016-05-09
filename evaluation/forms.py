# -*- coding: utf-8 -*-
from django import forms
from .widgets import ButtonRadioSelect, ButtonRadioGridChoiceInput, ButtonRadioHorizontalSelect, StepNumberInput
from .mixin import ControlNTFormMixin
from .models.kviq import KVIQ, NT, CHOICES_VISUAL_IMAGES, CHOICES_CINE_IMAGES
from .models.eeg import Eeg
from .models.fim import FIM, FIM_CHOICES_CATEGORY

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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
class KVIQAdminForm(ControlNTFormMixin, forms.ModelForm):
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
            'all': ('css/KVIQ.css',)
        }
        

class SISAdminForm(forms.ModelForm):

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }


class BostonAphasiaForm(forms.ModelForm):
    write_or_distribute_card_deck_left_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min':0, 'max':2}))
    write_or_distribute_card_deck_right_hand = forms.IntegerField(widget=StepNumberInput(attrs={'min':0, 'max':2}))

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }
        js = ('js/jquery.bootstrap-touchspin.js',)


class EegAdminForm(forms.ModelForm):

    class Meta:
        model = Eeg
        fields = ['patient', 'eegfile', 'eegtitle']

class FIMAdminForm(forms.ModelForm):
    
    self_care_eating = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    self_care_grooming = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    self_care_bathing = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    self_care_dressing_upper_body = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    self_care_dressing_lower_body = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    self_care_toileting = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    sphincter_bladder_mgt = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    sphincter_bowel_mgt = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    transfer_wheelchair = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    transfer_toilet = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    transfer_shower = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    locomotion_wheelchair = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    locomotion_stairs = forms.ChoiceField(widget=ButtonRadioHorizontalSelect())
    
    def __init__(self, *args, **kwargs):
        super(FIMAdminForm, self).__init__(*args, **kwargs)
        sorted_choices = sorted(FIM_CHOICES_CATEGORY, key=lambda x: x[1], reverse=False)
        self.fields['self_care_eating'].choices = sorted_choices
        self.fields['self_care_grooming'].choices = sorted_choices
        self.fields['self_care_bathing'].choices = sorted_choices
        self.fields['self_care_dressing_upper_body'].choices = sorted_choices
        self.fields['self_care_dressing_lower_body'].choices = sorted_choices
        self.fields['self_care_toileting'].choices = sorted_choices
        self.fields['sphincter_bladder_mgt'].choices = sorted_choices
        self.fields['sphincter_bowel_mgt'].choices = sorted_choices
        self.fields['transfer_wheelchair'].choices = sorted_choices
        self.fields['transfer_toilet'].choices = sorted_choices
        self.fields['transfer_shower'].choices = sorted_choices
        self.fields['locomotion_wheelchair'].choices = sorted_choices
        self.fields['locomotion_stairs'].choices = sorted_choices
    
    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }


        