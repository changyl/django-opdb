from django.views.generic.edit import FormView
from django.views.generic import DetailView,ListView,UpdateView,CreateView,DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from cmdb.models.db import  databases
from users.models.menus import menus
from cmdb.forms import DbForm
from django.db import connection
from unit.public_fun import Tools

decorators = [login_required]

__all__ = [
    'DbListView','DbCreateView','DbCreateView',''
]

@method_decorator(decorators,name='dispatch')
class DbListView(ListView):
    model = databases
    template_name = 'cmdb/db_list.html'

    def get_context_data(self, **kwargs):
        context = super(DbListView,self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob


@method_decorator(decorators,name='dispatch')
class DbCreateView(CreateView):
    model = databases
    form_class = DbForm
    template_name = 'cmdb/db_add.html'

    success_url = reverse_lazy('cmdb.db-add')
    success_message = 'Create user <a href="{url}">{name}</a> successfully.'


    def form_valid(self, form):
        databases = form.save(commit=False)
        databases.host = form.data['host']
        databases.user = form.data['user']
        databases.passwd = form.data['passwd']
        databases.port = form.data['port']
        databases.creator =  self.request.user.id
        databases.db_name = form.data['db_name']
        databases.flag = form.data['flag']
        databases.db_tag = form.data['db_tag']
        databases.updator = self.request.user.id
        databases.save()
        return super(DbCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DbCreateView,self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def get_success_url(self):
        return reverse('cmdb:db-add')

    def get_success_message(self, cleaned_data):
        url = reverse_lazy('cmdb:db-add')
        return self.success_message.format(
            url=url, name=self.object.idc_nm.encode("utf8")
        )




@method_decorator(decorators,name='dispatch')
class DbUpdateView(UpdateView):
    model = databases
    slug_field = 'auto_id'
    form_class = DbForm
    template_name = 'cmdb/db_update.html'

    def form_valid(self, form):
        databases = form.save(commit=False)
        databases.host = form.data['host']
        databases.user = form.data['user']
        databases.passwd = form.data['passwd']
        databases.port = form.data['port']
        databases.flag = form.data['flag']
        databases.db_name = form.data['db_name']
        databases.db_tag = form.data['db_tag']
        databases.save()
        return super(DbUpdateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DbUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def get_success_url(self):
        return reverse('cmdb:db-list')

class DbDeleteView(DeleteView):
    pass