from django.db import models
from datetime import datetime
# Create your models here.


class Employee_details(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    about_self = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class Employee_personal_details(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    emp_salary = models.CharField(max_length=100)
    emp_age = models.CharField(max_length=100)
    emp_permanant_address = models.TextField()
    emp_email_address = models.CharField(max_length=200)
    emp_current_address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name
        