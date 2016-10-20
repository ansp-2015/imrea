# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0009_auto_20160819_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoCA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('obs', models.TextField(max_length=500, null=True, blank=True)),
                ('alternate_trail', models.PositiveIntegerField(verbose_name='Alternating trail making', validators=[django.core.validators.MaxValueValidator(1)])),
                ('cube', models.PositiveIntegerField(verbose_name='Cube', validators=[django.core.validators.MaxValueValidator(1)])),
                ('clock_contour', models.PositiveIntegerField(verbose_name='Contour', validators=[django.core.validators.MaxValueValidator(1)])),
                ('clock_numbers', models.PositiveIntegerField(verbose_name='Numbers', validators=[django.core.validators.MaxValueValidator(1)])),
                ('clock_hands', models.PositiveIntegerField(verbose_name='Hands', validators=[django.core.validators.MaxValueValidator(1)])),
                ('naming_lion', models.PositiveIntegerField(verbose_name='Lion', validators=[django.core.validators.MaxValueValidator(1)])),
                ('naming_rhino', models.PositiveIntegerField(verbose_name='Rhino', validators=[django.core.validators.MaxValueValidator(1)])),
                ('naming_camel', models.PositiveIntegerField(verbose_name='Camel', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_face_1', models.PositiveIntegerField(verbose_name='Face', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_velvet_1', models.PositiveIntegerField(verbose_name='Velvet', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_church_1', models.PositiveIntegerField(verbose_name='Church', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_daisy_1', models.PositiveIntegerField(verbose_name='Daisy', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_red_1', models.PositiveIntegerField(verbose_name='Red', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_face_2', models.PositiveIntegerField(verbose_name='Face', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_velvet_2', models.PositiveIntegerField(verbose_name='Velvet', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_church_2', models.PositiveIntegerField(verbose_name='Church', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_daisy_2', models.PositiveIntegerField(verbose_name='Daisy', validators=[django.core.validators.MaxValueValidator(1)])),
                ('memory_red_2', models.PositiveIntegerField(verbose_name='Red', validators=[django.core.validators.MaxValueValidator(1)])),
                ('forward_digit_span', models.PositiveIntegerField(verbose_name='Forward digit span', validators=[django.core.validators.MaxValueValidator(1)])),
                ('backward_digit_span', models.PositiveIntegerField(verbose_name='Backward digit span', validators=[django.core.validators.MaxValueValidator(1)])),
                ('vigilance', models.PositiveIntegerField(verbose_name='Vigilance', validators=[django.core.validators.MaxValueValidator(1)])),
                ('serial_7s_93', models.PositiveIntegerField(verbose_name='93', validators=[django.core.validators.MaxValueValidator(1)])),
                ('serial_7s_86', models.PositiveIntegerField(verbose_name='86', validators=[django.core.validators.MaxValueValidator(1)])),
                ('serial_7s_79', models.PositiveIntegerField(verbose_name='79', validators=[django.core.validators.MaxValueValidator(1)])),
                ('serial_7s_72', models.PositiveIntegerField(verbose_name='72', validators=[django.core.validators.MaxValueValidator(1)])),
                ('serial_7s_65', models.PositiveIntegerField(verbose_name='65', validators=[django.core.validators.MaxValueValidator(1)])),
                ('repeat_1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1)])),
                ('repeat_2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1)])),
                ('verbal_fluency', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1)])),
                ('abstraction_1', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1)])),
                ('abstraction_2', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_face_no_cue', models.PositiveIntegerField(verbose_name='Face', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_velvet_no_cue', models.PositiveIntegerField(verbose_name='Velvet', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_church_no_cue', models.PositiveIntegerField(verbose_name='Church', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_daisy_no_cue', models.PositiveIntegerField(verbose_name='Daisy', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_red_no_cue', models.PositiveIntegerField(verbose_name='Red', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_face_category', models.PositiveIntegerField(verbose_name='Face', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_velvet_category', models.PositiveIntegerField(verbose_name='Velvet', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_church_category', models.PositiveIntegerField(verbose_name='Church', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_daisy_category', models.PositiveIntegerField(verbose_name='Daisy', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_red_category', models.PositiveIntegerField(verbose_name='Red', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_face_multiple_choice', models.PositiveIntegerField(verbose_name='Face', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_velvet_multiple_choice', models.PositiveIntegerField(verbose_name='Velvet', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_church_multiple_choice', models.PositiveIntegerField(verbose_name='Church', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_daisy_multiple_choice', models.PositiveIntegerField(verbose_name='Daisy', validators=[django.core.validators.MaxValueValidator(1)])),
                ('late_memory_red_multiple_choice', models.PositiveIntegerField(verbose_name='Red', validators=[django.core.validators.MaxValueValidator(1)])),
                ('orientation_date', models.PositiveIntegerField(verbose_name='Date', validators=[django.core.validators.MaxValueValidator(1)])),
                ('orientation_month', models.PositiveIntegerField(verbose_name='Month', validators=[django.core.validators.MaxValueValidator(1)])),
                ('orientation_year', models.PositiveIntegerField(verbose_name='Year', validators=[django.core.validators.MaxValueValidator(1)])),
                ('orientation_day', models.PositiveIntegerField(verbose_name='Day', validators=[django.core.validators.MaxValueValidator(1)])),
                ('orientation_place', models.PositiveIntegerField(verbose_name='Place', validators=[django.core.validators.MaxValueValidator(1)])),
                ('orientation_city', models.PositiveIntegerField(verbose_name='City', validators=[django.core.validators.MaxValueValidator(1)])),
                ('patient', models.ForeignKey(verbose_name='Patient', to='evaluation.Patient')),
                ('period', models.ForeignKey(verbose_name='Period', to='evaluation.Period')),
            ],
            options={
                'verbose_name': 'MoCA',
                'verbose_name_plural': 'MoCA',
            },
        ),
    ]
