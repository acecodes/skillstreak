from django.conf.urls import patterns, include, url
from django.contrib import admin
from streaks.views import IndexView
from members.views import MemberView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view()),
    url(r'^dashboard/', MemberView.as_view()),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
