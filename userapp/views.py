from django.shortcuts import render,redirect
from bloodapp.models import *
from django.contrib.auth import authenticate,login
from django.template import loader
from django.http import JsonResponse
from django.contrib.auth import logout
import sweetify
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def user_signup(request):
    if request.method == "POST":
            name = request.POST.get("name")
            blood_type = request.POST.get("blood_type")
            age = request.POST.get("age")
            age=int(age) if age else None
            sex = request.POST.get("sex")
            email = request.POST.get("email")
            password = request.POST.get("password")
            phone= request.POST.get("phone")
            phone=int(phone) if phone else None
            address= request.POST.get("address")
            comment= request.POST.get("comment")
            image= request.FILES.get("image")
            don = Patient.objects.create(
                    username=name,
                    image=image,
                    blood_type=blood_type,
                    age=age,
                    sex=sex,
                    email=email,
                    phone=phone,
                    address=address,
                    comment=comment
                    )
            don.set_password(password)
            don.save()
            return redirect('user_login')
    
    return render(request,"users/signup.html")


def user_login(request):
    if request.method == "POST":
            name = request.POST.get("name")
            password = request.POST.get("password")
            print("bbbbbbbbbbbbbbbbbb",name,password)
            user = authenticate(username=name, password=password)
            print(user)
            if user:
              login(request, user)
              return redirect('home')
            else:
               sweetify.error(request, 'Enter valid username and password')     
    return render(request,"users/login.html")

@login_required(login_url='user_login')
def view_u(request):
    
    id = request.GET.get("id")
    context={}
    print('kkkkkkkkkkkkkkkkkkkkk',id)
    if id:
         donn = Donar.objects.get(id=id)
    
    context={
         'data':donn
    }
    print("context",context)
    template = loader.get_template('users/u_dashboard_detail.html')
    rendered_template = template.render(context, request)
    return JsonResponse({"rendered_template":rendered_template})

@login_required(login_url='user_login')
def new_patient(request):
    return render(request,"users/home.html")

@login_required(login_url='user_login')
def dashboardd(request):
    user = request.user
    if user.is_authenticated:
       nam=Patient.objects.filter(username=user)
       patient = nam.get()  
       b_type=patient.blood_type
       if b_type=="A+":
                a=b_type
                b="A-"
                c="O+"
                d="O-"
                blood_types = [a, b, c, d]
                nam=Donar.objects.filter(blood_type__in=blood_types)
               
                
       elif b_type=="A-":
            a="A-"
            b="O-"
            blood_types = [a, b]
            nam=Donar.objects.filter(blood_type__in=blood_types)
            
            
       elif b_type=="B+":
            a="B+"
            b="B-"
            c="O+"
            d="O-"
            blood_types = [a,b,c,d]
            nam=Donar.objects.filter(blood_type__in=blood_types)
            
            
       elif b_type=="B-":
            a="B-"
            b="O-"
            blood_types = [a,b]
            nam=Donar.objects.filter(blood_type__in=blood_types)
            
            
       elif b_type=="O+":
            a="O+"
            b="O-"
            blood_types = [a,b]
            nam=Donar.objects.filter(blood_type__in=blood_types)
            
            
       elif b_type=="O-":
            a="O-"
            blood_types = [a]
            nam=Donar.objects.filter(blood_type__in=blood_types)
            
            
       elif b_type=="AB+":
            a="A+"
            b="A-"
            c="B+"
            d="B-"
            e="O+"
            f="O-"
            g="AB+"
            h="AB-"
            blood_types = [a,b,c,d,e,f,g,h]
            nam=Donar.objects.filter(blood_type__in=blood_types)
            
        
       elif b_type=="AB-":
            a="AB-"
            b="A-"
            c="B-"
            d="O-"
            blood_types = [a,b,c,d]
            nam=Donar.objects.filter(blood_type__in=blood_types)
       paginator = Paginator(nam, 3)
       page = request.GET.get('page', 1)
       try:
         nam = paginator.page(page)
       except PageNotAnInteger:
         nam = paginator.page(1)
       except EmptyPage:
         nam = paginator.page(paginator.num_pages)
     
       context={
                'data':nam
                }
        
    return render(request,"users/u_dashboard.html",context)

@login_required(login_url='user_login')
def add_mail(request):
     context = {}
     id = request.GET.get("id")

     user = request.user
     nam=Patient.objects.filter(username=user)
     nam=nam.get()
     p_name=nam.username
     p_blood=nam.blood_type
     p_age=nam.age
     p_sex=nam.sex
     p_phone=nam.phone
     p_address=nam.address
     p_phone=nam.phone
     p_email=nam.email

     print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',nam.blood_type,nam.age,nam.sex)
     if id:
         donar= Donar.objects.get(id=id)
         blood_type=donar.blood_type
         email=donar.email
         name=donar.name
         phone=donar.phone
         age=donar.age
         sex=donar.sex
         address=donar.address
         date_of_donation=donar.date_of_donation

     context['data']=nam
     from_email = "<surabhi2996@gmail.com>"
     if name and email:
            subject = "Urgent need of blood"
            html_message = render_to_string('users/mail_template.html',context)
            plain_message = strip_tags(html_message)
            to_email = [email]
            msg = EmailMultiAlternatives(subject, plain_message, from_email, to_email)
            msg.attach_alternative(html_message, "text/html")
            msg.send()
          #   send_mail(subject, plain_message, from_email, to_email)
            messages.info(request, "Your Request Shared Successfully")
     else:
            messages.info(request, "something went wrong")
     context = {'status': "success",'message': "success"}
     from_email = "<surabhi2996@gmail.com>"
     ##admin
     admin_name="surabhi"
     admin_email="surabhi2996@gmail.com"
     if admin_name and admin_email:
            subject = "Urgent need of blood"
            message = f"Are you willing for blood donation \n\n patient details \n\n patieint_Name: {p_name} \n patient_blood_type: {p_blood} \n patient_email:{p_email}\n patient_age: {p_sex} \n patient_address: {p_address} \n patient_phone: {p_phone}\n\n donar details \n\n donar_Name: {name} \n donar_blood_type: {blood_type} \n donar_email:{email} \n donar_age: {sex} \n donar_address: {address} \n donar_phone: {phone} \n date_of_donation: {date_of_donation}"
            to_email = [admin_email]
            send_mail(subject, message, from_email, to_email)
            messages.info(request, "Your Request Shared Successfully")
     else:
            messages.info(request, "something went wrong")
     return JsonResponse(context)

@login_required(login_url='user_login')
def mail(request):
    return render(request,"users/mail_template.html")

@login_required(login_url='user_login')   
def logout_adminn(request):
   logout(request)     
   return redirect('user_login') 

