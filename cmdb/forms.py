# -*- coding: utf-8 -*-

from django.forms import *
from cmdb.models.idc import Idc
from cmdb.models.db import databases


class IdcForm(ModelForm):
    class Meta:
        model = Idc
        fields = ['idc_nm','area_id', 'idc_tag', 'remark']

        type = {
            'remark': Textarea,
        }

        min_length = {
            'idc_nm': 1,
            'area_id':1,
            'idc_tag':0,
            'remark':0,
        }

        max_length = {
            'area_id':1,
            'idc_nm': 15,
            'idc_tag': 15,
            'remark': 50,
        }

        widgets = {
            'idc_nm': TextInput(
                attrs={'class': 'form-control'}),
            'area_id': Select(
                attrs={'class': 'form-control'}),
            'idc_tag': TextInput(
                attrs={'class': 'form-control'}),
            'remark': TextInput(
                attrs={'class': 'form-control'}),
        }



class DbForm(ModelForm):
    class Meta:
        model = databases
        fields = ['host','user', 'passwd', 'port','db_name','flag','db_tag']


        min_length = {
            'host':9,
            'user':1,
            'passwd':5,
            'port':3,
            'db_name':1,
            'flag':1,
            'db_tag':1,

        }

        max_length = {
            'host':15,
            'user': 15,
            'flag': 1,
            'port': 50,
        }

        widgets = {
            'host': TextInput(
                attrs={'class': 'form-control'}),
            'user': TextInput(
                attrs={'class': 'form-control'}),
            'passwd': TextInput(
                attrs={'class': 'form-control'}),
            'port': TextInput(
                attrs={'class': 'form-control'}),
            'db_name': TextInput(
                attrs={'class': 'form-control'}),
            'flag': Select(
                attrs={'class': 'form-control'}),
            'db_tag': TextInput(
                attrs={'class': 'form-control'}),
        }



