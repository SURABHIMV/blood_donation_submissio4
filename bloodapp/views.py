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
from django.contrib.auth.decorators import login_required 
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
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
from helper import admin_access_only


def admin_loginn(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            admin_user = Patient.objects.get(username=username)
            print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',admin_user.user_type)
            admin_user.user_type='admin'
            admin_user.save()
            print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',admin_user.user_type)
            login(request, user)
            return redirect('homee')
        else:
          sweetify.error(request, 'Enter valid username and password')     
    return render(request,"adminn/login.html")


@admin_access_only()
def basee(request):  
     return render(request,"adminn/base.html")


@admin_access_only()
def homee(request):  
     return render(request,"adminn/homee.html")


@admin_access_only()
def dashboardd(request):
    pat= Patient.objects.all().count()
    pat=pat-1
    don= Donar.objects.all().count()
    print('prod',pat)
    context = {
        'patient_count':pat,
        'donar_count':don
    } 
    return render(request,"adminn/dashboard.html",context)


@admin_access_only()
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


@admin_access_only()
def donarss(request):
     don= Donar.objects.all()
     paginator = Paginator(don, 3)
     page = request.GET.get('page', 1)
     try:
        don = paginator.page(page)
     except PageNotAnInteger:
        don = paginator.page(1)
     except EmptyPage:
        don = paginator.page(paginator.num_pages)
     
     context={
         'data':don
     }
     return render(request,"adminn/donars.html",context)


@admin_access_only()
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

@admin_access_only()
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
            d0 = datetime.strptime(date_of_donation, "%Y-%m-%d").date()
            d1 = datetime.strptime(last_donated_date, "%Y-%m-%d").date()
            delta=d0-d1
            try:
              donar_user = Donar.objects.get(name=name)
            except ObjectDoesNotExist:
              donar_user = None
            
            phone_len=len(str(abs(phone)))
            # email_donar=re.match(r"[^@]+@[^@]+\.[^@]+", email)
            # print('gggggggggggggggggggggggggggggg',email_donar)
            if (18 <= age <= 60) and (weight >= 45) and (hemoglobin >= 12) and (volume == 350) and (delta.days >=90) and (donar_user is None) and (phone_len==10):
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
                    volume=volume,
                    hemoglobin=hemoglobin,
                    last_donated_date=last_donated_date,
                    wieght=weight,  
                    email=email,
                    medical_history=medical_history,
                    overall_health=overall_health,
                    image=image
                )  
                context = {'status': "success",'message': "success",}
                return JsonResponse(context)
            
            required_fields = []
            if phone_len!=10:
                required_fields.append("valid phone number is required")
            if donar_user:
                required_fields.append("donar already exists")
            
            if age < 18 or age > 60:
                required_fields.append("age limit and between 18 and 60 is eligible")
            if weight < 45:
                required_fields.append("weight >= 45 is eligible")
            
            if hemoglobin < 12:
                required_fields.append("hemoglobin > 12 is eligible")
            if volume != 350 :
                required_fields.append("volume must be >=350 is eligible")
            if  delta.days <90:
                required_fields.append("minimum 3month gap is eligible for donation")
           
            if required_fields:
                response = f"{', '.join(required_fields)}"
                return JsonResponse({"message": response, "status": "failed"})
            
    return render(request,"adminn/donars.html")

# @login_required(login_url='login')
# def create_donar(request):
#     if request.method == "POST":
            
#             name = request.POST.get("name")
#             nationality = request.POST.get("nationality")
#             phone = request.POST.get("phone")
#             phone=int(phone) if phone else None
#             age = request.POST.get("age")
#             age=int(age) if age else None
#             sex = request.POST.get("sex")
#             email = request.POST.get("email")
#             address = request.POST.get("address")
#             date_of_donation = request.POST.get("date_of_donation")
#             blood_type = request.POST.get("blood_type")
#             donation = request.POST.get("donation")
#             volume = request.POST.get("volume")
#             volume=int(volume) if volume else None
#             hemoglobin = request.POST.get("hemoglobin")
#             hemoglobin=int(hemoglobin)  if hemoglobin else None
#             weight = request.POST.get("weight")
#             weight=int(weight) if weight else None
#             medical_history = request.POST.get("medical_history")
#             overall_health = request.POST.get("overall_health")
#             image = request.FILES.get("image")
#             last_donated_date =request.POST.get("last_date_of_donation")
#             d0 = datetime.strptime(date_of_donation, "%Y-%m-%d").date()
#             d1 = datetime.strptime(last_donated_date, "%Y-%m-%d").date()
#             delta=d0-d1
#             try:
#               donar_user = Donar.objects.get(name=name)
#             except ObjectDoesNotExist:
#               donar_user = None
            
#             phone_len=len(str(abs(phone)))
#             print('phone_lennnnnnnnnnnnnnnnnnnnn',phone_len)
#             if (18 <= age <= 60) and (weight >= 45) and (hemoglobin >= 12) and (volume == 350) and (delta.days >=90) and (donar_user is None) and (phone_len==10):
#                 don = Donar.objects.create(
#                     name=name,
#                     nationality=nationality,
#                     phone=phone,
#                     age=age,
#                     sex=sex,
#                     address=address,
#                     blood_type=blood_type,
#                     date_of_donation=date_of_donation,
#                     donation=donation,
#                     volume=volume,
#                     hemoglobin=hemoglobin,
#                     last_donated_date=last_donated_date,
#                     wieght=weight,  
#                     email=email,
#                     medical_history=medical_history,
#                     overall_health=overall_health,
#                     image=image
#                 )  
#                 context = {'status': "success",'message': "success",}
#                 return JsonResponse(context)
            
