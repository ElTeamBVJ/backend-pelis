from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label = 'Username', widget= forms.TextInput(attrs = {'class':'form-input'}))
    email = forms.EmailField(widget= forms.TextInput(attrs = {'class':'form-input'}))
    password1 = forms.CharField(label = 'Password', widget= forms.PasswordInput(attrs = {'class':'form-input','placeholder': '********'}))
    password2 = forms.CharField(label = 'Repeat password', widget = forms.PasswordInput(attrs = {'class':'form-input','placeholder': '********'}))
   
class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}