# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0022_auto_20160622_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseevaluation',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='baseevaluation',
            name='period',
        ),
        migrations.AlterModelOptions(
            name='bostonaphasia',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='clin',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='eeg',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='fuglmeyer',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='kviq',
            options={'ordering': ['patient']},
        ),
        migrations.AlterModelOptions(
            name='sis',
            options={'ordering': ['patient']},
        ),
        migrations.RemoveField(
            model_name='bostonaphasia',
            name='baseevaluation_ptr',
        ),
        migrations.RemoveField(
            model_name='eeg',
            name='baseevaluation_ptr',
        ),
        migrations.RemoveField(
            model_name='fim',
            name='baseevaluation_ptr',
        ),
        migrations.RemoveField(
            model_name='kviq',
            name='baseevaluation_ptr',
        ),
        migrations.RemoveField(
            model_name='sis',
            name='baseevaluation_ptr',
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 30, 335000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clin',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 33, 945000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clin',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='clin',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clin',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eeg',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 37, 672000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eeg',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='eeg',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eeg',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fim',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 41, 270000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fim',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fim',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fim',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 44, 614000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuglmeyer',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='had',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 47, 551000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='had',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='had',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='had',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 52, 231000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='kviq',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sis',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 20, 10, 52, 231000, tzinfo=utc), verbose_name='Last update', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sis',
            name='obs',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sis',
            name='patient',
            field=models.ForeignKey(default=1, verbose_name='Patient', to='evaluation.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sis',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),



        migrations.DeleteModel(
            name='BaseEvaluation',
        ),
    ]
