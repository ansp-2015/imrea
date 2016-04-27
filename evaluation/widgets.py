from __future__ import unicode_literals
from django.utils.html import format_html
from django.utils.safestring import mark_safe

__author__ = 'antonio'

from django.forms.widgets import RadioFieldRenderer, RadioSelect, RadioChoiceInput, TextInput


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
    outer_html = '<div class="btn-toolbar" role="toolbar">\n<div class="btn-group-vertical" role="group" data-toggle="buttons"{id_attr}>{content}</div></div>'
    inner_html = '{choice_value}{sub_widgets}'


class ButtonRadioSelect(RadioSelect):
    renderer = ButtonRadioRenderer


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
        return format_html(
            '<td class="btn-group" style="position:relative;text-align:center;"><label{} class="btn-choice btn btn-primary{}">{} {}</label></td>',
            label_for, active, self.tag(attrs), self.choice_value
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
        max_value = 10
        step = 1
        if self.attrs is not None:
            min_value = self.attrs.pop('min', min_value)
            max_value = self.attrs.pop('max', max_value)
            step = self.attrs.pop('step', step)

        input = super(StepNumberInput, self).render(name, value, attrs)

        extra = ''
        if isinstance(step, float):
            extra = mark_safe("forcestepdivisibility:'none',decimals:1,")
        div_buttons = """
        <div class="div-spinner">
            <div class="input-group bootstrap-touchspin">
                {}
            </div>
            <script>
                $("input[name='{}']").addClass("centerInput");
                $("input[name='{}']").TouchSpin({{min:{},max:{},{}step:{}
                                      }});
            </script>
        </div>
        """

        return format_html(div_buttons, input, name, name, min_value, max_value, extra, step)