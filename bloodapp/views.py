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
from datetime import datetime
from datetime import date
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
# Create your views here.

def admin_loginn(request):
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
    don= Donar.objects.all().count()
    print('prod',pat)
    context = {
        'patient_count':pat,
        'donar_count':don
    } 
    return render(request,"adminn/dashboard.html",context)
    
def patientss(request):  
     patient= Patient.objects.all()

     z=[]
     for i in patient:
          s=i.username
         
          if s!="adminn":
              print('nnnnnnnnnnnnnnnnnnnnnnnnnnnn',i)
              z.append(i)
              
     context={
         'data':z
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
    if id:
         donn = Donar.objects.get(id=id)
    
    context={
         'data':donn
    }
    print("context",context)
    template = loader.get_template('adminn/donar_detail.html')
    rendered_template = template.render(context, request)
    return JsonResponse({"rendered_template":rendered_template})
    
def create_donar(request):
    if request.method == "POST":
            name = request.POST.get("name")
            nationality = request.POST.get("nationality")
            phone = request.POST.get("phone")
            phone=int(phone) if phone else None
            age = request.POST.get("age")
            age=int(age) if age else None
            sex = request.POST.get("sex")
            email = request.POST.get("email")
            address = request.POST.get("address")
            date_of_donation = request.POST.get("date_of_donation")
            blood_type = request.POST.get("blood_type")
            donation = request.POST.get("donation")
            donar_status = request.POST.get("donar_status")
            volume = request.POST.get("volume")
            volume=int(volume) if volume else None
            hemoglobin = request.POST.get("hemoglobin")
            hemoglobin=int(hemoglobin)  if hemoglobin else None
            weight = request.POST.get("weight")
            weight=int(weight) if weight else None
            medical_history = request.POST.get("medical_history")
            overall_health = request.POST.get("overall_health")
            image = request.FILES.get("image")
            last_donated_date =request.POST.get("last_date_of_donation")
            print('MMMMMMMMMMMMMM',date_of_donation)
            print('nnnnnnnnnnnnnnn',last_donated_date)
            d0 = datetime.strptime(date_of_donation, "%Y-%m-%d").date()
            d1 = datetime.strptime(last_donated_date, "%Y-%m-%d").date()
            delta=d0-d1
            if (18 <= age <= 60) and (weight >= 45) and (hemoglobin >= 12) and (volume == 350) and (delta.days >=90):
                don = Donar.objects.create(
                    name=name,
                    nationality=nationality,
                    phone=phone,
                    age=age,
                    sex=sex,
                    address=address,
                    blood_type=blood_type,
                    date_of_donation=date_of_donation,
                    donation=donation,
                    donar_status=donar_status,
                    volume=volume,
                    hemoglobin=hemoglobin,
                    wieght=weight,  
                    email=email,
                    medical_history=medical_history,
                    overall_health=overall_health,
                    image=image
                )  
                context = {'status': "success",'message': "success",}
                return JsonResponse(context)

            else:
               context = {'status': "failed",'message': "enter valid data",}
               return JsonResponse(context)
    return render(request,"adminn/donars.html")

def status(request):
     value = request.GET.get("value")
     id = request.GET.get("id")
     d=Donar.objects.get(id=id)
     d.donar_status=value
     d.save()
     
     context = {'status': "success",'message': "success",}
     return JsonResponse(context)

def logout_admin(request):
   logout(request)     
   return redirect('login') 


