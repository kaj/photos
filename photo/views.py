from django.views.generic.simple import direct_to_template, redirect_to
from photos.photo.models import *
from sorl.thumbnail import get_thumbnail

def index(request):
    p = Photo.objects.all()[0]
    im = get_thumbnail(p.img, '100x100')
    return direct_to_template(request, 'photo/index.html', {
            'photos': Photo.objects.all(),
            })
