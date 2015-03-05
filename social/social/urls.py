from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import home, about, login, browse, activity, upload

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'social.views.home', name='home'),
    url(r'^home/', 'social.views.home', name='home'),
    url(r'^activity/', 'social.views.activity', name='activity'),
    url(r'^browse/', 'social.views.browse', name='browse'),
    url(r'^about/', 'social.views.about', name='about'),
    url(r'^login/', 'social.views.login', name='login'),
    url(r'^upload/', 'social.views.upload', name='upload'),
)
