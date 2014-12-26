from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

class IndexView(generic.View):
    template_name = 'index.html'

    def get(self, request):
    	return render(request, self.template_name)