from django.contrib import admin

from .models import Instructor, Course, Student



# Custom LogEntryAdmin class



# Register your models here.
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)

# Register the updated LogEntry admin with the updated user model

