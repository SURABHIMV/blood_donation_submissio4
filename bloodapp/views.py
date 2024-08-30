from django.shortcuts import render
import sweetify
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.template import loader
from . models import *
from datetime import datetime
from django.views import View
from django.utils.decorators import method_decorator  
from django.contrib.auth.decorators import login_required 

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('base')
        else:
          sweetify.error(request, 'Enter valid username and password')     
    return render(request,"adminn/login.html")

def basee(request):  
     return render(request,"adminn/base.html")

def dashboardd(request):
    pat= Patient.objects.all().count()
    don=Donar.objects.all().count()

    print('prod',pat)
    context = {
        'patient_count':pat,
        'donar_count':don
    } 
    return render(request,"adminn/dashboard.html",context)

def patientss(request):  
     patient= Patient.objects.all()
     context={
         'data':patient
     }
     return render(request,"adminn/patients.html",context)

def donarss(request):
     don= Donar.objects.all()
     context={
         'data':don
     }
     return render(request,"adminn/donars.html",context)
def view_donarr(request):
    id = request.GET.get("id")
    context={}
    print('kkkkkkkkkkkkkkkkkkkkk',id)
    if id:
         donn = Donar.objects.get(id=id)
    
#     context['data']=data
#     print("context",context)
#     rendered_template = template.render(context, request)
#     return JsonResponse({"rendered_template":rendered_template})
    context={
         'data':donn
    }
    print("context",context)
    template = loader.get_template('adminn/donar_detail.html')
    rendered_template = template.render(context, request)
    return JsonResponse({"rendered_template":rendered_template})


def logout_admin(request):
   logout(request)
   return redirect('login') 