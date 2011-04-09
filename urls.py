from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^tags/', include('photos.tags.urls')),
    (r'^', include('photos.photo.urls')),
)

if settings.DEBUG and settings.MEDIA_URL[0] == '/':
    urlpatterns += patterns(
        '',
        url('^500$', direct_to_template, {'template': '500.html'}),
        url('^404$', direct_to_template, {'template': '404.html'}),
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
         'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
