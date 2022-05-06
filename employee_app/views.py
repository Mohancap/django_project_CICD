from django.shortcuts import render
# from django.http import HttpResponse
from .models import Employee_details, Employee_personal_details

# Create your views here.


def base(request):
    post = Employee_details.objects.all()
    return render(request, "base.html", {"post": post})


def first(request):
    return render(request, "first.html", {"name": "Murali"})


def employee_contact_infor(request):
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        employee_id = request.POST['employee_id']
        contact_num = request.POST['contact_num']
        company_location = request.POST['company_location']
        emp_salary = request.POST['emp_salary']
        emp_age = request.POST['emp_age']
        emp_permanant_address = request.POST['permanant_address']
        emp_email_address = request.POST['email']
        emp_current_address = request.POST['current_address']
        created_date = request.POST.get('date')
        employee_details = Employee_personal_details(employee_name=employee_name, employee_id=employee_id, contact_num=contact_num,
        company_location=company_location, emp_salary=emp_salary, emp_age=emp_age,
        emp_permanant_address=emp_permanant_address, emp_email_address=emp_email_address,
        emp_current_address=emp_current_address, created_date=created_date)

        employee_details.save()

    return render(request, 'form_to_database.html')


def employee_info(request):
    post = Employee_personal_details.objects.all()
    return render(request, "base.html", {"post": post})
