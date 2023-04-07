from django.shortcuts import render

from data_tbl_app.models import Employee


def home(request):
    employee_list = Employee.objects.all()
    data = {
        'employees': employee_list,
    }

    return render(request, 'home.html', data)
