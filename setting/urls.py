# coding:utf-8
from django.conf.urls import url,include
from django.contrib import admin

app_name = 'django_dba'

urlpatterns = [
    url(r'^$', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls.users_urls')),
    url(r'^cmdb/', include('cmdb.urls.cmdb_urls')),
    url(r'^sqlaudit/', include('sqlaudit.urls.sql_audit_urls')),
    url(r'^onlineddl/', include('onlineddl.urls.sql_audit_urls')),
    url(r'^monitor/', include('monitor.urls.lepus_url')),
]
