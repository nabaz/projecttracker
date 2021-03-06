# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-08 21:31
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_time', models.DateTimeField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
