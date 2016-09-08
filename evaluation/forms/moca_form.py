from django import forms
from ..widgets import IntegerCheckboxInput
from ..models import MoCA
from ..util import choice_numbers


class MoCAForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MoCAForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            if f not in ['patient', 'period']:
                choices = self.fields[f].choices
                self.fields[f].choices = choice_numbers(1)

    class Media:
        css = {
            'all': ('css/evaluation_forms.css', 'css/bootstrap-switch.min.css')
        }
        js = ('js/jquery.bootstrap-touchspin.js', 'js/bootstrap-switch.min.js', 'js/evaluation.js')

    class Meta:
        model = MoCA
        fields = ['alternate_trail', 'cube',]

        widgets = {
            'alternate_trail': IntegerCheckboxInput(),
            'cube': IntegerCheckboxInput(),
            'clock_contour': IntegerCheckboxInput(),
            'clock_numbers': IntegerCheckboxInput(),
            'clock_hands': IntegerCheckboxInput(),
            'naming_lion': IntegerCheckboxInput(),
            'naming_rhino': IntegerCheckboxInput(),
            'naming_camel': IntegerCheckboxInput(),
            'memory_face_1': IntegerCheckboxInput(),
            'memory_velvet_1': IntegerCheckboxInput(),
            'memory_church_1': IntegerCheckboxInput(),
            'memory_daisy_1': IntegerCheckboxInput(),
            'memory_red_1': IntegerCheckboxInput(),
            'memory_face_2': IntegerCheckboxInput(),
            'memory_velvet_2': IntegerCheckboxInput(),
            'memory_church_2': IntegerCheckboxInput(),
            'memory_daisy_2': IntegerCheckboxInput(),
            'memory_red_2': IntegerCheckboxInput(),
            'forward_digit_span': IntegerCheckboxInput(),
            'backward_digit_span': IntegerCheckboxInput(),
            'vigilance': IntegerCheckboxInput(),
            'serial_7s_93': IntegerCheckboxInput(),
            'serial_7s_86': IntegerCheckboxInput(),
            'serial_7s_79': IntegerCheckboxInput(),
            'serial_7s_72': IntegerCheckboxInput(),
            'serial_7s_65': IntegerCheckboxInput(),
            'repeat_1': IntegerCheckboxInput(),
            'repeat_2': IntegerCheckboxInput(),
            'verbal_fluency': IntegerCheckboxInput(),
            'abstraction_1': IntegerCheckboxInput(),
            'abstraction_2': IntegerCheckboxInput(),
            'late_memory_face_no_cue': IntegerCheckboxInput(),
            'late_memory_velvet_no_cue': IntegerCheckboxInput(),
            'late_memory_church_no_cue': IntegerCheckboxInput(),
            'late_memory_daisy_no_cue': IntegerCheckboxInput(),
            'late_memory_red_no_cue': IntegerCheckboxInput(),
            'late_memory_face_category': IntegerCheckboxInput(),
            'late_memory_velvet_category': IntegerCheckboxInput(),
            'late_memory_church_category': IntegerCheckboxInput(),
            'late_memory_daisy_category': IntegerCheckboxInput(),
            'late_memory_red_category': IntegerCheckboxInput(),
            'late_memory_face_multiple_choice': IntegerCheckboxInput(),
            'late_memory_velvet_multiple_choice': IntegerCheckboxInput(),
            'late_memory_church_multiple_choice': IntegerCheckboxInput(),
            'late_memory_daisy_multiple_choice': IntegerCheckboxInput(),
            'late_memory_red_multiple_choice': IntegerCheckboxInput(),
            'orientation_date': IntegerCheckboxInput(),
            'orientation_month': IntegerCheckboxInput(),
            'orientation_year': IntegerCheckboxInput(),
            'orientation_day': IntegerCheckboxInput(),
            'orientation_place': IntegerCheckboxInput(),
            'orientation_city': IntegerCheckboxInput(),
        }