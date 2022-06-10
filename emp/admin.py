from itertools import product
from django.contrib import admin

from .models import employee,get_user,Product,Cart,CartItem,Wishlist,Category,RandomList
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from emp.models import MyUser

admin.site.register(MyUser)

@admin.register(get_user)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('email','contact','password1')

@admin.register(Product)
class Productdetail(admin.ModelAdmin):
    list_display = ['title','description','price','discounted_price']
    
admin.site.register(Cart)

admin.site.register(CartItem)

admin.site.register(RandomList)

admin.site.register(Category)

admin.site.register(Wishlist)




@admin.register(employee)
class Admin(admin.ModelAdmin):
     list_display = ['id','Firstname','Lastname','Email','City','Salary']


# Register your models here.
