#/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
import uuid

class databases(models.Model):

    yn_flag=(
        (0,u'不启用'),
        (1,u'启用')
    )

    auto_id = models.AutoField(primary_key=True)
    id    =   models.CharField(u'数据库编码',default=uuid.uuid4, editable=False,max_length=255)
    host     =   models.CharField(u'IP',max_length=45)
    user  =  models.CharField(u'用户名称',max_length=45)
    passwd  =  models.CharField(u'密码',max_length=45)
    port  =  models.IntegerField(u'端口',)
    db_name = models.CharField(u'数据库名称',max_length=45)
    create_time =   models.DateTimeField(u'创建时间',auto_now_add=True )
    creator =   models.IntegerField(u'创建人ID',)
    update_time =   models.DateTimeField(u'更新时间',auto_now=True)
    updator =   models.IntegerField(u'更新人ID',)
    flag    =   models.IntegerField(u'是否启用',choices=yn_flag)
    db_tag = models.CharField(u'数据库标签',max_length=45)

    class Meta:
        verbose_name = '数据库'
        verbose_name_plural = '数据库'
        db_table = "tb_cmdb_databases"  #重写数据表名称，覆盖类名