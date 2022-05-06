from django.db import models
from datetime import datetime
from django import forms
# Create your models here.

class Employee_details(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    salary = models.IntegerField()
    location = models.CharField(max_length = 100)
    about_self = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title   


class Employee_personal_details(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    contact_num = models.IntegerField()
    company_location = models.CharField(max_length=100)
    emp_salary = models.IntegerField()
    emp_age = models.IntegerField()
    emp_permanant_address = models.TextField()
    emp_email_address = models.CharField(max_length=200)
    emp_current_address = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.full_name