from django.contrib import admin
from django.urls import path
from django.conf import settings
from bloodapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.admin_loginn,name='login'),
    path('base/',views.basee,name='base'),
    path('logout/',views.logout_admin,name='logout'),
    path('dashboard/',views.dashboardd,name='dashboard'),
    path('donar/',views.donarss,name='donars'),
    path('patient/',views.patientss,name='patients'),
    path('donar/view_donar/',views.view_donarr,name='view_donar'),
    path('donar/create_donar',views.create_donar,name='create_donar'),
    path('donar/status',views.status,name='status'),
    path('homee/',views.homee,name='homee'),
    path('donar/edit_donar',views.edit_donar,name='edit_donar'),
    path('donar/edit_donar_actionn',views.edit_donar_actionn,name='edit_donar_action')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)