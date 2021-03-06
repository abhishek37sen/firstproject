# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-27 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_feedbackdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('course', multiselectfield.db.fields.MultiSelectField(choices=[('PY', 'PYTHON'), ('DJ', 'Django'), ('RA', 'Rest  Api')], max_length=8)),
                ('shifts', multiselectfield.db.fields.MultiSelectField(choices=[('Morning', 'Morning shift'), ('Afternoon', 'Afternoon_shift'), ('Evening', 'Evening_shift'), ('Night', 'Night_shift')], max_length=31)),
                ('start_date', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
