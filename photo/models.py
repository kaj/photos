from django.db import models
from os.path import basename

class Camera(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s %s' % (self.make, self.model)

class Photo(models.Model):
    img = models.ImageField(upload_to='orig')
    date = models.DateTimeField('orignial date')
    camera = models.ForeignKey(Camera)

    def __unicode__(self):
        return u'%s (%s)' % (self.img, self.date)
