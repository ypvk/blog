from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return 'articale, title: %s, content %s' % (self.title, self.content)

