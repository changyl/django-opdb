# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'tb_choice'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'tb_question'},
        ),
    ]
