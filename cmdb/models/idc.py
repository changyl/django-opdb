# -*- coding: utf-8 -*-

from django.db import models
import uuid

class Idc(models.Model):
    aid = (
        (0,u'华北区'),
        (1,u'华南区'),
        (2,u'华东区'),
        (3,u'华西区'),
    )

    id = models.AutoField(primary_key=True,max_length=11)
    idc_no = models.UUIDField(u'IDC编码',unique=True,default=uuid.uuid4, editable=False)
    area_id = models.IntegerField(u'IDC所属区域',choices=aid)
    idc_nm = models.CharField(u'IDC厂商',max_length=45,blank=False)
    idc_tag = models.CharField(u'IDC标签',max_length=45)
    create_date = models.DateTimeField(u'创建时间',auto_now_add=True)
    update_date = models.DateTimeField(u'更新时间',auto_now=True)
    creator = models.IntegerField(u'创建人',)
    remark = models.TextField(u'备注',max_length=255,blank=True)

    def __unicode__(self):
        return  "%s"  %  self.idc_nm

    @property
    def get_all_idc_infos(self):
        return self.objects.all()

    class Meta:
        verbose_name=u'资产管理-IDC'
        verbose_name_plural=u'资产管理-IDC'
        db_table = 'tb_cmdb_idc'
