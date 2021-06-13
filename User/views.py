from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from Admin.models import package,hotel
from .models import pBookings,hBookings
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

def Home(request):
    return render(request,'Home.html', None)

def Packages(request):
    if not request.user.is_authenticated :
        return redirect('login/')
    packages=package.objects.all()
    return render(request,'Packages.html',{'packages':packages})

def buyPackage(request) : 
    username=request.user.username
    packagename=request.POST.get('pname','')
    log=pBookings(pname=packagename,username=username)
    log.save()
    return redirect('/User/Packages/')
       
def Hotels(request):
    if not request.user.is_authenticated :
        return redirect('login/')
    hotels=hotel.objects.all()
    return render(request,'Hotels.html',{'hotels':hotels})

def buyHotel(request) : 
    username=request.user.username
    hotelname=request.POST.get('hname','')
    log=hBookings(hname=hotelname,username=username)
    log.save()
    return redirect('/User/Hotels/')

def Bookings(request):
    Hresults=hBookings.objects.filter(username=request.user.username)
    if Hresults.exists() :
        HOTELS=[]
        for result in Hresults :
            name=result.hname
            obj=hotel.objects.get(hname=name)
            HOTELS.append(obj)
    Presults=pBookings.objects.filter(username=request.user.username)
    if Presults.exists() :
        PACKAGES=[]
        for result in Presults :
            name=result.pname
            obj=package.objects.get(pname=name)
            PACKAGES.append(obj)
    return render(request,'Bookings.html', {'hotels':HOTELS,'packages':PACKAGES})  

    