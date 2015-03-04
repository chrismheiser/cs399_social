from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'app.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'app.views.home', name='home'),
					   url(r'^home/', 'app.views.home', name='home'),
					   url(r'^activity/', 'app.views.activity', name='activity'),
					   url(r'^browse/', 'app.views.browse', name='browse'),
					   url(r'^about/', 'app.views.about', name='about'),
					   url(r'^login/', 'app.views.login', name='login'),
					   url(r'^upload/', 'app.views.upload', name='upload'),
)
