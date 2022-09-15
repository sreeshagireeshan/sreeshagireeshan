from django.shortcuts import render,redirect
from siteuser.models import *
from django.contrib import messages
from siteadmin.models import *
import datetime
from django.http import JsonResponse

# Create your views here.
def register(request):
    countries=country_tb.objects.all()
    hobby=hobbyname_tb.objects.all()
    return render(request,"register.html",{'countries':countries,'hobby':hobby})

def getstate(request):
    cid=request.GET['country_id']
    state=state_tb.objects.filter(countryid=cid)
    return render(request,"getstate.html",{'state':state})

def registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    countryid=request.POST['country']
    stateid=request.POST['state']
    security=request.POST['security']
    answer=request.POST['answer']
    hobby=request.POST['hobby']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    register=register_tb(name=name,gender=gender,dob=dob,address=address,phone=phone,securityquestion=security,answer=answer,stateid_id=stateid,countryid_id=countryid,username=username+'@mymail.com',password=password)
    register.save()
    hobbies=request.POST.getlist('hobby')
    for hid in hobby:
        hobby=hobbyname_tb.objects.get(id=hid)
        hobby=hobby_tb(userid=register,hobbyid=hobby)
        hobby.save()
        messages.add_message(request,messages.INFO,"registration successful")
        return redirect('register')

def composemessage(request):
    return render(request,"composemessage.html")
