from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse, reverse_lazy
from monitor.models.lepus_model import LepusRedis,Lepus,LepusOracle,LepusMysqlConfig
from monitor.forms.lepus_form import Lepus,LepusOracleForm,LepusForm,LepusMysqlForm,LepusRedisForm
from unit.public_monitor import Monitor
from django.views import generic
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin

#获取上下文信息
from unit.public_fun import Tools

from django.contrib.auth.views import login_required
from django.db.transaction import atomic
from django.utils.decorators import method_decorator

decorators = [login_required, atomic]
__all__ = ['TotalConfigListView', 'TotalConfigUpdateView', 'MysqlListView', 'RedisListView', 'OracleListView',
           'MysqlUpdateView','MysqlCreateView','RedisCreateView','OracleCreateView']


@method_decorator(decorators, name='dispatch')
class TotalConfigListView(ListView):

    template_name = 'monitor/monitor_total_config.html'

    def get_queryset(self):
        res = Monitor.get_monitor_config()
        return res

    def get_context_data(self, **kwargs):
        context = super(TotalConfigListView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=context)
        return ob


@method_decorator(decorators, name='post')
class TotalConfigUpdateView(generic.View):

    @staticmethod
    def post(request):
        total = request.POST.get('total', None)
        mysql = request.POST.get('mysql', None)
        oracle = request.POST.get('oracle', None)
        redis = request.POST.get('redis', None)
        freq = request.POST.get('freq', None)
        Monitor.up_monitor_total_config(total=total,mysql=mysql,oracle=oracle,redis=redis,freq=freq)
        return redirect('monitor:monitor-total-config')





@method_decorator(decorators, name='dispatch')
class MysqlListView(ListView):

    model = LepusMysqlConfig
    template_name = 'monitor/monitor_mysql.html'


@method_decorator(decorators, name='dispatch')
class MysqlCreateView(SuccessMessageMixin,CreateView,):

    model = LepusMysqlConfig
    form_class = LepusMysqlForm
    template_name = 'monitor/monitor_mysql_update_form.html'
    success_message = "成功! 新的MySQL信息添加成功！"

    def get_context_data(self, **kwargs):
        context = super(MysqlCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            # form.instance.content = '无法上报alter ddl sql，请在《表在线变更》功能中上报！'
            # form.instance.creator = self.request.user.id
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('monitor:monitor-mysql-db-list')


@method_decorator(decorators, name='dispatch')
class MysqlUpdateView(SuccessMessageMixin,UpdateView):

    model = LepusMysqlConfig
    form_class = LepusMysqlForm
    slug_field = 'id'
    template_name = 'monitor/monitor_mysql_update_form.html'
    success_message = "成功! Mysql信息修改成功！"

    def get_context_data(self, **kwargs):
        con = super(MysqlUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        print(ob)
        return ob

    def get_success_url(self):
        return reverse('monitor:monitor-mysql-db-list')



@method_decorator(decorators, name='dispatch')
class RedisListView(ListView):

    model = LepusRedis
    template_name = 'monitor/monitor_redis.html'


@method_decorator(decorators, name='dispatch')
class RedisCreateView(SuccessMessageMixin,CreateView,):

    model = LepusRedis
    form_class = LepusRedisForm
    template_name = 'monitor/monitor_redis_form.html'
    success_message = "成功! 新的Redis信息添加成功！"

    def get_context_data(self, **kwargs):
        context = super(RedisCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('monitor:monitor-redis-db-list')


@method_decorator(decorators, name='dispatch')
class RedisUpdateView(SuccessMessageMixin,UpdateView):
    model = LepusRedis
    form_class = LepusRedisForm
    slug_field = 'id'
    template_name = 'monitor/monitor_redis_update_form.html'
    success_message = "成功! Redis信息修改成功！"

    def get_context_data(self, **kwargs):
        con = super(RedisUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_success_url(self):
        return reverse('monitor:monitor-redis-db-list')


@method_decorator(decorators, name='dispatch')
class OracleListView(ListView):

    model = LepusOracle
    template_name = 'monitor/monitor_oracle.html'


@method_decorator(decorators, name='dispatch')
class OracleCreateView(SuccessMessageMixin,CreateView,):

    model = LepusOracle
    form_class = LepusOracleForm
    template_name = 'monitor/monitor_oracle_form.html'
    success_message = "成功! 新的Oracle信息添加成功！"

    def get_context_data(self, **kwargs):
        context = super(OracleCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('monitor:monitor-oracle-db-list')


@method_decorator(decorators, name='dispatch')
class OracleUpdateView(SuccessMessageMixin,UpdateView):
    model = LepusOracle
    form_class = LepusOracleForm
    slug_field = 'id'
    template_name = 'monitor/monitor_oracle_update_form.html'
    success_message = "成功! Oracle信息修改成功！"

    def get_context_data(self, **kwargs):
        con = super(OracleUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_success_url(self):
        return reverse('monitor:monitor-oracle-db-list')