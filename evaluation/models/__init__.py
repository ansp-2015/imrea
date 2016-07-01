# -*- coding: utf-8 -*-
from .base_evaluation import BaseEvaluation
from .patient import Patient
from .period import Period

__all__ = ['BaseEvaluation', 'Patient', 'Period']
for c in BaseEvaluation.__subclasses__():
    cname = c.__name__
    __all__.append(cname)
    exec('from .%s import %s' % (cname.lower(), cname))

