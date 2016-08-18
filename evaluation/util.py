from django.core.urlresolvers import reverse
import os, sys, fnmatch, inspect
import evaluation


def url_to_edit_object(model_name, object):
    url = None
    if object:
        url = reverse('admin:evaluation_%s_change' % model_name, args=[object.id])
    return url


def url_new_object(model_name):
    url = reverse('admin:evaluation_%s_add' % model_name)
    return url


def choice_numbers(n):
    """
    Generate choice integer values for Model fields.
    :param n:
    :return: A tuple of tuples of form (i, 'i'), i ranging from 1 to n
    """
    return tuple([(i, '%s' % i) for i in range(n+1)])


def all_evaluations():
    """
    Returns all modules from evaluation models directory
    :return: A list generator with tuples (name, module)
    """
    models_path = os.path.join(os.path.dirname(evaluation.__file__), 'models')
    evals = [file for file in os.listdir(models_path) if fnmatch.fnmatch(file, '*.py')]
    evals.remove('__init__.py')
    evals.remove('base_evaluation.py')
    evals.remove('patient.py')
    evals.remove('period.py')

    for ev in evals:
        name = ev[:-3]
        exec('from .models import %s' % name)
        m = sys.modules['evaluation.models.%s' % name]
        cl = inspect.getmembers(m, inspect.isclass)
        for c in cl:
            if repr(c).find(name) > -1:
                break
        yield (name, ) + c