from django.conf.urls import patterns, include, url
from microblog.views import home, newposts, posts, login

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangomicroblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^login/', login),
    url(r'^newposts/', newposts),
    url(r'^posts/', posts),
)
