from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class User(models.Model):
    #username = models.CharField(max_length=30, unique=True)
    #password = models.CharField(max_length=50)
    #email = models.EmailField(unique=True)
    #created_at = models.DateTimeField(auto_now=True)
    #updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    #@classmethod
    #def create(cls, username, password, email):
        #entryt_password = cls.entrypt_password(password)
        #user = cls(username=username, password=entryt_password, email=email)
        #return user

    #@classmethod
    #def entrypt_password(cls, password):
        #return hashlib.md5(password).hexdigest()

    #def __unicode__(self):
        #return 'name: %s, email: %s' % (self.username, self.email)

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

