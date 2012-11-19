from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

class Articale(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.TextField()
    slug = models.CharField(max_length=10)
    author = models.ForeignKey(User)
