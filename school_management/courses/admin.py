from django.contrib import admin

from .models import Instructor, Course, Student,Registration



# Custom LogEntryAdmin class



# Register your models here.
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Registration)

# Register the updated LogEntry admin with the updated user model

