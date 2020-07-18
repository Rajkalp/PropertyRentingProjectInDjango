from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput
from .models import Property

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
          'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
          'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
          'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
          'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'ReEnter Password'}),
        }

class UploadProperty(ModelForm):
    class Meta:
        model = Property
        fields = ['owner_name','landmark', 'address1', 'address2', 'city','region','zipcode','rent']
        widgets = {
          'address1': forms.Textarea(attrs={'rows':2}),
          'address2': forms.Textarea(attrs={'rows':2}),
        }
