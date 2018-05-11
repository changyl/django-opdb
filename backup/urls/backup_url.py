#/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from backup.views import backup_views as views

app_name = 'backup'

urlpatterns = [
    url(r'^tasks/list/$', views.BackupListView.as_view(), name='backup-tasks-list'),
    url(r'^tasks/add/$', views.BackupTasksCreateView.as_view(), name='backup-tasks-add'),
    url(r'^tasks/update/(?P<slug>[-\w]+)/$', views.BackupTasksUpdateView.as_view(), name='backup-tasks-update'),
    #url(r'^idc/delete/(?P<slug>[-\w]+)/$', idc_views.IdcDeleteView.as_view(), name='idc-delete'),
    #url(r'^db/add/$', db_views.DbCreateView.as_view(), name='db-add'),
    #url(r'^db/list/$', db_views.DbListView.as_view(), name='db-list'),
    #url(r'^db/(?P<slug>[-\w]+)/$', db_views.DbUpdateView.as_view(), name='db-update'),
    #url(r'^idc/delete/(?P<slug>[-\w]+)/$', idc_views.IdcDeleteView.as_view(), name='idc-delete'),
]