from django.forms import ModelForm
from .models import Streak


class AddStreakForm(ModelForm):
    class Meta:
        model = Streak
        fields = ['activity',
                  'start',
                  'current_streak',
                  'longest_streak',
                  'notes'
                  ]
