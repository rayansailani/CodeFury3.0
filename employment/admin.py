from django.contrib import admin
from .models import Worker, Company

# Register your models here.


class employee(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "dob",
        "adhar",
        "other",
        "work",
        "dateTime",
        "is_employed",
    ]


admin.site.register(Worker, employee)


class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "CBDT_id",
        "other",
        "work",
        "dateTime",
        "Ammount_paid",
        'address',
    ]


admin.site.register(Company, CompanyAdmin)
