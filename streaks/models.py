from django.db import models
from django.conf import settings

class Streak(models.Model):
	member = models.ForeignKey('members.Member')
	activity = models.CharField(max_length=50)
	start = models.DateTimeField()
	current_streak = models.IntegerField(default=0)
	longest_streak = models.IntegerField(default=0)

	def __str__(self):
		return '{member} - {activity} - {start}'.format(
			member=self.member,
			activity=self.activity,
			start= self.start.strftime('%d %b %Y'))

	class Meta:
		db_table = settings.TABLE_PREFIX['relation'] + 'streaks'
		verbose_name = 'Member Streak'

