# -*- coding: utf-8 -*-
from .base_evaluation import BaseEvaluation
from ..util import all_evaluations


__all__ = ['BaseEvaluation', 'Patient', 'Period']
for c in all_evaluations():
    __all__.append(c[1])
    exec('from evaluation.models.%s import %s' % c[:2])

from .patient import Patient
from .period import Period
