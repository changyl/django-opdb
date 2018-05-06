#/usr/bin/python
# -*- coding: utf-8 -*-

from django.views.generic import DetailView, ListView, CreateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from sqlaudit.models.sql_audit import SqlAudit
from sqlaudit.forms.forms import SqlAuditForm
from unit.public_fun import Tools
from unit.public_sql_audit import SqlAuditExecute,Inception
from django.http import HttpResponse as write
from django.db import connections
from django.shortcuts import render
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

decorators = [login_required]
__all__ = ['SqlAuditCreateView', 'SqlAuditListView', 'PreResultView', 'ExecuteResultView', 'auditHistoryView']


@method_decorator(decorators,name='dispatch')
class SqlAuditListView(ListView):
    model = SqlAudit
    template_name = 'sql_audit/sql_list.html'

    def get_context_data(self, **kwargs):
        context = super(SqlAuditListView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob


@login_required()
def get_sql_list(request):
    try:
        return write(SqlAuditExecute.sqlList(request=request))
    except Exception as e:
        return write(e)


@login_required()
def sql_pre_audit(request):
    try:
        db_name = request.POST.get('dbname',None)
        ct = request.POST.get('content',None)
        sql_id = request.POST.get('sqlid',None)
        row = SqlAuditExecute.get_db_info(db_name=db_name)
        audit_sql = Inception().preAuditExecute(user=row[1],password=row[2],host=row[0],port=row[3],dbname=row[4],content=ct)
        if request.method == "POST":
            result = Inception().inceptionQuery(audit_sql)
            flag = []
            for row in result:
                flag.append(row[2])
                rep_str = row[5]
                strs = rep_str.replace("'","\\'")
                strss = strs.replace('"', "\\'")
                Inception().insert_audit_res(row=row,strss=strss,sql_id=sql_id )
                Inception().update_audit_flag(sql_id=sql_id)
            return write(1)
        else:
            return write(0)
    except Exception as e:
        return write(e)


@login_required()
def sql_execute_audit(request):
    try:
        sid = request.POST.get('sqlid', None)
        db_name = request.POST.get('dbname', None)
        ct = request.POST.get('content', None)
        row = SqlAuditExecute.get_db_info(db_name=db_name)
        audit_sql = Inception().mosaic(user=row[1], password=row[2], host=row[0], port=row[3], dbname=row[4],
                                            content=ct, request=request)
        if request.method == "POST":
            result = Inception().execute(request=request,main_sql=audit_sql,sql_id=sid)
            return write(result)
        else:
            return write(0)
    except Exception as e:
        return write(e)


@login_required()
def update_sql(request):
    try:
        id = request.POST.get('id',None)
        sql = request.POST.get('sql',None)
        SqlAuditExecute.updateSql(sql_id=id,cont=sql)
        return write(1)
    except Exception as e:
        print (e)
        return write(0)


@method_decorator(decorators, name='dispatch')
class SqlAuditCreateView(SuccessMessageMixin, CreateView):
    model = SqlAudit
    form_class = SqlAuditForm
    template_name = 'sql_audit/sql_add.html'

    success_message = '上报SQL成功！'
    cont = ['无法上报ALTER TBALE SQL！']
    context = {}
    context['messages'] = cont

    def get_context_data(self, **kwargs):
        context = super(SqlAuditCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            sql = str.lower(str(form.cleaned_data['content']))
            if 'alter' in sql:
                form.instance.content = '无法上报alter ddl sql，请在在线变更功能中执行！'
                form.instance.creator = self.request.user.id
                return self.form_valid(form)
            else:
                form.instance.creator = self.request.user.id
                return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('sqlaudit:sql-list')

    # def get_success_message(self, cleaned_data):
    #     url = reverse_lazy('sqlaudit:sql-list')
    #     return self.success_message.format(
    #         url=url, name=''
    #     )


@method_decorator(decorators,name='dispatch')
class PreResultView(SuccessMessageMixin,ListView):
    template_name = 'sql_audit/sql_audit_result.html'

    def get_context_data(self, **kwargs):
        con = super(PreResultView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_queryset(self):
        try:
            sid = self.request.GET.get('sqlid', None)
            sql_result = SqlAuditExecute.sqlResultList(sql_id=sid)
            return sql_result
        except Exception as e:
            return write(e)


@method_decorator(decorators,name='dispatch')
class ExecuteResultView(SuccessMessageMixin,ListView):
    template_name = 'sql_audit/sql_exec_result.html'

    def get_context_data(self, **kwargs):
        con = super(ExecuteResultView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_queryset(self):
        try:
            sid = self.request.GET.get('sqlid', None)
            sql_result = SqlAuditExecute.executeResultList(sql_id=sid)
            return sql_result
        except Exception as e:
            return write(e)


@login_required()
def sql_rollback(request):
    try:
        if request.method == 'POST':
            x_id = request.POST.get('xlh', None)
            db_bak = request.POST.get('db_bak', None)
            sql_id = request.POST.get('sql_id', None)
            sql_1 = '''select tablename from {0}.$_$Inception_backup_information$_$ where opid_time={1};'''.format(
                db_bak, x_id)
            cursor = connections['data_backup'].cursor()
            cursor.execute(sql_1)
            row_1 = cursor.fetchone()
            sql_2 = '''select rollback_statement from {0}.{1} where opid_time={2};'''.format(db_bak, row_1[0], x_id)
            cursor = connections['data_backup'].cursor()
            cursor.execute(sql_2)
            row_2 = cursor.fetchall()
            SqlAuditExecute().rollback(sqlid=sql_id, content=row_2[0])
            return write(1)
        else:
            return write(0)
    except Exception as e:
        print (e)
        return write(0)


@method_decorator(decorators,name='dispatch')
class auditHistoryView(ListView):
    model = SqlAudit
    template_name = 'sql_audit/sql_history_list.html'

    def get_context_data(self, **kwargs):
        context = super(auditHistoryView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=context)
        return ob


@login_required()
def get_sql_history_list(request):
    try:
        sql = SqlAuditExecute()
        return write(sql.sqlHistoryList(request=request))
    except Exception as e:
        return write(e)



