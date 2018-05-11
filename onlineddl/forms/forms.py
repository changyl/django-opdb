#/usr/bin/python
# -*- coding: utf-8 -*-


from django import forms as f
from django.forms import ModelForm
from sqlaudit.models.sql_audit import SqlAudit
from unit.public_fun import Tools




class SqlAuditForm(ModelForm):
    class Meta:
        model = SqlAudit
        fields = ['db_id', 'content', 'remarks']

        min_length = {
            'db_id': 1,
            'content': 1,
            'remarks': 1,
        }

        max_length = {
            'db_id': 1,
            #'content': 0,
            'remarks': 255,
        }

        db_tag = Tools.get_db()
        tuple_db = (x for x in db_tag)

        widgets = {
            'db_id': f.Select(choices=tuple_db,
                attrs={'class': 'form-control'}),
            'content': f.Textarea(
                attrs={'class': 'form-control'}),
            'remarks': f.Textarea(
                attrs={'class': 'form-control','rows':5, 'required': True}),
        }