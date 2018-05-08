# -*- coding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from django.urls import reverse,reverse_lazy
from django.contrib import auth
from django.contrib.auth.models import User
from users.models.group import Group,GroupMenus,UserGroup
from users.forms.forms import UserForm
from django.db import  connections
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views import generic
from users.forms.forms import LoginForm,GroupForm
from django.views.generic.edit import FormView
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView

#获取上下文信息
from unit.public_fun import Tools

from django.contrib.auth.views import login_required
from django.db.transaction import atomic
from django.utils.decorators import method_decorator

decorators = [login_required, atomic]
decorators_t = [atomic]


@method_decorator(decorators, name='dispatch')
class IndexView(generic.base.View):

    def get(self,*args, **kwargs):
        return render(self.request, template_name='index.html')

    def post(self,*args, **kwargs):
        pass

    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)



class LoginView(FormView,generic.View):

    template_name = 'users/login.html'
    form_class = LoginForm

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            uname = form.data['username']
            passwd = form.data['password']
            yn = auth.authenticate(username=uname, password=passwd)
            if yn is not None and yn.is_active:
                auth.login(request, yn)
                #url = self.get(request)
                #print url
                return self.form_valid(form)
            return self.form_valid(form)
        return  self.form_invalid(form)

    # def get(self,request,*args):
    #     url = self.request
    #     print url
    #     return url

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):

        return reverse('users:index')


@method_decorator(decorators, name='dispatch')
class LogoutView(generic.base.RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'users:login'

    def get_redirect_url(self, *args, **kwargs):
        auth.logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)


@method_decorator(decorators,name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

    def get_context_data(self, **kwargs):
        con = super(UserListView,self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=con)
        return ob


@method_decorator(decorators,name='dispatch')
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_add.html'

    def form_valid(self, form):
        User = form.save(commit=False)
        User.username = form.data['username']
        User.first_name = form.data['first_name']
        User.last_name = form.data['last_name']
        User.email = form.data['email']
        User.is_staff = form.data['is_staff']
        User.is_active = form.data['is_active']
        User.save()
        return super(UserCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserCreateView,self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=context)
        return ob

    def get_success_url(self):
        return reverse('users:user-add')

    def get_success_message(self, cleaned_data):
        url = reverse_lazy('users:user-add')
        return self.success_message.format(
            url=url, name=self.object.username.encode("utf8")
        )


@method_decorator(decorators,name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    slug_field = 'id'
    template_name = 'users/user_update.html'

    def form_valid(self, form):
        return super(UserUpdateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        con = super(UserUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_success_url(self):
        return reverse('users:user-list')


@method_decorator(decorators,name='dispatch')
class GroupListView(ListView):
    #model = Group
    template_name = 'users/group_list.html'

    def get_queryset(self):
        sql = '''SELECT 
                g.id,
                g.name,
                g.bak,
                g.create_date,
                n.username,
                GROUP_CONCAT(m.username),
                gm.menus_id
            FROM
                auth_group g
                    LEFT JOIN
                auth_user_groups ug ON g.id = ug.group_id
                    left join
                auth_user  m ON ug.user_id = m.id 
                left join 
                auth_user  n ON g.creator = n.id 
                left join 
                tb_group_menus  gm ON gm.group_id = ug.group_id
            GROUP BY ug.group_id'''
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        return res




    def get_context_data(self, **kwargs):
        con = super(GroupListView,self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request,context=con)
        return ob


class GroupDetailView(DetailView):
    model = Group
    slug_field = 'id'
    context_object_name = 'list'
    template_name = 'users/group_detail.html'


    def get_context_data(self, **kwargs):
        con = super(GroupDetailView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob


@method_decorator(decorators,name='dispatch')
class GroupCreateView(FormView):
    model = Group
    form_class = GroupForm
    template_name = 'users/group_add.html'

    def get_context_data(self,**kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=context)
        return ob

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.data['groupname']
            menus = form.cleaned_data['menus']
            users = form.cleaned_data['users']
            groupbak = form.cleaned_data['groupbak']

            gp = Group(name=name,bak=groupbak,creator=self.request.user.id)
            gp.save()

            sql = '''select id from auth_group where name='%s' ''' % (name)
            cursor = connections['default'].cursor()
            cursor.execute(sql)
            id = cursor.fetchone()
            gmnus = GroupMenus(group_id=id[0],menus_id=','.join(menus))
            gmnus.save()

            for i in users:
                ugroup = UserGroup(group_id=id[0],user_id=i )
                ugroup.save()
            return self.form_valid(form)
        return self.form_invalid(form)

    # def form_valid(self, form):
    #     return super(GroupCreateView, self).form_valid(form)


    def get_success_url(self):
        return reverse('users:group-add')

    # def get_success_message(self, cleaned_data):
    #     url = reverse_lazy('users:group-add')
    #     return self.success_message.format(
    #         url=url, name=self.object.name.encode("utf8")
    #     )


@method_decorator(decorators,name='dispatch')
class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    slug_field = 'id'
    template_name = 'users/group_add.html'

    def form_valid(self, form):

        return super(GroupUpdateView,self).form_valid(form)

    def get_context_data(self, **kwargs):
        con = super(GroupUpdateView, self).get_context_data(**kwargs)
        ob = Tools.get_content(request=self.request, context=con)
        return ob

    def get_success_url(self):
        return reverse('users:group-list')
