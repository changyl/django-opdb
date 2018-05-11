#/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms as f
from django.forms import ModelForm
from backup.models.backup_model import BackupTasks
from unit.public_fun import Tools


class BackupTasksForm(ModelForm):
    class Meta:
        model = BackupTasks
        fields = ['host_id', 'host', 'grained', 'type', 'dbname', 'tables', 'username', 'password', 'port', 'defaults_file', 'logdir', 'backupdir','level','flag']

        widgets = {
            'host_id': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'host': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'grained': f.Select(choices=(('1', '全库备份',), ('2', '单库',),('3', '单表',)),
                                attrs={'class': 'form-control'}),
            'type': f.Select(choices=(('1', '物理备份',), ('2', '逻辑备份',)),
                                attrs={'class': 'form-control'}),
            'dbname': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'tables': f.Textarea(
                attrs={'class': 'form-control', 'rows':'3', 'required': True}),
            'username': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'password': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'port': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'defaults_file': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'logdir': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'backupdir': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'level': f.Select(choices=(('1', '一般',), ('2', '紧急',),('3', '非常紧急',)),
                                attrs={'class': 'form-control'}),
            'flag': f.Select(choices=(('1', '开启',), ('0', '关闭',)),
                                attrs={'class': 'form-control'}),
        }

        min_length = {
            'host_id':1,
            'host': 7,
            'dbname':1,
            'tables':1,
            'username':1,
            'password':1,
            'port': 1,
            'defaults_file': 1,
            'logdir': 1,
            'backupdir': 8,
            'level': 1,
            'flag': 2,
        }

        max_length = {
            'host_id':20,
            'host': 30,
            'dbname':50,
            'tables':500,
            'username':50,
            'password':100,
            'port': 30,
            'defaults_file': 100,
            'logdir': 500,
            'backupdir': 500,
            'level': 10,
            'flag': 10,
        }

