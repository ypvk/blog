from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from blog.views import articles

urlpatterns = patterns('blog.views.articles',
        url(r'^$', articles.ArticleList.as_view(), name="articles"),
        url(r'^new/$', articles.ArticleNew.as_view(), name='article_new'),
        url(r'^(?P<slug>.+)/edit/$', articles.ArticleEdit.as_view(), name='article_edit'),
        url(r'^(?P<slug>.+)/$', articles.ArticleItem.as_view(), name='article'),
        )
urlpatterns = format_suffix_patterns(urlpatterns)
