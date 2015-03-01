from django.conf.urls import patterns, url
from .views import Dashboard

urlpatterns = patterns('streaks.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^dashboard/', Dashboard.as_view()),
                       )
