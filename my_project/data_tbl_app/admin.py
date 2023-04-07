from django.contrib import admin

from data_tbl_app.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'salary', 'occupation', 'gender']
    list_per_page = 8
    search_fields = ['name', ]


admin.site.register(Employee, EmployeeAdmin)
