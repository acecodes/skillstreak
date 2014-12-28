from django.db import models
from django.conf import settings
import pytz

class Member(models.Model):
	TIME_ZONES = [(x, x) for x in pytz.all_timezones]
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=258)
	time_zone = models.CharField(choices=TIME_ZONES, max_length=20, default='US/Pacific')

	def __str__(self):
		return '{first_name} {last_name}'.format(
			first_name=self.first_name,
			last_name=self.last_name)

	class Meta:
		db_table = settings.TABLE_PREFIX['core'] + 'members'
		verbose_name = 'Member'