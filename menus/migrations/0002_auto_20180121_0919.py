# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-21 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='exclude',
            new_name='excludes',
        ),
    ]