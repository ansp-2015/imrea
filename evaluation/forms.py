# -*- coding: utf-8 -*-
from django import forms
from .widgets import ButtonRadioSelect, StepNumberInput
from .mixin import ControlNTFormMixin
from .models.kviq import KVIQ, NT

# import the logging library
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
                                      choices=KVIQ.CHOICES_VISUAL_IMAGES,
                                      help_text=TEXT_VISUAL_IMAGES)
    cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                      choices=KVIQ.CHOICES_CINE_IMAGES)

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
