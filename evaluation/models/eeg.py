# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from . import Patient
from . import BaseEvaluation

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/patient_<id>/<filename>
    return 'patient_{0}/eeg/{1}'.format(instance.patient.id, filename)

class Eeg(BaseEvaluation):
    eegtitle = models.CharField(_(u'Title'), max_length=250)
    eegfile = models.FileField(_(u'File '), upload_to=user_directory_path)
    

