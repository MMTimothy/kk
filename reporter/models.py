# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models;
from django.contrib.gis.db import models



class Pictures(models.Model):
    image_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/%Y/%m/%d/%H/%M/%S', blank=True)
class Worker(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    longitude = models.FloatField(max_length=250,blank=True,null=True)
    latitude = models.FloatField(max_length=250,blank=True,null=True)
    time = models.CharField(max_length=250,blank=True,null=True)

class Checkout(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    longitude = models.CharField(max_length=250,blank=True,null=True)
    latitude = models.CharField(max_length=250,blank=True,null=True)
    time = models.CharField(max_length=250,blank=True,null=True)

class Place(models.Model):
    place_name = models.CharField(max_length=250,blank=True,null=True)
    longitude = models.CharField(max_length=250,blank=True,null=True)
    latitude = models.CharField(max_length=250,blank=True,null=True)



# Create your models here.
