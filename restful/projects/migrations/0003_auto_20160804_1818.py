# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160804_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='code',
            new_name='description',
        ),
    ]