# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def login(self):
        # send email using the self.cleaned_data dictionary
        pass