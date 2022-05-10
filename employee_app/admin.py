from django.contrib import admin
from .models import Employee_details, Employee_personal_details, Employee_information

# Register your models here.

admin.site.register(Employee_details)
admin.site.register(Employee_personal_details)
admin.site.register(Employee_information)
