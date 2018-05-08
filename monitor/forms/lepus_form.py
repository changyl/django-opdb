from django import forms as f
from django.contrib.auth.models import User
from django.forms import ModelForm
from monitor.models.lepus_model import Lepus
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
