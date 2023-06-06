from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class InstructorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class InstructorLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# class StudentLoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email') 
#         password = cleaned_data.get('password')

#         if email and password:
#             user = authenticate(email=email, password=password)
#             if user is None:
#                 raise forms.ValidationError('Invalid email or password.')
        
#         return cleaned_data


# class InstructorLoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)








# class InstructorRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
    

#     class Meta:
#         model = Instructor
#         fields = ['name', 'email', 'bio', 'password']
        
        
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if password and confirm_password and password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")

#         return cleaned_data
