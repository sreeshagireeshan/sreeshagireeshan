from django.shortcuts import render,redirect
from siteadmin.models import *
from django.contrib import messages
from siteuser.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    user=register_tb.objects.filter(username=username,password=password)
    print(admin)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,"adminhome.html",{'data':admin})
    elif user.count()>0:
         request.session['id']=user[0].id
         return render(request,"userhome.html",{'data':user})
    else:
         messages.add_message(request,messages.INFO,"Incorrect Username or Password")
         return redirect("login")

def addhobby(request):
    return render(request,"addhobby.html")
def addhobbyAction(request):
    hobby=request.POST['hobby']
    hobby=hobbyname_tb(hobbyname=hobby)
    hobby.save()
    messages.add_message(request,messages.INFO,"Addeded Successful")
    return redirect("addhobby")
def addhobbyfactor(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,"addhobbyfactor.html",{'hobby':hobby})
def hobbyfactorAction(request):
    hobby=request.POST['hobby']
    factor=request.POST['factor']
    hobby=hobbyfactor_tb(hobbyid_id=hobby,factorname=factor)
    hobby.save()
    messages.add_message(request,messages.INFO,"added successful ")
    return redirect("addhobbyfactor")

def addseason(request):
    return render(request,"addseason.html")
def seasonAction(request):
    season=request.POST['season']
    season=season_tb(seasonname=season)
    season.save()
    messages.add_message(request,messages.INFO,"added successfully")
    return redirect("addseason")

def addseasonfactor(request):
    season=season_tb.objects.all()
    return render(request,"addseasonfactor.html",{'season':season})
def addseasonfactorAction(request):
    season=request.POST['season']
    factor=request.POST['factor']
    season=seasonfactor_tb(seasonid_id=season,factorname=factor)
    season.save()
    messages.add_message(request,messages.INFO,"added successfully")
    return redirect("addseasonfactor")
def addseasoncountryfactor(request):
    country=country_tb.objects.all()
    season=season_tb.objects.all()
    return render(request,"addseasoncountryfactor.html",{'season':season,'country':country})
def getfactorname(request):
    sid=request.GET['seasonid']
    factor=seasonfactor_tb.objects.filter(seasonid_id=sid)
    return render(request,"getfactorname.html",{'factor':factor})
def getstatename(request):
    cid=request.GET['countryid']
    state=state_tb.objects.filter(countryid_id=cid)
    return render(request,"getstatename.html",{'state':state})
def seasoncountryfactorAction(request):
    seasonid=request.POST['season']
    factorid=request.POST['factor']
    stateid=request.POST['state']
    countryid=request.POST['country']
    month=request.POST['months']
    countryfactor=seasoncountry_tb(seasonid_id=seasonid,factorid_id=factorid,stateid_id=stateid,countryid_id=countryid,month=month)
    countryfactor.save()
    messages.add_message(request,messages.INFO,"added successfully")
    return redirect("addseasoncountryfactor")

def addagefactor(request):
    return render(request,"addagefactor.html")


def addagefactorAction(request):
    minage=request.POST['minage']
    maxage=request.POST['maxage']
    factorname=request.POST['factor']
    age=agefactor_tb(minimumage=minage,maximumage=maxage,factorname=factorname)
    age.save()
    messages.add_message(request,messages.INFO,"added successfully")
    return redirect("addagefactor")
    
     
    
    
    

    

        
