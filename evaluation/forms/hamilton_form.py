# -*- coding: utf-8 -*-
from django import forms
from ..widgets import ButtonRadioHorizontalValueSelect
from ..models.hamilton import Hamilton
from django.utils.translation import ugettext_lazy as _

class HamiltonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(HamiltonForm, self).__init__(*args, **kwargs)
        self.fields['mood'].choices = Hamilton.MOOD
        self.fields['guilt'].choices = Hamilton.GUILT
        self.fields['suicide'].choices = Hamilton.SUICIDE
        self.fields['insomnia_early'].choices = Hamilton.INSOMINIA_EARLY
        self.fields['insomnia_middle'].choices = Hamilton.INSOMINIA_MIDDLE
        self.fields['insomnia_late'].choices = Hamilton.INSOMINIA_LATE
        self.fields['work'].choices = Hamilton.WORK
        self.fields['retardation'].choices = Hamilton.RETARDATION
        self.fields['agitation'].choices = Hamilton.AGITATION
        self.fields['anxiety_psychic'].choices = Hamilton.ANXIETY_PSYCHIC
        self.fields['anxiety_somatic'].choices = Hamilton.ANXIETY_SOMATIC
        self.fields['gastro'].choices = Hamilton.GASTRO
        self.fields['general'].choices = Hamilton.GENERAL
        self.fields['genital'].choices = Hamilton.GENITAL
        self.fields['hypochondriasis'].choices = Hamilton.HYPOCHONDRIASIS
        self.fields['weight_history'].choices = Hamilton.WEIGHT_HISTORY
        self.fields['weight_weekly'].choices = Hamilton.WEIGHT_WEEKLY
        self.fields['insight'].choices = Hamilton.INSIGHT

    class Media:
        css = {
            'all': ('css/evaluation_forms.css',)
        }

    class Meta:
        model = Hamilton
        fields = ['mood', 'guilt', 'suicide', 'insomnia_early', 'insomnia_middle', 'insomnia_late', 'work',
                  'retardation', 'agitation', 'anxiety_psychic', 'anxiety_somatic', 'gastro', 'general', 'genital',
                  'hypochondriasis', 'weight_history', 'weight_weekly', 'insight']
        widgets = {
            'mood': ButtonRadioHorizontalValueSelect(),
            'guilt': ButtonRadioHorizontalValueSelect(),
            'suicide': ButtonRadioHorizontalValueSelect(),
            'insomnia_early': ButtonRadioHorizontalValueSelect(),
            'insomnia_middle': ButtonRadioHorizontalValueSelect(),
            'insomnia_late': ButtonRadioHorizontalValueSelect(),
            'work': ButtonRadioHorizontalValueSelect(),
            'retardation': ButtonRadioHorizontalValueSelect(),
            'agitation': ButtonRadioHorizontalValueSelect(),
            'anxiety_psychic': ButtonRadioHorizontalValueSelect(),
            'anxiety_somatic': ButtonRadioHorizontalValueSelect(attrs={'text': _("(physiological concomitants of anxiety, such as - gastro-"
                                                                               "intestinal: dry mouth, wind, indigestion, diarrhea, cramps, belching. - "
                                                                               "cardio-vascular : palpitations, headaches. - respiratory: hyperventilation, "
                                                                               "sighing. - urinary frequency - sweating)")}),
            'gastro': ButtonRadioHorizontalValueSelect(),
            'general': ButtonRadioHorizontalValueSelect(),
            'genital': ButtonRadioHorizontalValueSelect(),
            'hypochondriasis': ButtonRadioHorizontalValueSelect(),
            'weight_history': ButtonRadioHorizontalValueSelect(attrs={'text': 'A. %s' % _(u'When rating by history')}),
            'weight_weekly': ButtonRadioHorizontalValueSelect(attrs={'text': 'B. %s' % _(u'On Weekly Ratings by Ward Psychiatrist, when Actual changes are Measured')}),
            'insight': ButtonRadioHorizontalValueSelect(),
        }
