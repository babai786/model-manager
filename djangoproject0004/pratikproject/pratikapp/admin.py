from django.contrib import admin
from pratikapp.models import  Student
from pratikapp.models import Proxystudent
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['sname','sno','smarks']

admin.site.register(Student,StudentAdmin)


class Proxystudentadmin(admin.ModelAdmin):
    list_display=['sname','sno','smarks']


admin.site.register(Proxystudent,Proxystudentadmin)
