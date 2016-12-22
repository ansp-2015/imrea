from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from django.forms.widgets import RadioFieldRenderer, RadioSelect, RadioChoiceInput, TextInput, CheckboxInput
import logging
from evaluation.models.base_evaluation import BaseEvaluation

# Get an instance of a logger
from django.utils.safestring import mark_safe

logger = logging.getLogger(__name__)

__author__ = 'antonio'



###
# Radio with buttons
###
class ButtonRadioChoiceInput(RadioChoiceInput):
    def render(self, name=None, value=None, attrs=None):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        if self.is_checked():
            active = ' active'
        else:
            active = ''
        return format_html(
            '<label{} class="btn-choice btn btn-primary{}">{} {}</label>',
            label_for, active, self.tag(attrs), self.choice_label
        )


class ButtonRadioRenderer(RadioFieldRenderer):
    choice_input_class = ButtonRadioChoiceInput
    orientation = 'vertical'
    outer_html = '<div class="btn-toolbar" role="toolbar">\n<div class="btn-group-vertical" role="group" data-toggle="buttons"{id_attr}>{content}</div></div>'
    inner_html = '{choice_value}{sub_widgets}'
    
    def __init__(self, *args, **kwargs):
        super(ButtonRadioRenderer, self).__init__(*args, **kwargs)
        self.outer_html = '<div class="btn-toolbar" role="toolbar">\n<div class="btn-group-%s" role="group" data-toggle="buttons"{id_attr}>{content}</div></div>' % self.orientation


class ButtonRadioSelect(RadioSelect):
    renderer = ButtonRadioRenderer


###
# Radio with buttons horizontal.
# Display choice ids.
###
class ButtonRadioChoiceValueInput(RadioChoiceInput):
    def render(self, name=None, value=None, attrs=None):

        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)

        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        if self.is_checked():
            active = ' active'
        else:
            active = ''

        # Empty choice.
        value = '---'
        if self.choice_value:
            # override value if it is a custom value like NOT DEFINED or MISSING DATA
            if self.choice_value.startswith('-') and self.choice_value[1:].isdigit():
                value = self.choice_label
            else:
                value = self.choice_value

        return format_html(
            '<label{} class="btn-choice btn btn-primary{}">{} {}</label>',
            label_for, active, self.tag(attrs), value
        )

class ButtonRadioHorizontalValueRenderer(ButtonRadioRenderer):
    orientation = 'horizontal'
    choice_input_class = ButtonRadioChoiceValueInput


class ButtonRadioHorizontalValueSelect(RadioSelect):
    renderer = ButtonRadioHorizontalValueRenderer

###
# Radio with buttons horizontal
# Display label value.
###
class ButtonRadioChoiceLabelInput(RadioChoiceInput):
    def render(self, name=None, value=None, attrs=None):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        if self.is_checked():
            active = ' active'
        else:
            active = ''
        return format_html(
            '<label{} class="btn-choice btn btn-primary{}">{} {}</label>',
            label_for, active, self.tag(attrs), self.choice_label
        )

class ButtonRadioHorizontalLabelRenderer(ButtonRadioRenderer):
    orientation = 'horizontal'
    choice_input_class = ButtonRadioChoiceLabelInput

class ButtonRadioHorizontalLabelSelect(RadioSelect):
    renderer = ButtonRadioHorizontalLabelRenderer


###
# Radio in a grid table
###
class ButtonRadioGridChoiceInput(RadioChoiceInput):
    def render(self, name=None, value=None, attrs=None):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''
        attrs = dict(self.attrs, **attrs) if attrs else self.attrs
        if self.is_checked():
            active = ' active'
        else:
            active = ''

        # Empty choice.
        value = '---'
        if self.choice_value:
            # override value if it is a custom value like NOT DEFINED or MISSING DATA
            if self.choice_value.startswith('-') and self.choice_value[1:].isdigit():
                value = self.choice_label
            else:
                value = self.choice_value

        return format_html(
            '<td class="btn-group" style="position:relative;text-align:center;"><label{} class="btn-choice btn btn-primary{}">{} {}</label></td>',
            label_for, active, self.tag(attrs), value
        )


class ButtonRadioGridRenderer(RadioFieldRenderer):
    choice_input_class = ButtonRadioGridChoiceInput
    outer_html = '{content}'
    inner_html = '{choice_value}{sub_widgets}'


class ButtonRadioGridSelect(RadioSelect):
    renderer = ButtonRadioGridRenderer


###
# Input with '+' and '-' buttons for integers and floats with step
###
class StepNumberInput(TextInput):
    def render(self, name, value, attrs=None):
        min_value = 0
        max_value = 99999
        step = 1
        decimals = 1

        if self.attrs is not None:
            min_value = self.attrs.pop('min', min_value)
            max_value = self.attrs.pop('max', max_value)
            step = self.attrs.pop('step', step)
            decimals = self.attrs.pop('decimals', decimals)

        winput = super(StepNumberInput, self).render(name, value, attrs)


        extra = ''
        if isinstance(step, float):
            extra = mark_safe("forcestepdivisibility:'none',decimals:%d," % decimals)

        NT_button = mark_safe("postfix: 'NT', postfix_extraclass: 'btn btn-default'")

        spinner_script_template = """
            <script>
                $("input[name='{}']").addClass("centerInput");
                $("input[name='{}']").TouchSpin({{min:{},max:{},{}step:{}, {}
                                      }});
                // spinner script NT
                {}
                // spinner script NT value
                {}

            </script>
        """

        # spinner button script
        spinner_script_button_nt = format_html("""
            $("input[name='{}']").siblings("span.bootstrap-touchspin-postfix").click(function() {{ $("input[name='{}']").val('NT') }});
            """, name, name)

        # script to set NT value to the spinner value
        spinner_script_nt_value = ""
        if value == BaseEvaluation.UN[0][0]:
            spinner_script_nt_value = format_html("""
                $("input[name='{}']").val('NT');
                """, name)

        spinner_script = format_html(spinner_script_template, name, name, min_value, max_value, extra, step, NT_button, spinner_script_button_nt, spinner_script_nt_value )

        div_buttons = """
            <div class="div-spinner">
                <div class="input-group bootstrap-touchspin">
                    {}
                </div>
                {}
            </div>
            """

        return format_html(div_buttons, winput, spinner_script)


###
# Checkbox for 0/1 integers
###
def boolean_check(v):
    return not (v is False or v is None or v == '' or v == 0)


class IntegerCheckboxInput(CheckboxInput):

    def __init__(self, attrs=None, check_test=boolean_check):
        super(IntegerCheckboxInput, self).__init__(attrs, check_test)

    def render(self, name, value, attrs=None):
        if not attrs:
            attrs = {}
        attrs.update({'data-on-text': _('Yes'), 'data-off-text': _('No'), 'data-size': 'normal',
                      'data-handle-width': '50px'})
        return_html = super(IntegerCheckboxInput, self).render(name, value, attrs)
        checkbox = """
        {}
        <script type="text/javascript">
        $("[name='{}']").bootstrapSwitch().on('switchChange.bootstrapSwitch',
        function(event, state){{ change_state(this, state); }});
        </script>
        """
        return format_html(checkbox, return_html, name)

    def value_from_datadict(self, data, files, name):
        value = super(IntegerCheckboxInput, self).value_from_datadict(data, files, name)
        return 1 if value is True else 0
