# -*- coding: utf-8 -*-

from django.db import models

class Idc(models.Model):
    id = models.AutoField(primary_key=True,max_length=200)
    idc_no = models.IntegerField(u'IDC编号',unique=True,)
    idc_nm = models.CharField(u'IDC名称',max_length=45,blank=False)
    idc_tag = models.CharField(u'IDC标签',max_length=45)
    create_date = models.DateTimeField(u'创建时间',)
    update_date = models.DateTimeField(u'更新时间',)
    creator = models.IntegerField(u'创建人',)
    remark = models.CharField(u'备注',max_length=255,blank=True)

    def __unicode__(self):
        return  "%s"  %  self.idc_nm

    @property
    def get_all_idc_infos(self):
        return self.objects.all()

    class Meta:
        verbose_name=u'资产管理-IDC'
        verbose_name_plural=u'资产管理-IDC'
        db_table = 'tb_cmdb_idc'



class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return  "%s"  %  self.choice_text

    class Meta:
        verbose_name='tb_choice'
        verbose_name_plural = 'tb_choice'
        db_table='tb_choice'
