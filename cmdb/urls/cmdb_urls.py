# coding:utf-8
from django.conf.urls import url
from cmdb.views import idc_views,db_views

app_name = 'cmdb'

urlpatterns = [
    url(r'^idc/add/$', idc_views.IdcCreateView.as_view(), name='idc-add'),
    url(r'^idc/list/$', idc_views.IdcListView.as_view(), name='idc-list'),
    url(r'^idc/(?P<slug>[-\w]+)/$', idc_views.IdcUpdateView.as_view(), name='idc-update'),
    url(r'^idc/delete/(?P<slug>[-\w]+)/$', idc_views.IdcDeleteView.as_view(), name='idc-delete'),
    url(r'^db/add/$', db_views.DbCreateView.as_view(), name='db-add'),
    url(r'^db/list/$', db_views.DbListView.as_view(), name='db-list'),
    url(r'^db/(?P<slug>[-\w]+)/$', db_views.DbUpdateView.as_view(), name='db-update'),
    #url(r'^idc/delete/(?P<slug>[-\w]+)/$', idc_views.IdcDeleteView.as_view(), name='idc-delete'),
]