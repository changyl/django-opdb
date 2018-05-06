#/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'组名称', max_length=50)
    bak = models.TextField(u'备注')
    create_date = models.DateTimeField(u'创建时间',auto_now_add=True)
    creator = models.IntegerField(u'创建人ID')

    class Meta:
        verbose_name = '组'
        verbose_name_plural = '组'
        db_table = "auth_group"  # 重写数据表名称，覆盖类名
        # db_tablespace = "" 表空间名称

    def __unicode__(self):
        return ('%s') % (self.id)


class GroupMenus(models.Model):
    id = models.AutoField(primary_key=True)
    menus_id = models.CharField(u'菜单ID', max_length=50)
    group_id = models.IntegerField(u'组ID')
    create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        unique_together = ('menus_id', 'group_id')
        verbose_name = '菜单与组关系'
        verbose_name_plural = '菜单与组关系'
        db_table = "tb_group_menus"  # 重写数据表名称，覆盖类名
        # db_tablespace = "" 表空间名称

    def __unicode__(self):
        return ('%s') % (self.menus_id)


class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(u'用户ID')
    group_id = models.IntegerField(u'组ID')
    #create_time = models.DateTimeField(u'创建时间',auto_now_add=True)

    class Meta:
        unique_together = ('group_id', 'user_id')
        verbose_name = '用户组'
        verbose_name_plural = '用户组'
        db_table = "tb_user_groups"  # 重写数据表名称，覆盖类名
        # db_tablespace = "" 表空间名称

    def __unicode__(self):
        return ('%s') % (self.id)