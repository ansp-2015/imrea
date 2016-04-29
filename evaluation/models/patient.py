from django.db import models
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        names = self.name.split()
        return ''.join([n[0] for n in names if n[0].isupper()])