def composemessageAction(request):
    senderid=request.session['id']
    receiverid=request.POST['receiverid']
    rec=register_tb.objects.get(username=receiverid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    compose=message_tb(senderid_id=senderid,receiverid=rec,subject=subject,message=message,date=date,time=time)
    compose.save()
    messages.add_message(request,messages.INFO,"added successful ")
    return redirect("composemessage")
def checkusername1(request):
    username=request.GET['receiverid']
    print(username)
    user=register_tb.objects.filter(username=username)
    print(user)
    if user.count()>0:
        msg="exist"
    else:
        msg="not exist"
    print(msg)
    return JsonResponse({'valid':msg})
def sentmessage(request):
    senderid=request.session['id']
    status=['pending','Deleted by receiver']
    sent=message_tb.objects.filter(senderid=senderid,status__in=status)
    return render(request,"sentmessage.html",{'sent':sent})
def delete(request,id):
    message=message_tb.objects.filter(id=id)
    status=message[0].status
    if status == 'Deleted by receiver':
        msg=message_tb.objects.filter(id=id).delete()
        return redirect('sentmessage')
    if status == 'pending':
        msg=message_tb.objects.filter(id=id).update(status='deleted by sender')
    return redirect("sentmessage")

def viewmessage(request):
    senderid=request.session['id']
    status=['pending','Deleted by sender']
    #view=message_tb.objects.filter(receiverid=senderid,status__in=status).exclude(id__in=trash_tb.objects.filter(receiverid=senderid).values('messageid_id'))
    agefactors=customeragefactor_tb.objects.filter(userid=senderid)
    for factor in agefactors:
        msg=message_tb.objects.filter(receiverid=senderid,filterstatus='pending',message__icontains=factor.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(userid=senderid).values('contactid')).update(filterstatus="filtered")

    hobbyfactors=customerhobbyfactor_tb.objects.filter(userid=senderid)
    for factor in hobbyfactors:
        msg=message_tb.objects.filter(receiverid=senderid,filterstatus='pending',message__icontains=factor.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(userid=senderid).values('contactid')).update(filterstatus="filtered")
    seasoncountryfactor=customerseasoncountry_tb.objects.filter(userid=senderid)
    for factor in seasoncountryfactor:
        msg=message_tb.objects.filter(receiverid=senderid,filterstatus='pending',message__icontains=factor.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(userid=senderid).values('contactid')).update(filterstatus="filtered")
    contact=contact_tb.objects.filter(userid=senderid)
    for c in contact:
        msg=message_tb.objects.filter(receiverid=senderid,filterstatus='pending',senderid=c.contactid).update(filterstatus="filtered")

        
    view=message_tb.objects.filter(receiverid=senderid,status__in=status,filterstatus="filtered").exclude(id__in=trash_tb.objects.filter(receiverid=senderid).values('messageid_id'))
    return render(request,'viewmessage.html',{'view':view})
def movecheckbox(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    checkbox=request.POST.getlist('checkbox')
    for cid in checkbox:
        cid_obj=message_tb.objects.get(id=cid)
        senderid=request.session['id']
        trash=trash_tb(messageid=cid_obj,date=date,time=time,receiverid_id=senderid)
        trash.save()
    return redirect("viewmessage")

def trash(request):
    senderid=request.session['id']
    trash=trash_tb.objects.filter(receiverid_id=senderid)
    return render(request,"trash.html",{'trash':trash})
def deletetrash(request,id):
    trash=trash_tb.objects.filter(id=id)
    message=message_tb.objects.filter(id=trash[0].messageid_id)
    status=message[0].status
    if status == 'pending':
        update=message_tb.objects.filter(id=trash[0].messageid_id).update(status="deleted by receiver")
    else:
        update1=message_tb.objects.filter(id=id).delete()

        update2=trash_tb.objects.filter(id=id).delete()
    return redirect('trash')
def forward(request,id):
    message=message_tb.objects.filter(id=id)
    return render(request,"forward.html",{'forward':message})

def forwardAction(request):
    receiver=request.POST['receiverid']
    rec=register_tb.objects.get(username=receiver)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    senderid=request.session['id']
    time=datetime.datetime.now().strftime("%H:%M")
    forwardmessage=message_tb(senderid_id=senderid,receiverid=rec,subject=subject,message=message,date=date,time=time)
    forwardmessage.save()
    
    messages.add_message(request,messages.INFO,"Message forwarded")
    return redirect("viewmessage")

def reply(request,id):
    message=message_tb.objects.filter(id=id)
    return render(request,"reply.html",{'reply':message})
def replyAction(request):
    receiver=request.POST['receiverid']
    rec=register_tb.objects.get(username=receiver)
    senderid=request.session['id']
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    replymessage=message_tb(senderid_id=senderid,receiverid=rec,subject=subject,message=message,date=date,time=time)
    replymessage.save()
    messages.add_message(request,messages.INFO,"Message replied")
    return redirect("viewmessage")
def addcontact(request):
    return render(request,"addcontact.html")
def addcontactAction(request):
    senderid=request.session['id']
    #senderid_obj=register_tb.objects.get(id=id)
    username=request.POST['username']
    print(username)
    username_obj=register_tb.objects.get(username=username)
    print(username_obj)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    contact=contact_tb(name=name,date=date,time=time,remarks=remarks,contactid=username_obj,userid_id=senderid)
    contact.save()
    messages.add_message(request,messages.INFO,"contact addedd")
    return redirect("addcontact")
def addblacklist(request):
    return render(request,"addblacklist.html")
def addblacklistAction(request):
    senderid=request.session['id']
    username=request.POST['username']
    username_obj=register_tb.objects.get(username=username)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    contact=blacklist_tb(name=name,date=date,time=time,remarks=remarks,contactid=username_obj,userid_id=senderid)
    contact.save()
    messages.add_message(request,messages.INFO,"contact addedd to blacklist")
    return redirect("addblacklist")

def viewaddedcontacts(request):
    senderid=request.session['id']
    contact=contact_tb.objects.filter(userid=senderid)
    return render(request,"viewcontact.html",{'data':contact})
def deleteContact(request,id):
    cotact=contact_tb.objects.filter(id=id).delete()
    return redirect('viewaddedcontacts')
def viewblacklist(request):
    senderid=request.session['id']
    blacklist=blacklist_tb.objects.filter(userid=senderid)
    return render(request,'viewblacklist.html',{'data':blacklist})
def deleteblacklist(request,id):
    blacklist=blacklist_tb.objects.filter(id=id).delete()
    return redirect('viewblacklist')
def addtoblacklist(request,id):
    senderid=request.session['id']
    contact=contact_tb.objects.filter(id=id)
    print(contact)
    contactid=contact[0].contactid
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    remarks=contact[0].remarks
    name=contact[0].name
    blacklist=blacklist_tb(name=name,userid_id=senderid,contactid=contactid,date=date,time=time,remarks=remarks)
    blacklist.save()
    contact.delete()
    return redirect('viewaddedcontacts')
def customerhobbyfactor(request):
    senderid=request.session['id']
    hobby=hobby_tb.objects.filter(userid=senderid)
    return render(request,"customerhobbyfactor.html",{'data':hobby})
def gethobbyfactorname(request):
    hobbyid=request.GET['hobbyid']
    factor=hobbyfactor_tb.objects.filter(hobbyid=hobbyid)
    print(factor)
    return render(request,"getfactorname.html",{'data':factor})

def customerhobbyfactorAction(request):
    hobbyid=request.POST['hobby']
    factorid=request.POST['factor']
    senderid=request.session['id']
    customerhobbyfactor=customerhobbyfactor_tb(hobbyid_id=hobbyid,factorid_id=factorid,userid_id=senderid)
    customerhobbyfactor.save()
    messages.add_message(request,messages.INFO,"added successful ")
    return redirect('customerhobbyfactor')

def customeragefactor(request):
    senderid=request.session['id']
    user=register_tb.objects.filter(id=senderid)
    birthdate=user[0].dob
    by=birthdate.split('-')
    byear=by[0]
    date=datetime.date.today()
    ty=date.year
    age=ty-int(byear)
    factor=agefactor_tb.objects.filter(minimumage__lte=age,maximumage__gte=age)
    
    return render(request,"customeragefactor.html",{'agefactor':factor})
    
def customeragefactorAction(request):
    senderid=request.session['id']
    factorid=request.POST['factor']
    #fac=agefactor_tb.objects.get(id=factorid)
    customeragefactor=customeragefactor_tb(userid_id=senderid,factorid_id=factorid)
    customeragefactor.save()
    print(customeragefactor)
    messages.add_message(request,messages.INFO,"added successful ")
    return redirect('customeragefactor')

def customiseseasoncountryfactor(request):
    senderid=request.session['id']
    user=register_tb.objects.filter(id=senderid)
    countryid=user[0].countryid
    stateid=user[0].stateid
    date=datetime.date.today()
    month=date.month
    factor=seasoncountry_tb.objects.filter(countryid_id=countryid,stateid_id=stateid,month=month)
    return render(request,"customiseseasoncountryfactor.html",{'data':factor})
def customiseseasoncountryfactorAction(request):
    senderid=request.session['id']
    factorid=request.POST['factor']
    #fac=agefactor_tb.objects.get(id=factorid)
    customiseseasoncountry=customerseasoncountry_tb(userid_id=senderid,factorid_id=factorid)
    customiseseasoncountry.save()
    return redirect("customiseseasoncountryfactor")

def viewspam(request):
    status=['deleted by sender','pending']
    spammsg=message_tb.objects.filter(filterstatus="pending",status__in=status)
    return render(request,"viewspam.html",{'data':spammsg})
def deleteSpam(request,id):
    spam=message_tb.objects.filter(id=id)
    status=spam[0].status
    if status == 'deleted by sender':
         msg=message_tb.objects.filter(id=id).delete()
    else:
        msg=message_tb.objects.filter(id=id).update(status='Deleted by receiver')
    return redirect('viewspam')

#updateprofile
#logout

#forgotpassword

        
        
    
        


    


