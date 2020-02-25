from django.db import models

class CostomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(smarks__gt=40).order_by('sname')

    def sorting(self):
        return super().get_queryset().order_by('-sname')

class CostomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(smarks__gt=70)
















class Student(models.Model):
    sname=models.CharField(max_length=30)
    sno=models.IntegerField()
    smarks=models.FloatField()
    objects=CostomManager1()


class Proxystudent(Student):
    objects=CostomManager2()
    class Meta:
        proxy=True
