#/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from sqlaudit.views import sql_views

app_name = 'sqlaudit'

urlpatterns = [
    url(r'^sql/report/$', sql_views.SqlAuditCreateView.as_view(), name='sql-add'),
    url(r'^sql/list/$', sql_views.SqlAuditListView.as_view(), name='sql-list'),
    url(r'^sql/list/sql/$', sql_views.get_sql_list, name='sql-ajax'),
    url(r'^sql/list/history$', sql_views.auditHistoryView.as_view(), name='sql-history-list'),
    url(r'^sql/list/sql/history/ajax$', sql_views.get_sql_history_list, name='sql-ajax-history'),
    url(r'^sql/audit/pre/$', sql_views.sql_pre_audit, name='sql-pre'),
    url(r'^sql/audit/pre/result/$', sql_views.PreResultView.as_view(), name='sql-result'),
    url(r'^sql/audit/update$', sql_views.update_sql, name='sql-ajax-update'),
    url(r'^sql/audit/execute$', sql_views.sql_execute_audit, name='sql-ajax-execute'),
    url(r'^sql/audit/execute/result/$', sql_views.ExecuteResultView.as_view(), name='sql-exe-result'),
    url(r'^sql/audit/rollback$', sql_views.sql_rollback, name='sql-rollback'),
    #url(r'^idc/delete/(?P<slug>[-\w]+)/$', idc_views.IdcDeleteView.as_view(), name='idc-delete'),
]