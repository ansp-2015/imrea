# -*- coding: utf-8 -*-
from django import forms
from .widgets import ButtonRadioSelect
from .models.kviq import KVIQ

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


class KVIQAdminForm(forms.ModelForm):
    visual_images = forms.ChoiceField(widget=ButtonRadioSelect(),
                                      choices=KVIQ.CHOICES_VISUAL_IMAGES,
                                      help_text=TEXT_VISUAL_IMAGES)
    cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),choices=KVIQ.CHOICES_CINE_IMAGES)

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }
        

class SISAdminForm(forms.ModelForm):
    

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }