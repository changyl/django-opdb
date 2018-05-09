from django.db import models
from django.urls import reverse


class Lepus(models.Model):
    name = models.CharField('全局配置KEY', max_length=50, blank=True, default='')
    value = models.CharField('值', max_length=255, blank=True, default='')
    description = models.CharField('描述', max_length=100, default='')

    class Meta:
        verbose_name = 'Lepus监控全局配置'
        verbose_name_plural = 'Lepus监控全局配置'
        db_table = "options"  # 重写数据表名称，覆盖类名
        app_label = "monitor"


    def get_absolute_url(self):
        return reverse('monitor:monitor-total-config')


class LepusMysqlConfig(models.Model):
    id = models.AutoField('ID', primary_key=True)
    host = models.CharField('主机', max_length=255, blank=True, default='')
    port = models.CharField('端口', max_length=100, default='')
    tags = models.CharField('标签', max_length=100, default='')
    monitor = models.SmallIntegerField('监控设置', max_length=1, default='0')
    display_order = models.SmallIntegerField('显示排序', max_length=1, default='0')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    is_multi_source = models.SmallIntegerField('多源复制监控设置', max_length=1, default='0')

    class Meta:
        verbose_name = 'Lepus监控Mysql配置'
        verbose_name_plural = 'Lepus监控Mysql配置'
        db_table = "db_servers_mysql"  # 重写数据表名称，覆盖类名
        app_label = "monitor"

    def get_absolute_url(self):
        return reverse('monitor:monitor-total-config')