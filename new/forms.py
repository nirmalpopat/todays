from django.core import validators
from django import forms
from django.forms import widgets
from . import models
from .models import Usermodel
from .models import User

class UserForm(forms.Form):
    class Meta:
        model = models.Usermodel
        fields = ['password']
        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput() 
        }

class UserRegistration(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = ['user_name','password','user_type']
        widgets = {
            'user_name' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'user_type' : forms.TextInput(attrs={'class':'form-control'}),
        }