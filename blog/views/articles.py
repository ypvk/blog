# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings

from django.http import Http404
from django.shortcuts import render_to_response

from blog.models import Article
from blog.serializers import ArticleSerializer

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
        return render_to_response('articles.html.haml', {'articles': serializers.object})

    def post(self, request, format=None):
        """
        Create POST /articles
        """
        return

    def new(self, request, format=None):
        """
        New GET /users/new
        """
        return
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
        return render_to_response('article.html.haml', {'article': serializer.object})

    def put(self, request, slug, format=None):
        """
        Update PUT /articles/:slug
        """
        return

    def delete(self, request, slug, format=None):
        """
        Destroy DELETE /articles/:slug
        """
        return

    def edit(self, request, slug, format=None):
        """
        Edit GET /articles/:slug/edit
        """
        return
