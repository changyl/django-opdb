from django.db import models
from django.urls import reverse


class BackupTasks(models.Model):
    id = models.AutoField('ID', primary_key=True)
    host_id = models.IntegerField('主机ID',)
    host = models.CharField('主机', max_length=30)
    dbname = models.CharField('DB名称', max_length=50)
    username = models.CharField('用户', max_length=45)
    password = models.CharField('密码', max_length=45)
    port = models.CharField('端口', max_length=10)
    defaults_file = models.CharField('默认文件', max_length=500)
    logdir = models.CharField('日志目录', max_length=500)
    backup_path = models.CharField('备份路径', max_length=500)
    level = models.SmallIntegerField('备份紧急级别', max_length=1)
    flag = models.SmallIntegerField('备份是否开启', max_length=1)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
