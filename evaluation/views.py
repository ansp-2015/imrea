# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

from .models.patient import Patient
from .models.period import Period

from .models import BostonAphasia, FIM, KVIQ, SIS, Clin, HAD, FuglMeyer

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
    evaluated_periods = patient.find_evaluated_period()
    evaluated_periods_array = []
    for e in evaluated_periods:
        evaluated_periods_array.append({"id": e.pk, "period": e.period})

    not_evaluated_periods = patient.find_not_evaluated_period()
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

    bostonAphasia = BostonAphasia.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()
    fim = FIM.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()
    fuglmeyer = FuglMeyer.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()
    had = HAD.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()
    kviq = KVIQ.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()
    sis = SIS.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()
    clin = Clin.objects.filter(patient_id=patient_id).filter(period_id=period_id).first()

    evaluation_objects = []
    evaluation_objects.append(['bostonaphasia', BostonAphasia._meta.verbose_name.title(), bostonAphasia])
    evaluation_objects.append(['fim', FIM._meta.verbose_name.title(), fim])
    evaluation_objects.append(['fuglmeyer', FuglMeyer._meta.verbose_name.title(), fuglmeyer])
    evaluation_objects.append(['had', HAD._meta.verbose_name.title(), had])
    evaluation_objects.append(['kviq', KVIQ._meta.verbose_name.title(), kviq])
    evaluation_objects.append(['sis',SIS._meta.verbose_name.title(), sis])
    evaluation_objects.append(['clin', Clin._meta.verbose_name.title(), clin])

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
