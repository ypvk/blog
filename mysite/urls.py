from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('blog.urls.users')),
    url(r'^articles/', include('blog.urls.articles')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html.haml'}, name='login'),
    url(r'^logout/$', 'blog.views.useraction.user_logout', name="logout"),
    url(r'^registration/$', 'blog.views.useraction.registration', name='registration'),
)
