from django.views.generic.edit import FormView
from django.views.generic import DetailView,ListView,UpdateView,CreateView,DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from cmdb.models.idc import Idc
from users.models.menus import menus
from cmdb.forms import IdcForm
from django.db import connection
from unit.public_fun import Tools

decorators = [login_required]
__all__ = [
    'IdcCreateView','IdcListView','IdcUpdateView'
]


@method_decorator(decorators,name='dispatch')
class IdcListView(ListView):
    model = Idc
    template_name = 'cmdb/cmdb_list.html'


    def get_context_data(self, **kwargs):
        context = super(IdcListView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob



@method_decorator(decorators,name='dispatch')
class IdcUpdateView(UpdateView):

    model = Idc
    slug_field = 'id'
    form_class = IdcForm
    template_name = 'cmdb/cmdb_update.html'



    def form_valid(self, form):
        Idc = form.save(commit=False)
        Idc.idc_nm = form.data['idc_nm']
        Idc.idc_tag = form.data['idc_tag']
        Idc.area_id = form.data['area_id']
        Idc.remark = form.data['remark']
        Idc.save()
        return super(IdcUpdateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(IdcUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def get_success_url(self):
        return reverse('cmdb:idc-list')


@method_decorator(decorators,name='dispatch')
class IdcCreateView(SuccessMessageMixin,CreateView):
    model = Idc
    form_class = IdcForm
    template_name = 'cmdb/cmdb_add.html'

    #context_object_name = 'idc_list'
    success_url = reverse_lazy('cmdb.idc-add')
    success_message = 'Create user <a href="{url}">{name}</a> successfully.'


    def get_context_data(self, **kwargs):
        context = super(IdcCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def form_valid(self, form):
        Idc = form.save(commit=False)
        Idc.idc_nm = form.data['idc_nm']
        Idc.idc_tag = form.data['idc_tag']
        Idc.area_id = form.data['area_id']
        Idc.creator = self.request.user.id
        Idc.remark = form.data['remark']
        Idc.save()
        return super(IdcCreateView,self).form_valid(form)

    def get_success_url(self):
        return reverse('cmdb:idc-add')


    def get_success_message(self, cleaned_data):
        url = reverse_lazy('cmdb:idc-list')
        return self.success_message.format(
            url=url, name=self.object.idc_nm.encode("utf8")
        )



@method_decorator(decorators,name='dispatch')
class IdcDeleteView(DeleteView):
    #model = Idc
    template_name = 'cmdb/cmdb_delete.html'
