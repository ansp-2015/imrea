# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

from .models import Patient, BaseEvaluation

from .util import url_new_object
from .util import url_to_edit_object


def index(request):
    return HttpResponseRedirect('/login')


@login_required
def home(request):
    patients = Patient.objects.all()
    return render_to_response('admin/index.html',
        context_instance = RequestContext(request) + {'patients':patients}
    )


@login_required
def ajax_home_patient_periods(request):
    """
    AJAX para pegar os períodos de avaliações de um paciente.
    É separado em dois arrays, um com as avaliações já iniciadas/terminadas e outra com as avaliações
    ainda para serem feitas.
    :param request:
    :return:
    """

    patient_id = request.GET.get('p')
    patient = Patient.objects.get(pk=patient_id)

    # Evaluated periods
    evaluated_periods = BaseEvaluation.find_evaluated_period(patient)
    evaluated_periods_array = []
    for e in evaluated_periods:
        qty_evaluated = len(BaseEvaluation.find_evaluated_objects(patient, e))
        qty_total_evaluation = len(BaseEvaluation.__subclasses__())

        evaluated_periods_array.append({"id": e.pk, "period": e.period, "qty_evaluated": qty_evaluated, "qty_total_evaluation": qty_total_evaluation})

    not_evaluated_periods = BaseEvaluation.find_not_evaluated_period(patient)
    not_evaluated_periods_array = []
    for e in not_evaluated_periods:
        not_evaluated_periods_array.append({"id": e.pk, "period": e.period})

    data = json.dumps({
        'evaluated_periods': evaluated_periods_array,
        'not_evaluated_periods': not_evaluated_periods_array
    })

    return HttpResponse(data, content_type="application/json")


@login_required
def ajax_home_patient_evaluations(request):
    """
    AJAX para pegar as avaliações de um paciente por período.
    Utilizado na home para montar o panel das avaliações do paciente.
    :param request:
    :return:
    """
    patient_id = request.GET.get('p')
    period_id = request.GET.get('period')

    # Gets all evaluation objects (instances from subclasses of BaseEvaluation) for the given patient and period
    # that can be edit by the current user
    evaluation_objects = [(c.__name__.lower(), c._meta.verbose_name.title(),
                           c.objects.filter(patient_id=patient_id, period_id=period_id).first())
                          for c in BaseEvaluation.__subclasses__()
                          if request.user.has_perm('evaluation.change_%s' % c.__name__.lower())]

    evaluated = []
    not_evaluated = []
    for obj in evaluation_objects:
        if obj[2]:
            url = url_to_edit_object(obj[0], obj[2])
            evaluated.append({'label': '%s' % obj[1], 'url': url})
        else:
            url = url_new_object(obj[0])
            url = "%s?patient=%s&period=%s" % (url, patient_id, period_id)
            not_evaluated.append({'label': '%s' % obj[1], 'url': url})

    data = json.dumps({
        'evaluated': evaluated,
        'not_evaluated': not_evaluated
    })

    return HttpResponse(data, content_type="application/json")
