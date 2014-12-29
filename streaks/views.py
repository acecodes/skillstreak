from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')