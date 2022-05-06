from django.test import TestCase

# Create your tests here.

from .models import Employee_details


class EmployeeTests(TestCase):
    def test_page_is_created_successfully(self):
        employee_information = Employee_details(
            title = "Employee details",
            name = "Murali",
            age = 28,
            salary = 100000,
            location = "Bangalore",
            about_self = "Hi, This is Murali Mohan, Working at Capgemini in Bangalore",
            created_at = "time"
        )
        employee_information.save()
