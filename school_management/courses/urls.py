from django.urls import path
from . import views
from .views import student_registration




app_name = 'courses'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
       path('student/register/', student_registration, name='student_registration'),
       path('student/login/', views.student_login, name='student_login'),
       path('student/dashboard/', views.student_dashboard, name = 'student_dashboard'),
       
       path('courses/', views.CourseListView.as_view(), name='course-list'),
       path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
       
       path('instructors/', views.InstructorListView.as_view(), name='instructor-list'),
       path('instructors/<int:pk>/', views.InstructorDetailView.as_view(), name='instructor-detail'),
       path('logout/', views.logout_view, name='logout'),
    
    ]

