from django.core.management.base import NoArgsCommand
from photos.photo.models import *
import os
from os.path import join
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

def decode_exif(filename):
    i = Image.open(filename)
    info = i._getexif()
    ret = {}
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret;

class Command(NoArgsCommand):
    help = 'Find and index photos.'
    
    def handle_noargs(self, **options):
        base = '/home/kaj/Bilder/foto'
        for root, dirs, files in os.walk(base + '/2010/02'):
            #print "Current directory", root
            #print "Sub directories", dirs
            #print "Files", files
            for fn in files:
                filename = os.path.join(root, fn)
                exif = decode_exif(filename)
                date = datetime.strptime(exif['DateTimeOriginal'],
                                         '%Y:%m:%d %H:%M:%S')
                camera, is_new = Camera.objects.get_or_create(
                    make = exif['Make'],
                    model = exif['Model'])
                print filename, date, camera
                photo, is_new = Photo.objects.get_or_create(
                    img = filename.replace(base, 'orig'),
                    defaults = { 'date': date, 'camera': camera })
                if not is_new:
                    photo.date = date;
                    photo.camera = camera
                    photo.save()
                print photo, is_new

