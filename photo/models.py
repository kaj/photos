from django.db import models

class Camera(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

class Photo(models.Model):
    img = models.ImageField(upload_to='TODO')
    date = models.DateTimeField('orignial date')
    camera = models.ForeignKey(Camera)
