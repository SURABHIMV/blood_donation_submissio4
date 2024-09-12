from django.contrib import admin
from django.urls import path
from django.conf import settings
from userapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.user_signup,name='user_signin'),
    path('user_login/',views.user_login,name='user_login'),
    path('u_dashboard/',views.dashboardd,name='u_dashboard'),
    path('home/',views.new_patient,name='home'),
    path('u_dashboard/view_u/',views.view_u,name='view_u'),
    path('user_logout/',views.logout_adminn,name='user_logout'),
    path('u_dashboard/addmail',views.add_mail,name='addmail'),
    path('u_dashboard/mail',views.mail,name='mail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

