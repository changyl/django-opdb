#/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse


class SqlAudit(models.Model):
    id = models.AutoField(primary_key=True,)
    db_id = models.CharField(u'数据库ID', max_length=35, blank=True,)
    content = models.TextField(u'sql', blank=True,)
    flag = models.SmallIntegerField(u'是否审核', max_length=3, default=0,)
    audit_flag = models.SmallIntegerField('审核类别', max_length=1, default=0)
    auditor = models.IntegerField(u'审核人ID', max_length=5, default=0,)
    audit_date = models.DateTimeField(u'审核时间', auto_now=True,)
    remarks = models.CharField(u'备注', max_length=255, blank=True,)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True,)
    creator = models.IntegerField(u'创建人ID' ,max_length=5, default=0,)

    class Meta:
        verbose_name = 'SQL审核'
        verbose_name_plural = 'SQL审核'
        db_table = "tb_sql_audit"  # 重写数据表名称，覆盖类名
        # db_tablespace = "" 表空间名称
        app_label = "onlineddl"

    def __unicode__(self):
        return ('%s') % (self.id)

    def get_absolute_url(self):
        return reverse('sqlaudit:sql-list')