# -*- coding: utf-8 -*-
from django import forms
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class ControlNTFormMixin(object):
    """
    Mixin para adicionar um atributo HTML nos campos para fazer o controle para desabilitar
    os campos que podem receber NT e serem desabilitados no caso em que o paciente não 
    possa responder ao questionário.
    Ele referencia ao campo 'imrea_nt = {'fields': ()} com a lista de campos que
    podem ser desabilitados.
    """
    def __init__(self, *args, **kwargs):
        super(ControlNTFormMixin, self).__init__(*args, **kwargs)

        if hasattr(self, 'imrea_nt'):
            print self.imrea_nt
            if 'fields' in self.imrea_nt:
                for f in self.imrea_nt['fields']:
                    self.fields[f].widget.attrs.update({
                        'imrea-nt': 'true'
                    })