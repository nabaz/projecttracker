# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180213_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='creator',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeentry',
            name='creator',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
