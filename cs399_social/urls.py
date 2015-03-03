from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, about, login, activity, browse
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^about', about),
    url(r'^login', login),
    url(r'^browse', browse),
    url(r'^activity', activity),
    # url(r'^admin/', include(admin.site.urls)),
)
