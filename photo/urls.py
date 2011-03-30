from django.conf.urls.defaults import patterns, url
from photos.photo.views import *

urlpatterns = patterns('',
    url(r'^$', overview, name='overview'),
    url(r'^(?P<year>[0-9]{4})/$', index, name='index_year'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
        index, name='index_month'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$',
        index, name='index_day'),
    url(r'^img(?P<id>[0-9]+)', photo, name='photo'),
)
