# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170726_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.CharField(blank=True, help_text='Course of university or Period of school.', max_length=100, verbose_name='Course'),
        ),
    ]