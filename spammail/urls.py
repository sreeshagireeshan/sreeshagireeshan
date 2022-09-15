"""spammail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteadmin import views as adminview
from siteuser import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('addhobby/',adminview.addhobby,name="addhobby"),
    path('addhobbyAction/',adminview.addhobbyAction,name="addhobbyAction"),
    path('register/',userview.register,name="register"),
    path('registerAction/',userview.registerAction,name="registerAction"),
    path('getstate/',userview.getstate,name="getstate"),
    path('addhobbyfactor/',adminview.addhobbyfactor,name="addhobbyfactor"),
    path('hobbyfactorAction/',adminview.hobbyfactorAction,name="hobbyfactorAction"),
    path('addseason/',adminview.addseason,name="addseason"),
    path('seasonAction/',adminview.seasonAction,name="seasonAction"),
    path('addseasonfactor/',adminview.addseasonfactor,name="addseasonfactor"),
    path('addseasonfactorAction/',adminview.addseasonfactorAction,name="addseasonfactorAction"),
    path('addseasoncountryfactor/',adminview.addseasoncountryfactor,name="addseasoncountryfactor"),
    path('getfactorname/',adminview.getfactorname,name="getfactorname"),
    path('getstatename/',adminview.getstatename,name="getstatename"),
    path('seasoncountryfactorAction/',adminview.seasoncountryfactorAction,name="seasoncountryfactorAction"),
    path('addagefactor/',adminview.addagefactor,name="addagefactor"),
    path('addagefactorAction/',adminview.addagefactorAction,name="addagefactorAction"),
    path('composemessage/',userview.composemessage,name="composemessage"),
    path('composemessageAction/',userview.composemessageAction,name="composemessageAction"),
    path('checkusername1/',userview.checkusername1,name="checkusername1"),
    path('sentmessage/',userview.sentmessage,name="sentmessage"),
    path('delete/<int:id>',userview.delete,name="delete"),
    path('viewmessage/',userview.viewmessage,name="viewmessage"),
    path('movecheckbox/',userview.movecheckbox,name="movecheckbox"),
    path('trash/',userview.trash,name="trash"),
    path('deletetrash/<int:id>',userview.deletetrash,name="deletetrash"),
    path('forward/<int:id>',userview.forward,name="forward"),
    path('forwardAction/',userview.forwardAction,name="forwardAction"),
    path('reply/<int:id>',userview.reply,name="reply"),
    path('replyAction/',userview.replyAction,name="replyAction"),
    path('addcontact/',userview.addcontact,name="addcontact"),
    path('addcontactAction/',userview.addcontactAction,name="addcontactAction"),
    path('addblacklist/',userview.addblacklist,name="addblacklist"),
    path('addblacklistAction/',userview.addblacklistAction,name="addblacklistAction"),
    path('viewaddedcontacts/',userview.viewaddedcontacts,name="viewaddedcontacts"),
    path('deleteContact/<int:id>',userview.deleteContact,name="deleteContact"),
    path('viewblacklist/',userview.viewblacklist,name="viewblacklist"),
    path('deleteblacklist/<int:id>',userview.deleteblacklist,name="deleteblacklist"),
    path('addtoblacklist/<int:id>',userview.addtoblacklist,name="addtoblacklist"),
    path('customerhobbyfactor/',userview.customerhobbyfactor,name="customerhobbyfactor"),
    path('gethobbyfactorname/',userview.gethobbyfactorname,name="gethobbyfactorname"),
    path('customerhobbyfactorAction/',userview.customerhobbyfactorAction,name="customerhobbyfactorAction"),
    path('customeragefactor/',userview.customeragefactor,name="customeragefactor"),
    path('customeragefactorAction/',userview.customeragefactorAction,name="customeragefactorAction"),
    path('customiseseasoncountryfactor/',userview.customiseseasoncountryfactor,name="customiseseasoncountryfactor"),
    path('customiseseasoncountryfactorAction/',userview.customiseseasoncountryfactorAction,name="customiseseasoncountryfactorAction"),
    path('viewspam/',userview.viewspam,name="viewspam"),
    path('deleteSpam/<int:id>',userview.deleteSpam,name="deleteSpam")
]
