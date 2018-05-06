# coding:utf-8
from django.conf.urls import url

from users.views import views

app_name = 'users'

urlpatterns = [

    url(r'^$',   views.IndexView.as_view(), name='index'),
    url(r'^login/$',   views.LoginView.as_view(), name='login'),
    url(r'^logout/$',   views.LogoutView.as_view(), name='logout'),
    url(r'^user/list/$',   views.UserListView.as_view(), name='user-list'),
    url(r'^user/add/$',   views.UserCreateView.as_view(), name='user-add'),
    url(r'^user/update/(?P<slug>[-\w]+)/$',   views.UserUpdateView.as_view(), name='user-update'),
    url(r'^group/list/$',   views.GroupListView.as_view(), name='group-list'),
    url(r'^group/add/$',   views.GroupCreateView.as_view(), name='group-add'),
    url(r'^group/detail/(?P<slug>[-\w]+)/$',   views.GroupDetailView.as_view(), name='group-detail'),
    url(r'^group/update/(?P<slug>[-\w]+)/$',   views.GroupUpdateView.as_view(), name='group-update'),
]



