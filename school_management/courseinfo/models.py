from django.db import models
from courseinfo.models import Instructor, Student

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    
    
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=100)
    
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField()



