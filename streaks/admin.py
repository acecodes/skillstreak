from django.contrib import admin
from .models import *


class StreakAdmin(admin.ModelAdmin):
    model = Streak
    list_display = (
        ['id', 'user', 'activity', 'start', 'current_streak', 'longest_streak'])

admin.site.register(Streak, StreakAdmin)
