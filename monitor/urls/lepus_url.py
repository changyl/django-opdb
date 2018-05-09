from django.conf.urls import url

from monitor.views import lepus_view as views

app_name = 'monitor'


urlpatterns = [
    url(r'^total/config/$',   views.TotalConfigCreateView.as_view(), name='monitor-total-config'),
    url(r'^mysql/config/$',   views.MysqlListView.as_view(), name='monitor-mysql-db-list'),
    # url(r'^user/list/$',   views.UserListView.as_view(), name='user-list'),
    # url(r'^user/add/$',   views.UserCreateView.as_view(), name='user-add'),
    # url(r'^user/update/(?P<slug>[-\w]+)/$',   views.UserUpdateView.as_view(), name='user-update'),
    # url(r'^group/list/$',   views.GroupListView.as_view(), name='group-list'),
    # url(r'^group/add/$',   views.GroupCreateView.as_view(), name='group-add'),
    # url(r'^group/detail/(?P<slug>[-\w]+)/$',   views.GroupDetailView.as_view(), name='group-detail'),
    # url(r'^group/update/(?P<slug>[-\w]+)/$',   views.GroupUpdateView.as_view(), name='group-update'),
]