from django.test import TestCase

# Create your tests here.

from .models import Employee_information


class EmployeeTests(TestCase):
    def test_page_is_created_successfully(self):
        self.employee_app = Employee_information.objects.create(
            title="Bangalore",
            name="Bangalore",
            location="Bangalore")


def employee_information(self):
    e = self.employee_app
    self.assertTrue(isinstance(e, Employee_information))
    self.assertEqual(str(e), 'Bangalore')
