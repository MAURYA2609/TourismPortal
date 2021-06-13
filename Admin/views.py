from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .models import package,hotel
from django.template.context_processors import csrf 
from django.contrib import auth


def AdminHome(request) :
    if not request.user.is_authenticated :
        return redirect('/Login_App/login/')
    username=request.user.username
    if username=='admin' :
        return render(request,'AdminHome.html',None)
    else :
        return redirect('/User/Home/')

def AddPackage(request):
    if not request.user.is_authenticated :
        return redirect('/login/')
    a={}
    a.update(csrf(request))
    username=request.user.username
    if username=='admin' :
        return render(request,'AddPackage.html',a)
    else :
        return redirect('/User/Home/')

def addp(request):   
    pname=request.POST.get('pname','')
    pcity=request.POST.get('pcity','')
    pprize=request.POST.get('pprize','')
    pdur=request.POST.get('pdur','')
    pdec=request.POST.get('pdec','')
    if(request.FILES.get('pimage','')):
        pimage=request.FILES['pimage']
        if(pname is None or pcity is None or pprize is None or pimage is None) :
            msg="Fill All The Fields"
            return render(request,'AddPackage.html',{'msg':msg})
        log=package(pname=pname,pcity=pcity,pprize=pprize,pimage=pimage,pdec=pdec,pdur=pdur)
        log.save()
        msg="Successfully Uploaded."
        return render(request,'AddPackage.html',{'msg':msg})
    else:
        render(request,'AddPackage.html')
        msg="fill all the details"
        return render(request,'AddPackage.html',{'msg':msg})


def AddHotel(request):
    if not request.user.is_authenticated :
        return redirect('/login/')
    a={}
    a.update(csrf(request))
    username=request.user.username
    if username=='admin' :
        return render(request,'AddHotel.html',a)
    else :
        return redirect('/User/Home/')

def addh(request):   
    hname=request.POST.get('hname','')
    hcity=request.POST.get('hcity','')
    hprize=request.POST.get('hprize','')
    hdec=request.POST.get('hdec','')
    if(request.FILES.get('himage','')):
        himage=request.FILES['himage']
        if(hname is None or hcity is None or hprize is None or himage is None) :
            msg="Fill All The Fields"
            return render(request,'AddHotel.html',{'msg':msg})
        log=hotel(hname=hname,hcity=hcity,hprize=hprize,himage=himage,hdec=hdec)
        log.save()
        msg="Successfully Uploaded."
        return render(request,'AddHotel.html',{'msg':msg})
    else:
        render(request,'AddPackage.html')
        msg="fill all the details"
        return render(request,'AddHotel.html',{'msg':msg})


def AllHotels(request):
    if not request.user.is_authenticated :
        return redirect('login/')
    hotels=hotel.objects.all()
    username=request.user.username
    if username=='admin' :
        return render(request,'AllHotels.html',{'hotels':hotels})
    else :
        return redirect('/User/Home/')

def AllPackages(request):
    if not request.user.is_authenticated :
        return redirect('login/')
    packages=package.objects.all()
    print(packages)
    username=request.user.username
    if username=='admin' :
        return render(request,'AllPackages.html',{'packages':packages})
    else :
        return redirect('/User/Home/')
