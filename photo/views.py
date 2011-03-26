from django.views.generic.simple import direct_to_template, redirect_to
from photos.photo.models import *
from sorl.thumbnail import get_thumbnail

def index(request, year=None, month=None, day=None):
    p = Photo.objects.all()[0]
    im = get_thumbnail(p.img, '100x100')
    if year:
        if month:
            if day:
                photos = Photo.objects.filter(
                    date__year=year, date__month=month, date__day=day)
                title = '%s-%s-%s' % (year, month, day)
            else:
                photos = Photo.objects.filter(
                    date__year=year, date__month=month)
                title = '%s-%s' % (year, month)
        else:
            photos = Photo.objects.filter(date__year=year)
            title = '%s' % (year)
    else:
        photos = Photo.objects
        title = ''

    limit = 20
    count = photos.count()
    photos = photos.all()[:limit]
    return direct_to_template(request, 'photo/index.html', {
            'title': title,
            'count': count,
            'limit': limit,
            'photos': photos,
            })
