from django.conf.urls import patterns, include, url
from . import views
import pdb
# pdb.set_trace()
urlpatterns = [
    # Examples:
    # url(r'^$', 'vin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
]