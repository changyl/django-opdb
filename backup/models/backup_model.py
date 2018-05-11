from django.db import models
from django.urls import reverse


class BackupTasks(models.Model):
    id = models.AutoField('ID', primary_key=True)
    host_id = models.CharField('主机ID', max_length=20, default='')
    host = models.CharField('主机', max_length=30, default='' )
    grained = models.SmallIntegerField('备份粒度', max_length=2, default='1')
    dbname = models.CharField('Schem名称', max_length=50, default='')
    tables = models.CharField('表名称', max_length=50, default='')
    username = models.CharField('用户', max_length=45, default='')
    password = models.CharField('密码', max_length=45, default='')
    port = models.CharField('端口', max_length=20, default='')
    defaults_file = models.CharField('默认文件', max_length=100, default='/etc/my.cnf')
    logdir = models.CharField('日志目录', max_length=500, default='')
    backupdir = models.CharField('备份路径', max_length=500, default='')
    type = models.SmallIntegerField('备份方式', max_length=2, default='1')
    gz = models.SmallIntegerField('压缩状态', max_length=2, default='1')
    level = models.SmallIntegerField('备份紧急级别', max_length=2,default='1')
    flag = models.SmallIntegerField('备份是否开启', max_length=2,default='0')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '备份任务'
        verbose_name_plural = '备份任务'
        db_table = "tb_backup_tasks"  # 重写数据表名称，覆盖类名
        # db_tablespace = "" 表空间名称
        app_label = "backup"

    def get_absolute_url(self):
        return reverse('sqlaudit:sql-list')
