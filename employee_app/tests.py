from django.shortcuts import render
from django.test import TestCase
from datetime import datetime

# Create your tests here.

from .models import Employee_information


class EmployeeTests(TestCase):
    def test_page_is_created_successfully(self):
        employee_information = Employee_information(
            title = "Employee details",
            name = "Murali",
            age = 28,
            salary = 100000,
            location = "Bangalore",
            about_self = "Hi, This is Murali Mohan, Working at Capgemini in Bangalore",
            # created_at = datetime.now()
        )
        employee_information.save()

def employee_information(request):
    post = Employee_information.objects.all()
    return render(request, "base.html", {"post": post})