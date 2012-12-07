from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = patterns('blog.views',
        url(r'^users/$', views.UserList.as_view()),
        url(r'^users/(?P<username>.+)/$', views.UserItem.as_view()),
        url(r'^users/new/$', views.UserList.new),
        url(r'^users/(?P<username>.+)/edit/$', views.UserItem.edit),

        url(r'^articles/$', views.ArticleList.as_view()),
        url(r'^articles/(?P<slug>.+)/$', views.ArticleItem.as_view()),
        url(r'^articles/new/$', views.ArticleList.new),
        url(r'^articles/(?P<slug>.+)/edit/$', views.ArticleItem.edit),
        )

urlpatterns = format_suffix_patterns(urlpatterns)
