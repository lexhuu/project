from django.contrib import admin

# Register your models here.
from pro.models import student,employee

admin.site.register(student)
admin.site.register(employee)

