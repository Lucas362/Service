# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 03:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]