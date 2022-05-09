from xml.dom.minidom import Attr
from django import forms
from . models import *
from . models import employee
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
# from django.contrib.gis.db import models
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from emp.models import MyUser
from django.contrib.auth import get_user_model


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=50,label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50,label='confirm password',widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ('email','user_type','contact')


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('password does not match')
        return password2
    
    def save(self,commit =True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField() 
    
    class Meta:
        model = MyUser
        fields = ('email','password','contact','is_active','is_admin')


class EmployeeForm(forms.ModelForm):
    #  location = .PointField
     class Meta:
      model =  employee
      fields = ['Firstname','Lastname','Email','City','Salary']
      
class ProductForm(forms.ModelForm):
    # email = forms.CharField(max_length=50,label='email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    title = forms.CharField(max_length=50,label='title',widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=50,label='description',widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(max_value=399999,label='price',widget=forms.NumberInput(attrs={'class': 'form-control'}))
    discounted_price = forms.IntegerField(max_value=399999,label='discounted_price',widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image_upload = forms.ImageField(label='image_upload',widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    file = forms.FileField(label='file',widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['user','title','description','price','discounted_price','image_upload','file','category']
        # exclude = ('user',)
     
class UpdateForm(forms.ModelForm):
     class Meta:
      model =  employee
      fields = ['Firstname','Lastname','Email','City','Salary']
     
class RegistrationForm(UserCreationForm):
    # username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50,label='email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=50,label='password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=50,label='confirm password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(max_length=11, required=False,widget=forms.NumberInput(attrs={'class': 'form-control'}))
     #salary = forms.FloatField(max_value=200, required=False)
    class Meta:
         model = get_user_model()
         fields = ('email',  'password1', 'password2','contact')
        #  model = User
        #  fields =['username','email','first_name','last_name']

class LoginForm(AuthenticationForm):
    username= forms.CharField(label='email/username')
    
