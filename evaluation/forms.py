# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .widgets import ButtonRadioSelect, ButtonRadioGridChoiceInput, ButtonRadioHorizontalSelect, StepNumberInput
from .mixin import ControlNTFormMixin
from .models.kviq import KVIQ, NT, CHOICES_VISUAL_IMAGES, CHOICES_CINE_IMAGES
from .models.eeg import Eeg
from .models.fim import FIM

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
    imrea_nt = {'fields': ('visual_images', 'cine_images'),}
    
    visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                      choices=CHOICES_VISUAL_IMAGES,
                                      help_text=TEXT_VISUAL_IMAGES)
    cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
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

    self_care_eating = forms.ChoiceField(label=_('Eating'), widget=ButtonRadioHorizontalSelect())
    self_care_grooming = forms.ChoiceField(label=_('Grooming'), widget=ButtonRadioHorizontalSelect())
    self_care_bathing = forms.ChoiceField(label=_('Bathing/showering'), widget=ButtonRadioHorizontalSelect())
    self_care_dressing_upper_body = forms.ChoiceField(label=_('Dressing upper body'), widget=ButtonRadioHorizontalSelect())
    self_care_dressing_lower_body = forms.ChoiceField(label=_('Dressing lower body'), widget=ButtonRadioHorizontalSelect())
    self_care_toileting = forms.ChoiceField(label=_('Toileting'), widget=ButtonRadioHorizontalSelect())
    sphincter_bladder_mgt = forms.ChoiceField(label=_('Bladder management'), widget=ButtonRadioHorizontalSelect())
    sphincter_bowel_mgt = forms.ChoiceField(label=_('Bowel management'), widget=ButtonRadioHorizontalSelect())
    transfer_wheelchair = forms.ChoiceField(label=_('Transfers bed/chair/wheelchair'), widget=ButtonRadioHorizontalSelect())
    transfer_toilet = forms.ChoiceField(label=_('Transfers toilet'), widget=ButtonRadioHorizontalSelect())
    transfer_shower = forms.ChoiceField(label=_('Transfers bathtub/shower'), widget=ButtonRadioHorizontalSelect())
    locomotion_wheelchair = forms.ChoiceField(label=_('Locomotion walking/wheelchair'), widget=ButtonRadioHorizontalSelect())
    locomotion_stairs = forms.ChoiceField(label=_('Locomotion stairs'), widget=ButtonRadioHorizontalSelect())
    
    def __init__(self, *args, **kwargs):
        super(FIMAdminForm, self).__init__(*args, **kwargs)
        sorted_choices = sorted(FIM.FIM_CHOICES_CATEGORY, key=lambda x: x[1], reverse=False)
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


        