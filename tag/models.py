from django.db import models

# Create your models here.
class Bulding(models.Model):
    buildingRequest = models.CharField(max_length=100)
    wheelchair = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    improvement = models.CharField(max_length=100)
    elevator = models.CharField(max_length=100)
    toilets =models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)

    def __unicode__(self):
        return self.rating

class Path(models.Model):
    smoothness = models.CharField(max_length=100)
    surface = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    slope = models.CharField(max_length=100)
    way = models.CharField(max_length=100)
    wheelchair = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    improvement = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)

    def __unicode__(self):
        return self.rating


class Other(models.Model):
    typeCrossing = models.CharField(max_length=100)
    busStop = models.CharField(max_length=100)
    barrier = models.CharField(max_length=100)
    sidewalk = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    improvement = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)

    def __unicode__(self):
        return self.rating