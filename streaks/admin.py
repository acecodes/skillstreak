from django.contrib import admin
from .models import *

class StreakAdmin(admin.ModelAdmin):
	model = Streak
	list_display = (['id', 'member', 'activity', 'current_streak', 'longest_streak'])

admin.site.register(Streak, StreakAdmin)
