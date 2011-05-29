from django.core.management.base import NoArgsCommand
from django.conf import settings
from xml.dom import minidom
from photos.photo.models import Photo
from photos.tags.models import *
from os import path

def get_tag_model(model, name):
    obj, isnew = model.objects.get_or_create(name=name)
    return obj

class Command(NoArgsCommand):
    help = 'Load tags from the kphotoalbum index.'
    
    def handle_noargs(self, **options):
        source = minidom.parse(path.join(settings.PHOTO_STORAGE_BASE,
                                         'index.xml'))
        for image in source.getElementsByTagName('image'):
            file = image.getAttribute('file')
            if file.startswith('2010'):
                try:
                    photo = Photo.objects.get(img='orig/' + file)
                except Photo.DoesNotExist:
                    print "Photo", file, "does not exist."
                    continue
                
                for opt in image.getElementsByTagName('option'):
                    name = opt.getAttribute('name')
                    values = [v.getAttribute('value') for v in opt.getElementsByTagName('value')]

                    if name == 'Nyckelord':
                        for value in values:
                            KeywordTag.objects.get_or_create(
                                photo=photo,
                                keyword=get_tag_model(Keyword, value))
                        
                        print 'Image', photo, 'was tagged', values
                    
                    elif name == 'Platser':
                        for value in values:
                            PlaceTag.objects.get_or_create(
                                photo=photo,
                                place=get_tag_model(Place, value))

                    elif name == 'Personer':
                        for value in values:
                            PersonTag.objects.get_or_create(
                                photo=photo,
                                person=get_tag_model(Person, value))
            
