from django import forms as f
from django.contrib.auth.models import User
from django.forms import ModelForm
from monitor.models.lepus_model import Lepus,LepusMysqlConfig,LepusRedis,LepusOracle
from unit.public_fun import Tools


class LepusForm(ModelForm):
    class Meta:
        model = Lepus
        fields = ['name', 'value', 'description']

        min_length = {
            'name': 1,
            'value': 1,
            'description': 90,
        }

        max_length = {
            'name': 1,
            'value': 1,
            'description': 90,
        }


class LepusMysqlForm(ModelForm):
    class Meta:
        model = LepusMysqlConfig
        fields = ['host', 'port', 'tags', 'username', 'password', 'monitor', 'display_order', 'is_multi_source']

        widgets = {
            'host': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'port': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'username': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'password': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'tags': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'monitor': f.Select(choices=(('1', '开启',), ('0', '关闭',)),
                              attrs={'class': 'form-control'}),
            'display_order': f.TextInput(
                attrs={'class': 'form-control'}),
            'is_multi_source': f.Select(choices=(('1', '开启',), ('0', '关闭',)),
                attrs={'class': 'form-control', 'rows': 5, 'required': True}),
        }

        min_length = {
            'host': 7,
            'port': 1,
            'tags': 1,
            'monitor': 2,
            'display_order': 1,
            'is_multi_source': 1,
        }

        max_length = {
            'host': 9,
            'port': 9,
            'tags': 90,
            'monitor': 90,
            'display_order': 90,
            'is_multi_source': 90,
        }


class LepusRedisForm(ModelForm):
    class Meta:
        model = LepusRedis
        fields = ['host', 'port', 'tags', 'password', 'monitor', 'display_order']

        widgets = {
            'host': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'port': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'password': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'tags': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'monitor': f.Select(choices=(('1', '开启',), ('0', '关闭',)),
                              attrs={'class': 'form-control'}),
            'display_order': f.TextInput(
                attrs={'class': 'form-control'}),
        }

        min_length = {
            'host': 7,
            'port': 1,
            'password': 8,
            'tags': 1,
            'monitor': 2,
            'display_order': 1,
        }

        max_length = {
            'host': 9,
            'port': 9,
            'password': 50,
            'tags': 90,
            'monitor': 90,
            'display_order': 90,
        }


class LepusOracleForm(ModelForm):
    class Meta:
        model = LepusOracle
        fields = ['host', 'port','dsn', 'tags','username', 'password', 'monitor', 'display_order']

        widgets = {
            'host': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'port': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'dsn': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'username': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'password': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'tags': f.TextInput(
                attrs={'class': 'form-control', 'required': True}),
            'monitor': f.Select(choices=(('1', '开启',), ('0', '关闭',)),
                              attrs={'class': 'form-control'}),
            'display_order': f.TextInput(
                attrs={'class': 'form-control'}),
        }

        min_length = {
            'host': 7,
            'port': 1,
            'dsn': 1,
            'username':1,
            'password': 8,
            'tags': 1,
            'monitor': 2,
            'display_order': 1,
        }

        max_length = {
            'host': 9,
            'port': 9,
            'password': 50,
            'tags': 90,
            'monitor': 90,
            'display_order': 90,
        }