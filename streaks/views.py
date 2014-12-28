from django.views import generic
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

class IndexView(generic.View):
    template_name = 'index.html'

    def get(self, request):
    	return render(request, self.template_name)

class MemberView(generic.View):
	template_name = 'member.html'

	def get(self, request):
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, self.template_name)