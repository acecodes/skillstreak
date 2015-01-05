from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from streaks import views

router = routers.DefaultRouter()
router.register(r'streaks', views.StreakViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    url(r'^', include('streaks.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', 
    {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^accounts/', include('allauth.urls')),
)

