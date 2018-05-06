# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0004_auto_20171207_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(max_length=200, primary_key=True, serialize=False)),
                ('idc_no', models.IntegerField(max_length=11, unique=True, verbose_name='IDC\u7f16\u53f7')),
                ('idc_nm', models.CharField(max_length=45, verbose_name='IDC\u540d\u79f0')),
                ('idc_tag', models.CharField(max_length=45, verbose_name='IDC\u6807\u7b7e')),
                ('create_date', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_date', models.DateTimeField(verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('creator', models.IntegerField(max_length=4, verbose_name='\u521b\u5efa\u4eba')),
                ('remark', models.CharField(blank=True, max_length=255, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'tb_cmdb_idc',
                'verbose_name': '\u8d44\u4ea7\u7ba1\u7406-IDC',
                'verbose_name_plural': '\u8d44\u4ea7\u7ba1\u7406-IDC',
            },
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
