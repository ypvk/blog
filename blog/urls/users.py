from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import users

urlpatterns = patterns('blog.views',
        url(r'^$', users.UserList.as_view(), name="users"),
        url(r'^(?P<username>.+)/$', users.UserItem.as_view(), name="user"),
        url(r'^new/$', users.UserList.new, name="user_new"),
        url(r'^(?P<username>.+)/edit/$', users.UserItem.edit, name="user_edit"),
        )
urlpatterns = format_suffix_patterns(urlpatterns)
