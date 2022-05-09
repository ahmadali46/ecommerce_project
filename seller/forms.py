from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import RegisterModel,Machine,Worker
from django import forms
from django.contrib.auth.models import User

class SellerRegistrationForm(forms.ModelForm):
    firstname= forms.CharField(max_length=50,label='username')
    lastname = forms.CharField(max_length=50,label='lastname')
    email = forms.CharField(max_length=50,widget=forms.EmailInput)
    password1 = forms.CharField(max_length=50,label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50,label='confirm password',widget=forms.PasswordInput)
    class Meta:
        model = RegisterModel
        fields = ['firstname','lastname','email','password1','password2']
        
class SellerLoginForm(AuthenticationForm):
    username= forms.CharField(label='email/username')
    



        