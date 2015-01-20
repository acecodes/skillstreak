from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Streak

from .serializers import StreakSerializer, UserSerializer
from rest_framework import viewsets, mixins


def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


class StreakViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):

    """
    API endpoint for user streaks
    """
    queryset = Streak.objects.all()
    serializer_class = StreakSerializer


class UserViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
