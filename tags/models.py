from django.db import models
from photo.models import Photo

class Tag(models.Model):
    photo = models.ForeignKey(Photo)

    class Meta:
        abstract = True

class Keyword(models.Model):
    name = models.CharField(max_length=200)

class KeywordTag(Tag):
    keyword = models.ForeignKey(Keyword)

    def __unicode__(self):
        return self.keyword.name

class Person(models.Model):
    name = models.CharField(max_length=200)

class PersonTag(Tag):
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return self.person.name

class Place(models.Model):
    name = models.CharField(max_length=200)
    # TODO actual position

class PlaceTag(Tag):
    place = models.ForeignKey(Place)

    def __unicode__(self):
        return self.place.name
