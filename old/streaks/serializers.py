from django.contrib.auth.models import User
from .models import Streak
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class StreakSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())
    activity = serializers.CharField(max_length=40)
    start = serializers.DateTimeField()
    current_streak = serializers.IntegerField(default=0)
    longest_streak = serializers.IntegerField(default=0)

    class Meta:
        model = Streak
        fields = (
            'id',
            'user',
            'activity',
            'start',
            'current_streak',
            'longest_streak',
            'resets',
            'last_reset',
            'notes',)
