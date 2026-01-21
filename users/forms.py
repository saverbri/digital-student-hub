from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, initial='student')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2', 
                 'phone', 'course_group', 'department', 'bio']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'phone', 'bio', 'course_group', 'department']