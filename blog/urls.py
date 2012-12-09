from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = patterns('blog.views',
        url(r'^users/$', views.UserList.as_view(), name="users"),
        url(r'^users/(?P<username>.+)/$', views.UserItem.as_view(), name="user"),
        url(r'^users/new/$', views.UserList.new, name="user_new"),
        url(r'^users/(?P<username>.+)/edit/$', views.UserItem.edit, name="user_edit"),

        url(r'^articles/$', views.ArticleList.as_view(), name="articles"),
        url(r'^articles/(?P<slug>.+)/$', views.ArticleItem.as_view(), name='article'),
        url(r'^articles/new/$', views.ArticleList.new, name='article_new'),
        url(r'^articles/(?P<slug>.+)/edit/$', views.ArticleItem.edit, name='article_edit'),
        )

urlpatterns = format_suffix_patterns(urlpatterns)