#             if phone_len!=10:
#                context = {'status': "failed",'message': "Enter a valid phone number"}
#                return JsonResponse(context) 
#             if donar_user:
#                context = {'status': "failed",'message': "Donar exists"}
#                return JsonResponse(context)
#             if age < 18 or age > 60:
#                context = {'status': "failed",'message': "age limit and between 18 and 60 is eligible",}
#                return JsonResponse(context)
            
#             if weight < 45:
#                context = {'status': "failed",'message': "weight >= 45 is eligible",}
#                return JsonResponse(context)
            
#             if hemoglobin < 12:
#                context = {'status': "failed",'message': "hemoglobin > 12 is eligible",}
#                return JsonResponse(context)
            
#             if volume != 350 :
#                context = {'status': "failed",'message': "volume must be >=350 is eligible",}
#                return JsonResponse(context)
            
#             if  delta.days <90:
#                context = {'status': "failed",'message': "minimum 3month gap is eligible for donation",}
#                return JsonResponse(context)

#     return render(request,"adminn/donars.html")

@login_required(login_url='login')
def status(request):
     value = request.GET.get("value")
     id = request.GET.get("id")
     d=Donar.objects.get(id=id)
     d.donar_status=value
     d.save()
     
     context = {'status': "success",'message': "success",}
     return JsonResponse(context)


# @login_required(login_url='login')
# def donar_update(request):
#     if request.method == 'POST':
#         errors = {}

#         name = request.POST.get('name', '').strip()
#         nationality = request.POST.get('nationality', '').strip()
#         phone = request.POST.get('phone', '').strip()
#         age = request.POST.get('age', '').strip()
#         sex = request.POST.get('sex', '').strip()
#         email = request.POST.get('email', '').strip()
#         address = request.POST.get('address', '').strip()
#         date_of_donation = request.POST.get('date_of_donation', '').strip()
#         last_date_of_donation = request.POST.get('last_date_of_donation', '').strip()
#         donation = request.POST.get('donation', '').strip()
#         donar_status = request.POST.get('donar_status', '').strip()
#         volume = request.POST.get('volume', '').strip()
#         hemoglobin = request.POST.get('hemoglobin', '').strip()
#         weight = request.POST.get('weight', '').strip()
#         medical_history = request.POST.get('medical_history', '').strip()
#         overall_health = request.POST.get('overall_health', '').strip()
#         image =request.POST.get('image', '').strip()
        
#         if not name:
#             errors['name'] = 'name cannot be empty.'
#         if not nationality:
#             errors['nationality'] = 'nationality cannot be empty.'

#         if not phone:
#             errors['phone'] = 'phone cannot be empty.'

#         if not age:
#             errors['age'] = 'age cannot be empty.'
#         if not sex:
#             errors['sex'] = 'sex cannot be empty.'
#         if not sex:
#             errors['email'] = 'email cannot be empty.'
#         if not address:
#             errors['address'] = 'address cannot be empty.'
#         if not date_of_donation:
#             errors['date_of_donation'] = 'date_of_donation cannot be empty.'
#         if not last_date_of_donation:
#             errors['last_date_of_donation'] = 'last_date_of_donation cannot be empty.'
#         if not donation:
#             errors['donation'] = 'donation cannot be empty.'
#         if not donar_status:
#             errors['donar_status'] = 'donar_status cannot be empty.'
#         if not volume:
#             errors['volume'] = 'volume cannot be empty.'
#         if not hemoglobin:
#             errors['hemoglobin'] = 'hemoglobin cannot be empty.'
#         if not weight:
#             errors['hemoglobin'] = 'weight cannot be empty.'
#         if not medical_history:
#             errors['medical_history'] = 'medical_history cannot be empty.'
#         if not overall_health:
#             errors['overall_health'] = 'overall_health cannot be empty.'
#         if not image:
#             errors['image'] = 'image cannot be empty.'
        
        
#         if errors:
#             return JsonResponse(errors, status=400)

#         # Process valid data here
#         # For example, save the data to the database
        
#         return JsonResponse({'success': 'Data processed successfully.'})



@admin_access_only()
def edit_donar(request):
    context={}
    id = request.GET.get("id")
    print('',id)
    id = request.GET.get("id")
    data = Donar.objects.get(id=id)
    template = loader.get_template('adminn/edit_donar.html')
    context['data']=data
    print("context",context)
    rendered_template = template.render(context, request)
    return JsonResponse({"rendered_template":rendered_template})

@admin_access_only()
def edit_donar_actionn(request):
  if request.method == "POST":
        id=request.POST.get("donar_id")
        date_of_donation = request.POST.get("Date_of_donation")
        last_date_of_donation = request.POST.get("last_date_of_donation")
       
        print('ddddddddddddddddddddddd',date_of_donation)
        d0 = datetime.strptime(date_of_donation, "%Y-%m-%d")
        d1= datetime.strptime(last_date_of_donation, "%Y-%m-%d")
       
        delta=d0-d1
        if delta.days >=90:
       
            data = Donar.objects.get(id=id)
            data.date_of_donation=d0
            data.last_donated_date=d1
            data.save()
            return JsonResponse({"message": "success", "status": "success"})
        else:
            data = Donar.objects.get(id=id)
            data.delete()
            return JsonResponse({"message": "success", "status": "success"})


@admin_access_only()
def logout_admin(request):
   logout(request)     
   return redirect('login') 


