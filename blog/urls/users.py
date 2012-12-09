from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import users

urlpatterns = patterns('blog.views.users',
        url(r'^$', users.UserList.as_view(), name="users"),
        url(r'^new/$', users.UserNew.as_view(), name="user_new"),
        url(r'^(?P<username>.+)/edit/$', users.UserEdit.as_view(), name="user_edit"),
        url(r'^(?P<username>.+)/$', users.UserItem.as_view(), name="user"),
        )
urlpatterns = format_suffix_patterns(urlpatterns)
