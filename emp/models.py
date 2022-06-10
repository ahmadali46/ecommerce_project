from django.contrib import messages
from email import message
from email.policy import default
from tkinter.messagebox import NO
from urllib import request
from uuid import UUID
import uuid
import datetime
from click import option
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self,email,contact,password=None,confirm_password=None):
        if not confirm_password:
            raise ValueError('user must have an email address agdhfjt')
        if not email:
            raise ValueError('user must have an email address')
        user = self.model(
            email= self.normalize_email(email), 
            contact=contact,  
            confirm_password=confirm_password,
        )
        user.set_password(password)
        user.set_comfirm_password(confirm_password)
        
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,contact,password=None):
        user = self.create_user(email,contact=contact,password=password)
        user.is_admin = True
        user.user_type='SUPERADMIN'
        user.save(using=self._db)
        return user
        # is_staff
    
class MyUser(AbstractBaseUser):
    USER_ROLES = (
        ('SELLER','seller'),
        ('SUPERADMIN','super admin'),
        ('CUSTOMER', 'customer'),
        
    )
    options=(
        ('accept','accept'),
        ('reject','reject'),
        ('delay','delay'),
       
    )
    username=None
    email = models.EmailField(verbose_name='email address',max_length=254,unique=True)
    contact = models.CharField(max_length=11,null=True)
    user_type = models.CharField(max_length=11,choices=USER_ROLES,null=True)
    option_type = models.CharField(max_length=7,choices=options,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    
    objects  = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact']
    
    def __str__(self):
        return self.email
    
    def has_perm(self,perms,obj=None):
        return True

    def has_perms(self,perms,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


class Product(models.Model):
    choice_field = (
        
        ('mobile','mobile'),
        ('laptop','laptop'),     
    )

    # default=request.email
    #  <input type="file" name="upload" accept=".doc, .docx, .pdf, .txt">
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=settings.AUTH_USER_MODEL)
    # product_id = models.ForeignKey(primary_key=True,default=False,on_delete=models.CASCADE)
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    discounted_price =models.FloatField()
    image_upload = models.ImageField(upload_to='',height_field=None, width_field=None, max_length=None,default=None,null=True)
    file = models.FileField(null = True)
    category = models.CharField(max_length=6,choices=choice_field,default=None,null=True)
    def __str__(self):
        return self.title

class employee(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
     Firstname = models.CharField(max_length=50)
     Lastname = models.CharField(max_length=50)
     Email = models.EmailField(max_length = 254,default=None)
     City = models.CharField(max_length=50)
     Salary = models.FloatField()
    #  location = models.PointField()
     def __str__(self):
         return str(self.user)
     
class get_user(models.Model):
    email =  models.EmailField(max_length = 254,default=None)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    
    
# class Reg(models.Model):
#         # User = models.ForeignKey(User, on_delete=models.CASCADE)
#      Username  = models.CharField(max_length=50)
#      Firstname = models.CharField(max_length=50)
#      Lastname = models.CharField(max_length=50)
#      Email = models.EmailField(max_length = 254,default=None)
#      City = models.CharField(max_length=50)
#      Salary = models.FloatField()
    
#      def __str__(self):
#          return self.Username

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    

class Cart(models.Model):

    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE,default=True) 
    price = models.IntegerField(default=1)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    # date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
         return str(self.product)
    
class Wishlist(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE) 
    item  = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        unique_together = ['customer','item']
    def __str__(self):
         return str(self.item)


class Category(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self) :
        return str(self.name)
    

class RandomList(models.Model):
    category = models.ForeignKey(Category, related_name="random_list", on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=False)
    description = models.TextField(null=True)


    def __str__(self):
        return str(self.name)
    
# Create your models here.
