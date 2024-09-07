from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
CATEGORY_CHOICES = (
        ("O+", "O+"),
        ("O-", "O-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("A+", "A+"),
        ("A-", "A-"),
        ("AB+", "AB+"),
        ("AB-", "AB-")
    )

CATEGORY_CHOICES1 = (
        ("Female", "Female"),
        ("Male", "Male"),
        ("Others","Others")
    )
class Patient(AbstractUser):
    
    image = models.FileField(upload_to="patient_image", null=True, db_index=True)
    blood_type= models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    age= models.IntegerField(null=True, db_index=True)
    sex= models.CharField(choices=CATEGORY_CHOICES1,max_length=100)
    phone = models.BigIntegerField(null=True, db_index=True)
    address= models.TextField(null=True, db_index=True)
    comment= models.TextField(null=True, db_index=True)
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS= []

    def __str__(self):
        return str(self.username)
    
options=  (
        ("Indian", "Indian"),
        ("Others","Others")
    )
type_donation=(("Whole blood", "Whole blood"),
               ("Red cell","Red cell"),
               ("plasma","plasma"),
               ("platelate","platelate"))
status= (("Accepted", "Accepted"),
               ("Rejected","Rejected"),
               ("pending","pending"))

health=(("good","good"),
        ("best","best"),
        ("need improvement","need improvement"))


class Donar(models.Model):
    name= models.CharField(max_length=200, null=True, db_index=True)
    image = models.FileField(upload_to="donar_image", null=True, db_index=True)
    nationality= models.CharField(choices=options, max_length=100)
    phone = models.BigIntegerField(null=True, db_index=True)
    age= models.IntegerField(null=True, db_index=True)
    sex= models.CharField(choices=CATEGORY_CHOICES1,max_length=100)
    email = models.CharField(max_length=200, null=True, db_index=True)
    phone = models.BigIntegerField(null=True, db_index=True)
    address= models.TextField(null=True, db_index=True)
    blood_type= models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    date_of_donation= models.DateField(null=True)
    donation= models.CharField(choices=type_donation, max_length=100)
    donar_status= models.CharField(choices=status, max_length=100)
    volume= models.IntegerField(null=True, db_index=True)
    hemoglobin= models.IntegerField(null=True, db_index=True)
    last_donated_date= models.DateField(null=True)
    wieght=models.IntegerField(null=True, db_index=True)
    medical_history= models.TextField(null=True, db_index=True)
    overall_health= models.CharField(choices=health, max_length=100)









