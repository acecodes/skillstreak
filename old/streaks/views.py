from django.shortcuts import render, render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext

from .models import Streak
from .serializers import StreakSerializer, UserSerializer
from .forms import AddStreakForm

from rest_framework import viewsets, mixins, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated


def index(request):
    return render(request, 'index.html')


class Dashboard(generics.RetrieveUpdateDestroyAPIView):
    """
    View that first greets a member after login
    """
    permission_classes = (IsAuthenticated,)
    queryset = Streak.objects.all()

    def get(self, request):
        addform = AddStreakForm()
        context_instance = RequestContext(request)
        template = 'dashboard.html'
        streaks = Streak.objects.filter(user=request.user)
        return render_to_response(template,
                                  {'streaks': streaks,
                                   'addform': addform},
                                  context_instance)


class StreakViewSet(viewsets.ModelViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):

    """
    View your current streaks.
    """
    queryset = Streak.objects.all()
    serializer_class = StreakSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Streak.objects.all()
        else:
            return Streak.objects.filter(id=self.request.user.id)


class UserViewSet(viewsets.ModelViewSet):

    """
    Check out your own user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Return only results relevant to current user
        """
        user = self.request.user
        return User.objects.filter(id=user.id)
