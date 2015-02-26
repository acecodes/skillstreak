from django.conf.urls import patterns, include, url
from django.contrib import admin
from streaks.views import Dashboard
from rest_framework.authtoken import views

urlpatterns = patterns('',
    url(r'^$', include('streaks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^dashboard/', Dashboard.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
