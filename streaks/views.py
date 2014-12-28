from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

class IndexView(generic.edit.FormView):
    template_name = 'index.html'
    form_class = LoginForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        return super(IndexView, self).form_valid(form)