#/usr/bin/python
# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from backup.models.backup_model import BackupTasks
from backup.forms.backup_forms import BackupTasksForm
from unit.public_fun import Tools
from tasks.task import add

decorators = [login_required]
__all__ = ['BackupListView', 'BackupTasksCreateView']


@method_decorator(decorators,name='dispatch')
class BackupListView(ListView):
    model = BackupTasks
    template_name = 'backup/backup_tasks_list.html'

    def get_context_data(self, **kwargs):
        context = super(BackupListView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob


@method_decorator(decorators, name='dispatch')
class BackupTasksCreateView(SuccessMessageMixin,CreateView):

    model = BackupTasks
    form_class = BackupTasksForm
    template_name = 'backup/backup_tasks_form.html'
    success_message = "成功! 新的备份任务添加完成！"

    def get_context_data(self, **kwargs):

        context = super(BackupTasksCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('backup:backup-tasks-list')


@method_decorator(decorators, name='dispatch')
class BackupTasksUpdateView(SuccessMessageMixin,UpdateView):
    model = BackupTasks
    form_class = BackupTasksForm
    slug_field = 'id'
    template_name = 'backup/backup_tasks_update_form.html'
    success_message = "成功! 备份任务修改完成！"

    def get_context_data(self, **kwargs):
        con = super(BackupTasksUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_success_url(self):
        return reverse('backup:backup-tasks-list')
