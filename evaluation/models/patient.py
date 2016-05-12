from django.db import models
from django.forms import extras
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):

    name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)

    def __unicode__(self):
        #names = self.name.split()
        #return ''.join([n[0] for n in names if n[0].isupper()])
        return self.name
    
    class Meta:
        ordering = ['name']

