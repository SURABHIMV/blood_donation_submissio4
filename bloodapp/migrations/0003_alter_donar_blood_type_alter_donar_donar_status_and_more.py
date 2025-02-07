# Generated by Django 5.1 on 2024-09-10 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0002_alter_donar_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donar',
            name='blood_type',
            field=models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='donar',
            name='donar_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('pending', 'pending')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donar',
            name='donation',
            field=models.CharField(choices=[('Whole blood', 'Whole blood'), ('Red cell', 'Red cell'), ('plasma', 'plasma'), ('platelate', 'platelate')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donar',
            name='nationality',
            field=models.CharField(choices=[('Indian', 'Indian'), ('Others', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donar',
            name='overall_health',
            field=models.CharField(choices=[('good', 'good'), ('best', 'best'), ('need improvement', 'need improvement')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='donar',
            name='sex',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=100, null=True),
        ),
    ]
