# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='is_closed',
            field=models.BooleanField(default=False, help_text='Checks if class is closed', verbose_name='Is closed?'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Student'),
        ),
    ]
