# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('idc_no', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='IDC\u7f16\u53f7')),
                ('area_id', models.IntegerField(choices=[(0, '\u534e\u5317\u533a'), (1, '\u534e\u5357\u533a'), (2, '\u534e\u4e1c\u533a'), (3, '\u534e\u897f\u533a')], verbose_name='IDC\u6240\u5c5e\u533a\u57df')),
                ('idc_nm', models.CharField(max_length=45, verbose_name='IDC\u5382\u5546')),
                ('idc_tag', models.CharField(max_length=45, verbose_name='IDC\u6807\u7b7e')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('creator', models.IntegerField(max_length=4, verbose_name='\u521b\u5efa\u4eba')),
                ('remark', models.TextField(blank=True, max_length=255, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'tb_cmdb_idc',
                'verbose_name': '\u8d44\u4ea7\u7ba1\u7406-IDC',
                'verbose_name_plural': '\u8d44\u4ea7\u7ba1\u7406-IDC',
            },
        ),
    ]
