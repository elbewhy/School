from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from .forms import StudentRegistrationForm , InstructorRegistrationForm,StudentLoginForm,InstructorLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Student,Instructor,Course

class HomeView(TemplateView):
    template_name = 'home.html'

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Save form data without committing to the database
            user.save()  # Save the user object to create a User instance
            student = Student(user=user)  # Create a Student instance linked to the User
            student.save()  # Save the student object
            login(request, user)  # Log in the newly registered user
            return redirect('/')
    else:
        form = StudentRegistrationForm()
    return render(request, 'courses/student_registration.html', {'form': form})
def instructor_registration(request):
    if request.method == 'POST':
        form = InstructorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            instructor = Instructor(user=user)
            instructor.save()
            login(request, user)
            return redirect('/')
    else:
        form = InstructorRegistrationForm()
    return render(request, 'courses/instructor_registration.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/student/dashboard/')
            else:
                # User authentication failed
                form.add_error(None, 'Invalid username or password.')
    else:
        form = StudentLoginForm()
    return render(request, 'courses/student_login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')
    
@login_required
def student_dashboard(request):
    student, created = Student.objects.get_or_create(user=request.user)
    courses = student.courses.all()
    context = {
        'student': student,
        'courses': courses,
    }
    return render(request, 'courses/student_dashboard.html', context)


def instructor_login(request):
    if request.method == 'POST':
        form = InstructorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/instructor/dashboard')  # Replace 'instructor_profile' with the URL name of the instructor's profile page
    else:
        form = InstructorLoginForm()
    return render(request, 'courses/instructor_login.html', {'form': form})

@login_required
def instructor_dashboard(request):
    # Logic for student dashboard
    return render(request, 'courses/instructor_dashboard.html')





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