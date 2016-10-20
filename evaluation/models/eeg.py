# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext
from . import BaseEvaluation


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/patient_<id>/eeg/<filename>
    return 'patient_{0}/eeg/{1}'.format(instance.eeg.patient.id, filename)


class Eeg(BaseEvaluation):
    eegtitle = models.CharField(_(u'Title'), max_length=250)

    class Meta:

        verbose_name = pgettext('models.Eeg', 'EEG')
        verbose_name_plural = pgettext('models.Eeg', 'EEGs')


class EegFile(models.Model):
    eeg = models.ForeignKey(Eeg, default=None)
    file = models.FileField(upload_to=user_directory_path, verbose_name=_('File'), )

    class Meta:
        verbose_name = pgettext('models.EegFile', 'EEG File')
        verbose_name_plural = pgettext('models.EegFile', 'EEG Files')