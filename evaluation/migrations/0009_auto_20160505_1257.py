# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0008_auto_20160504_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.CharField(max_length=40)),
                ('parent', models.ForeignKey(related_name='child', verbose_name='Parent', to='evaluation.Period')),
            ],
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 5, 15, 53, 15, 474545, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eeg',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 5, 15, 56, 55, 428569, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fim',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 5, 15, 57, 14, 829551, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kviq',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 5, 15, 57, 24, 146361, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sis',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 5, 5, 15, 57, 34, 807647, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bostonaphasia',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', to='evaluation.Patient'),
        ),
        migrations.AlterField(
            model_name='eeg',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', to='evaluation.Patient'),
        ),
        migrations.AlterField(
            model_name='fim',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', to='evaluation.Patient'),
        ),
        migrations.AlterField(
            model_name='kviq',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', to='evaluation.Patient'),
        ),
        migrations.AlterField(
            model_name='sis',
            name='patient',
            field=models.ForeignKey(verbose_name='Patient', to='evaluation.Patient'),
        ),
        migrations.AddField(
            model_name='bostonaphasia',
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
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
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
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
            name='period',
            field=models.ForeignKey(default=1, verbose_name='Period', to='evaluation.Period'),
            preserve_default=False,
        ),
    ]
