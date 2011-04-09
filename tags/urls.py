from django.conf.urls.defaults import patterns, url
from photos.tags.views import *

urlpatterns = patterns('',
    url(r'^$', overview, name='tags'),
    url(r'^who/(?P<person>.*)$', index, name='person_index'),
    url(r'^where/(?P<place>.*)$', index, name='place_index'),
    url(r'^(?P<keyword>.*)$', index, name='tag_index'),
)
