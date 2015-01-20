from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress


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
            start=self.start.strftime('%d %b %Y'))

    class Meta:
        db_table = settings.TABLE_PREFIX['relation'] + 'streaks'
        verbose_name = 'Member Streak'


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __str__(self):
        return "{user}'s profile".format(user=self.user.username)

    class Meta:
        db_table = settings.TABLE_PREFIX['core'] + 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
            return False
