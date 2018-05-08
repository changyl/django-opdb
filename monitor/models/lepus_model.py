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

    def get_absolute_url(self):
        return reverse('monitor:monitor-total-config')