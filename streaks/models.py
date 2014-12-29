from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Streak(models.Model):
	user = models.ForeignKey(User)
	activity = models.CharField(max_length=50)
	start = models.DateTimeField()
	current_streak = models.IntegerField(default=0)
	longest_streak = models.IntegerField(default=0)

	def __str__(self):
		return '{member} - {activity} - {start}'.format(
			member=self.user,
			activity=self.activity,
			start= self.start.strftime('%d %b %Y'))

	class Meta:
		db_table = settings.TABLE_PREFIX['relation'] + 'streaks'
		verbose_name = 'Member Streak'

