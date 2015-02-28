from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

from django.utils import timezone


class Streak(models.Model):
    user = models.ForeignKey(User)
    activity = models.CharField(max_length=50)
    start = models.DateTimeField()
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    resets = models.IntegerField(default=0)
    last_reset = models.DateTimeField(null=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{member} - {activity} - {start}'.format(
            member=self.user,
            activity=self.activity,
            start=self.start.strftime('%d %b %Y'))

    def add(self):
        """Add to our current streak"""
        self.current_streak += 1
        if self.current_streak >= self.longest_streak:
            self.longest_streak = self.current_streak
        self.save()

    def subtract(self):
        """Make sure we don't go negative"""
        if self.current_streak == 0:
            self.current_streak = 0
        else:
            self.current_streak -= 1
        self.save()

    def reset_current(self):
        """Send current streak back to zero"""
        self.current_streak = 0
        self.last_reset = timezone.now()
        self.resets += 1
        self.save()

    def reset_longest(self):
        """Reset longest streak"""
        self.longest_streak = 0
        self.save()

    class Meta:
        db_table = settings.TABLE_PREFIX['relation'] + 'streaks'
        verbose_name = 'Member Streak'
        ordering = ['-start']
        unique_together = ("user", "activity")


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
