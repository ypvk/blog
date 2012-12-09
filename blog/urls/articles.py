from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import articles

urlpatterns = patterns('blog.views',
        url(r'^$', articles.ArticleList.as_view(), name="articles"),
        url(r'^(?P<slug>.+)/$', articles.ArticleItem.as_view(), name='article'),
        url(r'^new/$', articles.ArticleList.new, name='article_new'),
        url(r'^(?P<slug>.+)/edit/$', articles.ArticleItem.edit, name='article_edit'),
        )
urlpatterns = format_suffix_patterns(urlpatterns)
