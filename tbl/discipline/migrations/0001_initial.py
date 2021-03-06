# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 23:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0009_user_is_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of discipline', max_length=100, verbose_name='Title')),
                ('course', models.CharField(help_text='Course that is ministered the discipline', max_length=100, verbose_name='Course')),
                ('description', models.TextField(help_text='Description of discipline', verbose_name='Description')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplines', related_query_name='discipline', to='accounts.Teacher')),
            ],
            options={
                'verbose_name': 'Discipline',
                'verbose_name_plural': 'Disciplines',
            },
        ),
    ]
