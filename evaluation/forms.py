# -*- coding: utf-8 -*-
from django import forms
from .widgets import ButtonRadioSelect, ButtonRadioGridSelect
from .models.kviq import CHOICES_VISUAL_IMAGES, CHOICES_CINE_IMAGES
from .models.sis import CHOICES_STRENGTH
from django.utils.translation import ugettext_lazy as _

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
                                      choices=CHOICES_VISUAL_IMAGES,
                                      help_text=TEXT_VISUAL_IMAGES)
    cine_images = forms.ChoiceField(widget=ButtonRadioSelect(),choices=CHOICES_CINE_IMAGES)

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }
        

class SISAdminForm(forms.ModelForm):
    
    strength_arm = forms.ChoiceField(widget=ButtonRadioGridSelect(),
                                     label=_(u'arm that was most affected by your stroke?'),
                                     choices=CHOICES_STRENGTH)
    strength_hand = forms.ChoiceField(widget=ButtonRadioGridSelect(),
                                      label=_(u'grip of your hand that was most affected by your stroke?'),
                                     choices=CHOICES_STRENGTH)
    strength_leg = forms.ChoiceField(widget=ButtonRadioGridSelect(),
                                     label=_(u'leg tha was most affected by your stroke?'),
                                     choices=CHOICES_STRENGTH)
    strength_foot = forms.ChoiceField(widget=ButtonRadioGridSelect(),
                                      label=_(u'foot/ankle that was most affected by your stroke?'),
                                     choices=CHOICES_STRENGTH)

    class Media:
        css = {
            'all': ('css/KVIQ.css',)
        }