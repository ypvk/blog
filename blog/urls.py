from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = patterns('',
        url(r'^users/$', views.UserList.as_view()),
        url(r'^user/(?P<username>.+)/$', views.UserItem.as_view())
        )

urlpatterns = format_suffix_patterns(urlpatterns)
