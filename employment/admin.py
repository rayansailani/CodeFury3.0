from django.contrib import admin
from .models import Worker

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
