"""Lazapee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees, name="employees"),
    path('create_employee', views.create_employee, name="create_employee"),
    path('update_employee/<int:pk>/', views.update_employee, name="update_employee"),
    path('payslips', views.payslips, name="payslips"),
    path('view_payslip', views.view_payslip, name="view_payslip"),
    path('delete_employee/<int:pk>/', views.delete_employee, name="delete_employee"),
]
