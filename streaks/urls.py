from django.conf.urls import patterns, url
from .views import Dashboard, StreakView

urlpatterns = patterns('streaks.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^dashboard/', Dashboard.as_view()),
                       url(r'^dashboard/streaks/([0-9])+/$', StreakView.as_view())
                       )
