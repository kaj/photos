from django.conf.urls.defaults import patterns, url
from photos.photo.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
)
