# -*- encoding: utf-8; -*-
from django.views.generic.simple import direct_to_template, redirect_to
from photos.tags.models import *
from photos.photo.models import *
from sorl.thumbnail import get_thumbnail
from django.db.models import Count, Min
from django.contrib.auth.decorators import login_required

@login_required
def overview(request):
    keywords = Keyword.objects.values('name').annotate(n=Count('keywordtag'))
    people = Person.objects.values('name').annotate(n=Count('persontag'))
    places = Place.objects.values('name').annotate(n=Count('placetag'))
    return direct_to_template(request, 'tags/overview.html', {
            'keywords': keywords,
            'people': people,
            'places': places,
            })

@login_required
def index(request, keyword=None, person=None, place=None):
    if keyword:
        photos = Photo.objects.filter(keywordtag__keyword__name=keyword)
        title = 'Taggat %s' % (keyword)
        
    if person:
        photos = Photo.objects.filter(persontag__person__name=person)
        title = u'på %s' % (person)

    if place:
        photos = Photo.objects.filter(placetag__place__name=place)
        title = u'från %s' % (place)

    limit = 20
    count = photos.count()
    photos = photos.order_by('date')[:limit]
    return direct_to_template(request, 'photo/index.html', {
            'title': title,
            'count': count,
            'limit': limit,
            'photos': photos,
            })
