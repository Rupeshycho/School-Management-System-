from django import forms 
from django.contrib.auth.models import user
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True, unique=True)
    
    class Meta:
        model=user
        fields=['username', 'email', 'password1', 'password2']
        
    