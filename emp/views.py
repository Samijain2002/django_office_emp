from datetime import datetime
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render (request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    data = {"emps":emps}
    return render(request, "all_emp.html", data)

def remove_emp(request, emp_id = 0):
    if emp_id != 0:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return render (request, 'index.html')
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    data = {"emps":emps}
    return render(request, "remove_emp.html", data)

    
def add_emp(request):
    if request.method == "POST":   
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        Employee.objects.create(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id= dept, role_id = role, hire_date = datetime.now())
        return render (request, 'index.html')
    elif request.method == "GET":
        dept = Department.objects.all()
        role = Role.objects.all()
        context = {"dept":dept, "role":role}
        return render(request, "add_emp.html",context)  
    else:
        return HttpResponse("An error occured")

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(first_name__contains = name)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')