from django.core.management.base import NoArgsCommand
from photos.photo.models import *
import os
from os.path import join
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from re import match, IGNORECASE

def decode_exif(filename):
    i = Image.open(filename)
    info = i._getexif() or {}
    ret = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def parsedate(datestr):
    if datestr:
        return datetime.strptime(datestr, '%Y:%m:%d %H:%M:%S')
    else:
        return None

def get_camera(exif):
    make = exif.get('Make', '')
    model = exif.get('Model', '')
    if make or model:
        camera, is_new = Camera.objects.get_or_create(make=make, model=model)
        return camera
    else:
        return None
    
class Command(NoArgsCommand):
    help = 'Find and index photos.'
    
    def handle_noargs(self, **options):
        base = '/home/kaj/Bilder/foto'
        for root, dirs, files in os.walk(base + '/2010'):
            #print "Current directory", root
            #print "Sub directories", dirs
            #print "Files", files
            for fn in files:
                if match('.*.jpg$', fn, IGNORECASE):
                    filename = os.path.join(root, fn)
                    try:
                        exif = decode_exif(filename)
                        date = parsedate(exif.get('DateTimeOriginal'))
                        camera = get_camera(exif)
                        #print filename, date, camera
                        photo, is_new = Photo.objects.get_or_create(
                            img = filename.replace(base, 'orig'),
                            defaults = { 'date': date, 'camera': camera })
                        if not is_new:
                            photo.date = date;
                            photo.camera = camera
                            photo.save()
                        print photo, is_new
                    except:
                        print "Failed to load %s" % filename
                        raise
