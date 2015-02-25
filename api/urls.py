from django.conf.urls import patterns, include, url
from rest_framework import routers
from streaks.views import StreakViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'streaks', StreakViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns(
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^streaks/$', StreakViewSet.as_view(
        {'post': 'list', 'get': 'list'}),
        name='streaks'
        )
)
