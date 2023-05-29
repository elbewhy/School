from django.views.generic import ListView, DetailView
from .models import Course, Instructor
from django.views.generic import TemplateView






class HomeView(TemplateView):
    template_name = 'home.html'




class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class InstructorListView(ListView):
    model = Instructor
    template_name = 'courses/instructor_list.html'
    context_object_name = 'instructors'

class InstructorDetailView(DetailView):
    model = Instructor
    template_name = 'courses/instructor_detail.html'
    context_object_name = 'instructor'
