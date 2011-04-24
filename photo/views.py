from django.contrib.auth.decorators import login_required
from django.db.models import Count, Min
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template, redirect_to
from photos.photo.models import *
from sorl.thumbnail import get_thumbnail

@login_required
def overview(request):
    bydate = Photo.objects.extra({'odate' : 'date(date)'}).values('odate')\
        .annotate(n=Count('id'), ex=Min('id')).order_by('-odate')
    for d in bydate: 
        date = d.get('odate')
        d['photo'] = Photo.objects.get(id=d['ex'])
        if date:
            d['url'] = '/%4d/%02d/%02d/' % (date.year, date.month, date.day)
    return direct_to_template(request, 'photo/overview.html', {
            'dates': bydate,
            })

@login_required
def index(request, year=None, month=None, day=None):
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
    
    return show_index(request, photos, title)

def show_index(request, photos, title='', limit=20):
    low = int(request.GET.get('low', 0))
    high = low + limit
    count = photos.count()
    photos = photos.order_by('date')[low:high]
    return direct_to_template(request, 'photo/index.html', {
            'title': title,
            'count': count,
            'limit': limit,
            'low': low,
            'high': high,
            'prev': max(0, low - limit),
            'photos': photos,
            })

@login_required
def photo(request, id):
    photo = Photo.objects.get(id=id)
    return direct_to_template(request, 'photo/photo.html', {
            'photo': photo,
            })

@login_required
def img(request, id, size):
    photo = Photo.objects.get(id=id)
    thumbnail = get_thumbnail(photo.img, "%sx%s" % (size, size))
    return HttpResponse(thumbnail.read(), mimetype='image/jpeg')
