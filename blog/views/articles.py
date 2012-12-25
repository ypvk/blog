# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from blog.models import Article
from blog.serializers import ArticleSerializer
# form for article
from blog.forms import ArticleForm

import logging

logger = logging.getLogger(__name__)

class ArticleList(APIView):
    """
    Article List
    """
    def get(self, request, format=None):
        """
        Index GET /articles
        """
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles)
        return render_to_response('articles.html.haml',
                {'articles': serializers.object},
                context_instance=RequestContext(request))

    #@csrf_protect
    def post(self, request, format=None):
        """
        Create POST /articles
        """
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles')
        else:
            return render_to_response('article_new.html.haml',
                    {'form': form},
                    context_instance=RequestContext(request))

class ArticleItem(APIView):
    """
    for individual article
    """
    def get_article(self, slug):
        """
        get article by slug
        """
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        """
        Show GET /articles/:slug
        """
        article = self.get_article(slug)
        serializer = ArticleSerializer(article)
        return render_to_response('article.html.haml',
                {'article': serializer.object},
                context_instance=RequestContext(request))

    #@csrf_protect
    def put(self, request, slug, format=None):
        """
        Update PUT /articles/:slug
        """
        article = self.get_article(slug)
        form = ArticleForm(request.POST, instance=article)
        if form.save():
            return redirect('articles')
        else:
            return render_to_response('article_edit.html.haml',
                    {'form': form},
                    context_instance=RequestContext(request))

    def delete(self, request, slug, format=None):
        """
        Destroy DELETE /articles/:slug
        """
        return HttpResponseRedirect('/users/')

class ArticleNew(APIView):
    """
    new article
    """
    @method_decorator(login_required)
    def get(self, request, format=None):
        """
        New GET /articles/new
        """
        form = ArticleForm(instance=Article(author=request.user))
        return render_to_response('article_new.html.haml',
                {'form': form},
                context_instance=RequestContext(request))

class ArticleEdit(APIView):
    """
    edit user
    """
    def get_article(self, slug):
        """
        get article by slug
        """
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        """
        Edit GET /articles/:slug
        """
        article = self.get_article(slug)
        form = ArticleForm(instance=article)
        return render_to_response('article_edit.html.haml',
                {'form': form, 'article': article},
                context_instance=RequestContext(request))
