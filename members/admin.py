from django.contrib import admin
from .models import *

class MemberAdmin(admin.ModelAdmin):
	model = Member
	list_display = (['id', 'first_name', 'last_name', 'email', 'time_zone'])

admin.site.register(Member, MemberAdmin)