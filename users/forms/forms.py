# -*- coding: utf-8 -*-

from django import forms as f
from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models.menus import menus
from users.models.group import GroupMenus
from unit.public_fun import Tools
from django.core.exceptions import ValidationError

def UsernameValidate(value):
    if value is None:
        raise ValidationError('用户名称错误')


class LoginForm(f.Form):
    username = f.CharField(label='',min_length=1,max_length=15,validators=[UsernameValidate],error_messages={'required':'用户不能为空'},widget=f.TextInput(attrs={'class': 'form-control'}))
    password = f.CharField(label='',min_length=7,max_length=14,widget=f.PasswordInput(attrs={'class': 'form-control'}))


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','is_staff','is_active','is_superuser']

        min_length = {
            'username': 1,
            'first_name': 1,
            'last_name': 1,
            'email': 5,
            'is_staff':1,
            'is_active':1,
            'is_superuser':1,
        }

        max_length = {
            'username': 10,
            'first_name': 10,
            'last_name': 10,
            'email': 15,
            'is_staff':1,
            'is_active':1,
            'is_superuser':1,
        }

        widgets = {
            'username': f.TextInput(
                attrs={'class': 'form-control','required': True}),
            'first_name': f.TextInput(
                attrs={'class': 'form-control','required': True}),
            'last_name': f.TextInput(
                attrs={'class': 'form-control'}),
            'email': f.EmailInput(
                attrs={'class': 'form-control'}),
            'is_staff': f.Select(
                attrs={'class': 'form-control'}),
            'is_active': f.Select(
                attrs={'class': 'form-control'}),
            'is_superuser': f.Select(
                attrs={'class': 'form-control'}),
        }



class GroupForm(f.Form):

    groupname = f.CharField(label=u'组名称',min_length=1,widget=f.TextInput(attrs={'class':'form-control','style':'width: 370px'}))

    groupbak = f.CharField(label=u'备注',required=False,min_length=0,widget=f.Textarea(attrs={'class': 'form-control','style':'width:380px;height: 50px'}))

    menu = Tools.get_menus()
    tuple_menus = (x for x in menu)
    menus = f.MultipleChoiceField(widget=f.SelectMultiple(attrs={'id':'menus-public-methods','multiple':'multiple'}),
                          choices=tuple_menus,label=u'用户清单')

    user = Tools.get_users()
    tuple_users = (x for x in user)
    users = f.MultipleChoiceField(widget=f.SelectMultiple(attrs={'id': 'users-public-methods', 'multiple': 'multiple'}),
                          choices=tuple_users, label=u'用户清单')




class MenusForm(ModelForm):
    class Meta:
        module = GroupMenus
        fields = ['menus_id','user_id']