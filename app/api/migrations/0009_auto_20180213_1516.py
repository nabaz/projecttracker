# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20180213_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='creator',
            new_name='creator_id',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='creator',
            new_name='creator_id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='creator',
            new_name='creator_id',
        ),
        migrations.RenameField(
            model_name='timeentry',
            old_name='creator',
            new_name='creator_id',
        ),
    ]
