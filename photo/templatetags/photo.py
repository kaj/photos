from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def img(photo, size=100):
    ratio = min(float(size) / photo.img.width, float(size) / photo.img.height)
    return '<img src="%s" width="%d" height="%d"/>' % (
        reverse('img', kwargs={'id': photo.id, 'size': size}),
        int(round(ratio * photo.img.width)),
        int(round(ratio * photo.img.height)),
        )
