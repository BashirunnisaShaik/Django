from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    marks=models.IntegerField()

class faculty(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dept = models.CharField(max_length=100)
    salary=models.IntegerField()

class course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    