from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class RegisterModel(models.Model):
    username = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default=None)
    
    password1 = models.CharField(max_length=50,null=True)
    password2 = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.username
    
    


# Create your models here.
#DataFlair #Many to Many Relationship
class Worker(models.Model):
    name = models.CharField(max_length=255)

class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(
        Worker,
        related_name='Machine'
    )
    
class OneCustomer(models.Model):
    name = models.CharField(max_length=255)
class oneVehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        OneCustomer,
        on_delete=models.CASCADE,
        related_name='vehicle'
    )
    
    
class ManyCustomer(models.Model):
    name = models.CharField(max_length=255)
class ManyVehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        ManyCustomer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )
# Create your models here.
