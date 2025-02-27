from django.shortcuts import render, redirect
from .models import Employee, Payslip

# Create your views here.

def employees(request):
    employee_objs = Employee.objects.all()
    return render(request, 'payroll_app/employees.html',
                  {'employees': employee_objs})

def create_employee(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'payroll_app/create_employee.html')

def update_employee(request, pk):
    if request.method == "POST":
        pass
    else:
        return render(request, 'payroll_app/update_employee.html')

def payslips(request):
    if request.method == "POST":
        pass
    else:
        payslip_objs = Payslip.objects.all()
        return render(request, 'payroll_app/payslips.html',
                      {'payslips': payslip_objs})

def view_payslip(request):
    return render(request, 'payroll_app/view_payslip.html')

def delete_employee(request, pk):
    Employee.objects.filter(pk=pk).delete()
    return redirect('employees')
