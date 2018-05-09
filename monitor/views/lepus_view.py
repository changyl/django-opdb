from django.shortcuts import render,get_object_or_404
from django.urls import reverse, reverse_lazy
from monitor.models import lepus_model
from django.db import  connections
from monitor.forms import lepus_form
from django.views import generic
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView

#获取上下文信息
from unit.public_fun import Tools

from django.contrib.auth.views import login_required
from django.db.transaction import atomic
from django.utils.decorators import method_decorator

decorators = [login_required, atomic]


@method_decorator(decorators, name='dispatch')
class TotalConfigCreateView(CreateView):
    model = lepus_model
    form_class = lepus_form.LepusForm
    template_name = 'monitor/monitor_total_config.html'

    def form_valid(self, form):
        return super(TotalConfigCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TotalConfigCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=context)
        return ob

    def get_success_url(self):
        return reverse('users:user-add')

    def get_success_message(self):
        url = reverse_lazy('users:user-add')
        return self.success_message.format(
            url=url, name=self.object.username.encode("utf8")
        )


@method_decorator(decorators, name='dispatch')
class MysqlListView(ListView):

    model = lepus_model.LepusMysqlConfig
    #form_class = lepus_form.LepusMysqlForm
    template_name = 'monitor/monitor_mysql_config.html'
