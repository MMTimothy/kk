# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Pictures,Worker,Checkout
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from datetime import datetime


# Create your views here.
class index(generic.FormView):
    def get(self,request,*args,**kwargs):



        icons = Pictures.objects.all().filter(image_name='icon')
        pictures = Pictures.objects.all().filter(image_name='logo')
        #pictures = Pictures.objects.all()
        worker = Worker.objects.all();


        context = {
            'icons':icons,
            'pictures':pictures,
            'user':request.user,
            'workers':worker
        }
        #return HttpResponse(pictures.image_name)
        return render(request, 'reporter/index.html',context)
    def post(self, request, *args, **kwargs):

        form = request.POST

        job_ids = form["job_id"]
        passwords = form["guard_password"]
        user = authenticate(username=job_ids,password=str(passwords))
        #worker = Worker.objects.create(first_name=first_names,second_name=second_names,job_id=job_ids,latitude=latitudes,longitude=longitudes)
        if user.is_authenticated():
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return HttpResponseRedirect('/reporter')

        return HttpResponse(job_ids)
class checkin(generic.FormView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is checkin")

    def post(self, request, *args, **kwargs):
        form = request.POST
        userid = form["user_id"]
        time = datetime.now()
        longit = form["user_longitude"]
        lat = form["user_latitude"]

        worker = Worker.objects.create(user_id=userid,longitude=longit,latitude=lat,time=time)
        return HttpResponse(time)

class checkout (generic.FormView):

    def get(self, request, *args, **kwargs):
        return HttpResponse("you have checked out")

    def post(self, request, *args, **kwargs):
        form = request.POST
        userid = form["user_id"]
        time = datetime.now()
        longit = form["user_longitude"]
        lat = form["latitude"]

        check_out = Checkout.objects.create(user_id=userid,longitude=longit,latitude=lat,time=time)
        return HttpResponse(longit)

class supervisor (generic.FormView):

    def get(self, request, *args, **kwargs):

        pictures = Pictures.objects.all().filter(image_name='logo')
        users = User.objects.all()
        worker_in = Worker.objects.all()
        checkouts = Checkout.objects.all()


        context = {
            'pictures':pictures,
            'users':users,
            'workers_in':worker_in,
            'checkouts':checkouts

        }



        #return HttpResponse(checkouts.user_id)
        return  render(request,'reporter/supervisor.html',context)
    def post(self, request, *args, **kwargs):

        form = request.POST
        guard_id = form["guard_id"]

        return render(request,'reporter/guardmap.html')

class guardmap (generic.FormView):
    def get(self, request, *args, **kwargs):


        return render(request, 'reporter/guardmap.html')

    def post(self, request, *args, **kwargs):

        form = request.POST
        longitude = form["longitude"]
        latitude = form["latitude"]

        context = {
            'longitude':longitude,
            'latitude':latitude

        }
        return  render(request,'reporter/guardmap.html',context)










