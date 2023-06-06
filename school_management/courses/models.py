from django.contrib.auth.models import User
from django.db import models



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    # Additional fields for student

    def __str__(self):
        return self.user.username if self.user else 'Unassigned'
    
    
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    bio = models.TextField(blank=True)
    email = models.EmailField()
    # profile_picture = models.ImageField(upload_to='instructor_profile_pics/', blank=True)

    def __str__(self):
        return self.user.username


# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
#     # Additional fields for instructor

#     def __str__(self):
#         return self.user.username if self.user else 'Unassigned'

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.course}"
