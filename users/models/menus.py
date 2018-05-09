#/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class menus(models.Model):
    id = models.IntegerField(primary_key=True)
    menu_id = models.IntegerField(u'菜单ID',)
    pid = models.IntegerField(u'父id', )
    sort = models.IntegerField(u'菜单排序', )
    flag = models.IntegerField(u'标识', )
    ch_nm = models.CharField(u'中文名称', max_length=25)
    en_nm = models.CharField(u'英文名称', max_length=25)
    url = models.CharField(u'url', max_length=255)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True )
    update_date = models.DateTimeField(u'更新时间', auto_now=True )

    class Meta:
        verbose_name = '菜单配置'
        verbose_name_plural = '菜单配置'
        db_table = "tb_menus"  # 重写数据表名称，覆盖类名
        # db_tablespace = "" 表空间名称
        app_label = "users"

    def __unicode__(self):
        return ('%s,%s,%s,%s,%s,%s,%s') % (self.id, self.menu_id, self.pid, self.sort, self.flag, self.ch_nm, self.url)





