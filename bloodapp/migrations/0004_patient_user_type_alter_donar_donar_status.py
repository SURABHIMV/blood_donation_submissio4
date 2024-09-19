# Generated by Django 5.1 on 2024-09-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0003_alter_donar_blood_type_alter_donar_donar_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='user_type',
            field=models.CharField(choices=[('admin', 'admin'), ('patient', 'patient')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='donar',
            name='donar_status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=100, null=True),
        ),
    ]