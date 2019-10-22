# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-23 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=200)),
                ('date', models.DateTimeField(max_length=50)),
            ],
        ),
    ]
