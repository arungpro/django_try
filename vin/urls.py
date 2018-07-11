from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', include('posts.urls')),
)
