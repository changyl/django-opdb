from django.conf.urls import url

from monitor.views import lepus_view as views

app_name = 'monitor'


urlpatterns = [
    url(r'^total/$',   views.TotalConfigListView.as_view(), name='monitor-total-config'),
    url(r'^total/update/$',   views.TotalConfigUpdateView.post, name='monitor-total-config-update'),

    url(r'^mysql/$',   views.MysqlListView.as_view(), name='monitor-mysql-db-list'),
    url(r'^mysql/add/$',   views.MysqlCreateView.as_view(), name='monitor-mysql-db-add'),
    url(r'^mysql/update/(?P<slug>[-\w]+)/$',   views.MysqlUpdateView.as_view(), name='monitor-mysql-db-update'),

    url(r'^redis/$',   views.RedisListView.as_view(), name='monitor-redis-db-list'),
    url(r'^redis/add/$',   views.RedisCreateView.as_view(), name='monitor-redis-db-add'),
    url(r'^redis/update/(?P<slug>[-\w]+)/$',   views.RedisUpdateView.as_view(), name='monitor-redis-db-update'),

    url(r'^oracle/$',   views.OracleListView.as_view(), name='monitor-oracle-db-list'),
    url(r'^oracle/add/$',   views.OracleCreateView.as_view(), name='monitor-oracle-db-add'),
    url(r'^oracle/update/(?P<slug>[-\w]+)/$',   views.OracleUpdateView.as_view(), name='monitor-oracle-db-update'),

    # url(r'^user/update/(?P<slug>[-\w]+)/$',   views.UserUpdateView.as_view(), name='user-update'),
    # url(r'^group/list/$',   views.GroupListView.as_view(), name='group-list'),
    # url(r'^group/add/$',   views.GroupCreateView.as_view(), name='group-add'),
    # url(r'^group/detail/(?P<slug>[-\w]+)/$',   views.GroupDetailView.as_view(), name='group-detail'),
    # url(r'^group/update/(?P<slug>[-\w]+)/$',   views.GroupUpdateView.as_view(), name='group-update'),
]