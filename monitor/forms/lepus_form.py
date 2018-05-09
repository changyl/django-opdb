from django import forms as f
from django.contrib.auth.models import User
from django.forms import ModelForm
from monitor.models.lepus_model import Lepus,LepusMysqlConfig
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
        fields = ['id', 'host', 'port', 'tags', 'monitor', 'display_order', 'is_multi_source']

        # min_length = {
        #     'id': 1,
        #     'host': 7,
        #     'port': 1,
        #     'tags': 1,
        #     'monitor': 1,
        #     'display_order': 1,
        #     'is_multi_source': 1,
        # }
        #
        # max_length = {
        #     'id': 1,
        #     'host': 9,
        #     'port': 9,
        #     'tags': 90,
        #     'monitor': 90,
        #     'display_order': 90,
        #     'is_multi_source': 90,
        #     'create_time': 90,
        # }