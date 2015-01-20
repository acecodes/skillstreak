from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('streaks.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^dashboard/$', 'dashboard',
                           name='streaks_dashboard'),
                       )
