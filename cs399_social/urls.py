from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login, about, browse, activity, upload


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs399_social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', login),
    url(r'^about', about),
    url(r'^browse', browse),
    url(r'^activity', activity),
    url(r'^upload', upload),
)
