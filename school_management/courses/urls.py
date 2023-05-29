from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('instructors/', views.InstructorListView.as_view(), name='instructor-list'),
    path('instructors/<int:pk>/', views.InstructorDetailView.as_view(), name='instructor-detail'),

    
]
