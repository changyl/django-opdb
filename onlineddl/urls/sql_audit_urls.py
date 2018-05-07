#/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from onlineddl.views import sql_alter_views

app_name = 'onlineddl'

urlpatterns = [
    url(r'^sql/alter/report/$', sql_alter_views.SqlAuditCreateView.as_view(), name='sql-alter-add'),
    url(r'^sql/alter/list/$', sql_alter_views.SqlAuditListView.as_view(), name='sql-alter-list'),
    url(r'^sql/alter/list/sql/$', sql_alter_views.get_sql_list, name='sql-alter-ajax'),
    url(r'^sql/alter/list/history$', sql_alter_views.auditHistoryView.as_view(), name='sql-alter-history-list'),
    url(r'^sql/alter/list/sql/history/ajax$', sql_alter_views.get_sql_history_list, name='sql-alter-ajax-history'),
    url(r'^sql/alter/audit/pre/$', sql_alter_views.sql_pre_audit, name='sql-alter-pre'),
    url(r'^sql/alter/audit/pre/result/$', sql_alter_views.PreResultView.as_view(), name='sql-alter-result'),
    url(r'^sql/alter/audit/update$', sql_alter_views.update_sql, name='sql-alter-ajax-update'),
    url(r'^sql/alter/audit/execute$', sql_alter_views.sql_execute_audit, name='sql-alter-ajax-execute'),
    url(r'^sql/alter/audit/execute/result/$', sql_alter_views.ExecuteResultView.as_view(), name='sql-alter-exe-result'),
    url(r'^sql/alter/audit/rollback$', sql_alter_views.sql_rollback, name='sql-alter-rollback'),
    #url(r'^idc/delete/(?P<slug>[-\w]+)/$', idc_views.IdcDeleteView.as_view(), name='idc-delete'),
]