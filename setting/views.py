# -*- coding: utf-8 -*-

from django.http.response import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic
from forms import LoginForm
from django.views.generic.edit import FormView
from models import Idc,Choice
from django.contrib.auth.views import login_required



# class LoginView(generic.ListView):
#     print '111111111'
#     template_name = 'polls/index.html'
#     context_object_name = 'idc_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Idc.objects.order_by('-create_date')[:5]



class LoginView(FormView):

    template_name = 'users/login.html'
    form_class = LoginForm

    success_url = 'wwww.baidu.com'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.login()
        return super(LoginView, self).form_valid(form)





class DetailView(generic.DetailView):
    model = Idc
    print model
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Idc
    print model
    template_name = 'polls/result.html'

def vote(request, question_id):
    question = get_object_or_404(Idc, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
