from django.shortcuts import render
from pratikapp.models import Student


def student_view(request):
    student=Student.objects.all()
    return render(request,'pratikapp/wish.html',{'student':student})
