import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from employee.emp_serializer import EmpDeptSerializer
from employee.models import Employees, Departments

# Create your views here.


def home(request):
    content = 'Welcome Employee Services'
    return HttpResponse(content)

@api_view(['POST'])
def add_employee(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        edserializer = EmpDeptSerializer(data=request.POST)
        if edserializer.is_valid():
            emp = Employees()
            emp.first_name = request.POST.get('first_name')
            emp.last_name = request.POST.get('last_name')
            emp.gender = request.POST.get('gender')
            # emp.hire_date = request.POST.get('hire_date')
            # emp.birth_date = request.POST.get('birth_date')
            emp.save(using='employee')

            dept = Departments()
            dept.dept_name = request.POST.get('department')
            dept.dept_id = emp.id
            dept.save(using='employee')

            content = {'message': 'Employee Added Successfully'}
            response = json.dumps(content)
            return HttpResponse(response)
        else:
            content = {'message': 'Employee registrations unsuccessful'}
            response = json.dumps(content)
            return HttpResponse(response)
    else:
        content = {'message': 'User Registration Failed, Please check the fields entered'}
        response = json.dumps(content)
        return HttpResponse(response, content_type="application/json")





