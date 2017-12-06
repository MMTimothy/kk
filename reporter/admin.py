# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pictures,Place
from leaflet.admin import LeafletGeoAdmin
# Register your models here.



class PicturesAdmin(admin.ModelAdmin):
    list_display = ('image_name','image')

admin.site.register(Pictures,PicturesAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name','longitude','latitude')

admin.site.register(Place,PlaceAdmin)