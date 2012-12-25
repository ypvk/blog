from django.forms import ModelForm
from django.forms import Form
from django import forms
from django.contrib.auth.models import User
from blog.models import Article

#class UserRegisterForm(Form):
    #username = forms.CharField(label='username')
    #email = forms.EmailField(label='email')
    #password = forms.CharField(label='password', widget=forms.PasswordInput)
    #password_confirmation = forms.CharField(label='password_confirmation', widget=forms.PasswordInput)

#class UserLoginForm(Form):
    #username = forms.CharField(label='username')
    #password = forms.CharField(label='password', widget=forms.PasswordInput)

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('slug', 'author', 'title', 'preview', 'content')
