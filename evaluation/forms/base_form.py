# -*- coding: utf-8 -*-
from django import forms
from ..models.base_evaluation import BaseEvaluation


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        data = args[0] if args else kwargs.get('data', None)
        # Changing value for NT field value before Form clean validation
        if data:
            for partial_field_name in (self.get_nt_fields()):
                field_name = self.get_nt_field_prefix() + partial_field_name
                if data[field_name] and data[field_name] == 'NT':
                    data[field_name] = BaseEvaluation.UN[0][0]
        super(BaseForm, self).__init__(*args, **kwargs)

    def get_nt_fields(self):
        return []

    def get_nt_field_prefix(self):
        return ''

