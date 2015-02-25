from django.conf.urls import patterns, url

urlpatterns = patterns('streaks.views',
                       url(r'^$', 'index', name='index'),
                       )
