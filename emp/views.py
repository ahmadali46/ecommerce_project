from atexit import register
import email
from importlib.metadata import files
from itertools import product
from msilib.schema import File
from operator import concat
from turtle import home
from unicodedata import category
from urllib import request
from uuid import uuid1
from django import views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import *
from . forms import *
import copy
import os
from . import views
from django.views.generic import CreateView,DeleteView,ListView
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from crud.settings import LOGIN_REDIRECT_URL
import time

@login_required(login_url='login')
def add(request):
    print('add')
    return render(request,'add.html')


@login_required
def logout(request):
    auth.logout(request)
    # if auth.is_authenticate:
    
    return render(request,'logout.html')
    # time.sleep(10)    
    # return redirect('login')

@login_required(login_url='login')
def start(request):
    return render(request,'start.html')

@login_required
def editemployee(request,id): 
     ed = employee.objects.get(id=id)
     form = EmployeeForm(request.POST or None,instance=ed)
     if request.method == 'POST':
     #  form = UpdateForm(request.POST)
     #  print('form2',form)
     
      if form.is_valid():
       form.save()
       return redirect('get')  
     context = {'ed':ed,'form':form}
     return render(request,'edit.html',context)

# @login_required
# def editemployee(request,id):                 when exeuted email already exist
#     ed = employee.objects.get(id=id)
#     form = EmployeeForm(request.POST or None,instance=ed)
#     if request.method == 'POST':
#       email = request.POST['Email']
#       emp_email=employee.objects.filter(Email=email)
#       if emp_email:
#             messages.success(request,'this email is already exit')
            
#      #  form = UpdateForm(request.POST)
#      #  print('form2',form)    
#             if form.is_valid():
#                 form.save()
#                 return redirect('get')  
#     context = {'ed':ed,'form':form}
#     return render(request,'edit.html',context)
 
@login_required(login_url='login')
def about(request):
    return render(request,'about.html')

def adminlogin(request):
    if request.user.is_authenticated:
        return redirect(LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        email = request.POST.get()

def loggin(request):
    # user1 = MyUser.objects.filter(id=request.user.id).delete()
    # request.session.save()
    
    # user =user.session_set.all().delete()
    # user = MyUser.user_type.objects.get(id=request.user.id)
    # user.clean()
    # user.save()
    
    # return redirect('get')
    if request.user.is_authenticated:
            return redirect(LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        # user1 = MyUser.objects.all()
        # if user1:
        #     user1.save()
            
            # username=request.POST.get('username') # username used in html input name="username"
        email = request.POST.get('email')
        password = request.POST.get('password')
        # email = request.session.get('email')
        # password = request.session.get('password')
        
            # username = form.cleaned_data['username'] if use form then using clean data 
            # password = form.cleaned_data['password']
        # user = MyUser.objects.filter(choice_field='SELLER')
        # user1 = MyUser.objects.filter(choice_field='SUPERADMIN')
        # user2 = MyUser.objects.filter(choice_field='CUSTOMER')
        user =authenticate(password=password,email=email )
        # user1 =authenticate(password=password,email=email )
        # user2 =authenticate(password=password,email=email )
        
        if user:
        
            print("log",user.user_type)
            if user.user_type=='SELLER':
                print('seller')
                login(request,user)
                messages.success(request,f"you are  logged in as seller {email}")
                return redirect('selladdproduct')
            if user.user_type=='SUPERADMIN':
                print("log")
                login(request,user)
                messages.success(request,f"you are  logged in as superuser {email}")
                return redirect('get')
            if user.user_type=='CUSTOMER':
                login(request,user)
                messages.success(request,f"you are  logged in as customer {email}")
                return redirect('customerlogin')
            
        else:
            print('else part')
            messages.error(request,'create you account first')
            return redirect('login')
    return render(request, 'login.html')



@login_required(login_url='login')
def getemployee(request):
    if request.method == 'POST':
        
        email = request.POST['Email']
        emp_email=employee.objects.filter(Email=email)
        if emp_email:
             messages.success(request,'this email is already exit')
             return redirect("get")
        else:
             form = EmployeeForm(request.POST)
             if form.is_valid():
    
                    form.save()
                    return redirect("get")
    else:
        get = employee.objects.all()
        form = EmployeeForm()
        
        context = {'get':get,'form':form}
        return render(request,'home.html',context)
    
@login_required(login_url='login')
def deleteemploye(request, pk):
        print("POST REQUEST\n", request)
        
        pi = employee.objects.get(pk=pk)
        print("PI DELETE REQUEST\n", pi)
        pi.delete()
        return redirect('get')

   
def register(request):
    
    return render(request,'register.html')

@login_required 
def addtocart(request,pk):
    user = request.user
    # userid= Cart.objects.get(user_id=user)
    userid= MyUser.objects.get(email=user)
    print('user',user)
    # product_id = request.GET.get('pro_id')
    # print('product_id',product_id)
    # user1 = request.uuid    
    products = Product.objects.get(product_id=pk)
    # products = Product.objects.get(product_id=request.user.id)
    # products = Product.objects.get(user=id)
    CartItem(product=products,customer=userid).save()
    return render(request,'addtocart.html')

def productview(request):
    mobiles = Product.objects.filter(category='mobile')
    laptops = Product.objects.filter(category='laptop')
    return render(request,'product.html',{'mobiles':mobiles,'laptops':laptops})    

@login_required(login_url='login')
def selleraddproductview(request):
    # print('request ', request.user)
#  if MyUser.is_authenticated:
#   User = request.POST['user']
#   emp_email=Product.objects.filter(user=user)
#   if emp_email:

    if request.method == 'POST':
        # user = request.POST.get('user')
        # title = request.POST.get('title')
        # description = request.POST.get('description')
        # price = request.POST.get('price')
        # discounted_price = request.POST.get('discounted_price')
        # image_upload = request.POST.get('image_upload')
        # file = request.POST.get('file')
        # category = request.POST.get('category')
        
        # print('request',request.POST)
        # print('request',request.POST)
        # POST_DATA = copy.deepcopy( request.POST)
    
        # form =authenticate(title=title,user=user,description=description,price=price,discounted_price=discounted_price,image_upload=image_upload,file=file,category=category)
        # POST_DATA['user'] = request.user
        # print('AHMADA ALI',POST_DATA)
       
        form=ProductForm(request.POST, request.FILES)
        print('user form\n',form)

        print('user ahmad',request.POST)
        if form.is_valid():
            print('form.is_valid()',form.is_valid())
            form.save()
            # form.user = 'admin@gmail.com'
            # form.save()
            
            print('form.save()',form.save())
            messages.success(request,'product added successfully')
            return redirect('selladdproduct')
        else:
            print('data not saved')
    get = Product.objects.filter(user_id = request.user.id)
    # get = Product.objects.all()
    form=ProductForm()   
    return render(request,'selleraddproduct.html',{"form":form,"get":get})

# def editproduct(request,id):
#     proedit = Product.objects.get(id=id)
#     form = ProductForm(request.POST or Noneinstance=proedit)
#     if request.method == 'POST':
#         if form.is_valid:
#             form.save()
#             return redirect('selladdproduct')
#     return render(request,'productedit.html',{"form":form,"proedit":proedit})


def editproduct(request,ahmad):
    proedit = Product.objects.get(pk=ahmad)
    form = ProductForm(instance=proedit)
    if request.method == 'POST':
        print('request',request)
        # if form.is_valid():
        print('valid form',form.is_valid)
        IMAGE_PATH = proedit.file.path
        print('IMAGE_PATH',IMAGE_PATH)
        if os.path.exists(IMAGE_PATH):
            print('os.path.exists(IMAGE_PATH)',os.path.exists(IMAGE_PATH))
            # os.remove(IMAGE_PATH)
            os.replace(IMAGE_PATH,IMAGE_PATH)
        form = ProductForm(request.POST ,request.FILES,instance=proedit)
        form.save()
        return redirect('selladdproduct')
    # else:
    # proedit = Product.objects.get(id=id)
    #     form = ProductForm(request.POST ,request.FILES,instance=proedit)
    #     # if request.user.is_authenticated():
    #     #     form = ProductForm(instance=proedit)
    return render(request,'productedit.html',{"form":form,"proedit":proedit})    

# def editproduct(request,id):
#     proedit = Product.objects.get(id=id)
#     form = ProductForm(instance=proedit)
#     if request.method == 'POST':
        
        
#         print('valid form',form.is_valid)
#         IMAGE_PATH = proedit.image_upload.path  
#         print('IMAGE_PATH',IMAGE_PATH)
#         if os.path.exists(IMAGE_PATH):
#             os.remove(IMAGE_PATH)
#         form = ProductForm(request.POST ,instance=proedit)
#         form.save()
#         return redirect('selladdproduct')
#     # else:
#     proedit = Product.objects.get(id=id)
#     #     form = ProductForm(request.POST ,request.FILES,instance=proedit)
#     #     # if request.user.is_authenticated():
#     #     #     form = ProductForm(instance=proedit)
#     return render(request,'productedit.html',{"form":form,"proedit":proedit}) 

def deleteproduct(request,pk):
    print("POST REQUEST\n", request)

    pi=Product.objects.get(pk=pk,user=request.user)
    if pi.image_upload:
        pi.image_upload.delete()
        pi.file.delete()
    
    pi.delete()
    return redirect('selladdproduct')
    
    
    
# def deleteproduct(request,pk):
    
#     try:
#         forms = ProductForm(request.POST or None ,instance=proedit)
#         if request.method == 'POST':
#             if forms.is_valid:
#                 forms.save()
#     except:
#         proedit=Product.objects.get(pk=pk)
#         proedit.delete()
#         return redirect('selladdproduct')
#     return render(request,'productedit.html',{"forms":forms,"proedit":proedit})
 
def sellregister(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        if 'seller_button' in request.POST:
            muser=MyUser.objects.create_user(email=email,password=password,contact=contact)
            muser.user_type='SELLER'
            
            muser.save()
            messages.success(request,f'you are register with {email} as a SELLER')
            return redirect('login')
        if 'customer_button' in request.POST:
            muser =MyUser.objects.create_user(email=email,password=password,contact=contact)
            muser.user_type = 'CUSTOMER'
            
            muser.save()
            messages.success(request,f'you are register with {email} as a CUSTOMER')
            return redirect('login')
        
    return render(request,'sellregister.html')

@login_required
def wishlist(request,id):
    user_id= MyUser.objects.get(email=request.user)
    product_id = Product.objects.get(pk=id)
    try:

        # myuser = Wishlist.objects.get(customer=user_id)

        wishlist = Wishlist.objects.get(item=product_id, customer=user_id)
        # new_wishlist = (myuser,wishlist)
        # if new_wishlist:
        #     new_wishlist.delete()
        if  wishlist:
           wishlist.delete()
            
    except Wishlist.DoesNotExist:
        muser = Wishlist.objects.create(customer=user_id,item=product_id)
    return redirect('product')    
    
@login_required
def Wish(request):
    # item  = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishlist=Wishlist.objects.all()
    
    context = {
        'wishlist':wishlist
    }
    return render(request,'wishlist.html',context)

def Deletewishlist(request,pk):
    pi=Wishlist.objects.get(pk=pk,user=request.user)
    pi.delete()
    return redirect('Wish')

def seller_view(request):
    return render(request, 'sellerslogin.html')

def customer_view(request):
    return render(request, 'customerlogin.html')


# class WishCreate(CreateView):
#     model = Wishlist
#     fields = ['items']
    
# def form_valid(self,form):
#     obj =form.save(commit=False)
#     obj.customer = self.request.user
#     obj.save()
#     return HttpResponseRedirect(self.get_success_url())

# class WishDelete(DeleteView):
#     model = Wishlist
#     success_url = reverse_lazy('wish-list')
    
# class WishList(ListView):
#     model = Wishlist
# def get_queryset(self):
#     return Wishlist.objects.filter(customer=self.request.user)
    

# def loggin(request):
#     if request.method == 'POST':

#             # username=request.POST.get('username') # username used in html   input name="username"
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#             # username = form.cleaned_data['username'] if use form then using clean data 
#             # password = form.cleaned_data['password']
#         user =authenticate(password=password,email=email )
#         if user:
#             print("log")
#             login(request,user)
#             messages.success(request,f"you are  logged in as {email}")
#             return redirect('get')
#         else:
#             print('else part')
#             messages.error(request,'create you account first')
#             return redirect('login')
#     return render(request, 'login.html')
 
    
# def postemployee(request):
#     form = EmployeeForm(request.POST)
#     if form.is_valid():
#         # data = employee(Firstname=request.POST['Firstname'],Lastname=request.POST['Lastname'],Email=request.POST['Email'],City=request.POST['City'],Salary=request.POST['Salary'])
#         form.save()
#         return redirect("home")
        
#     return render(request,'home.html',{'form':form})


# def wishlist(request,id):
    
#     user_id = MyUser.objects.get(email=request.user)
#     product_id = Product.objects.get(id=id)
    
#     muser = Wishlist.objects.create(customer=user_id,item=product_id)
#     # print('muser.item.description\n', muser.item.description)
#     # muser.item.category='mobile'
  

#     print('muser.save()\n', muser.save())
#     return redirect('product')

# def register(request):
#      if request.method == 'POST':
#          form=RegistrationForm(request.POST)
#          if form.is_valid():
#              form.save()
            
#              messages.success(request,'registration form submit')
#              return redirect('get')
#          messages.error(request,'invalid please check it again')
#      form = RegistrationForm()
#      return render(request,'register.html',{"form":form})
 
# def sellregister(request):
#     if request.method == 'POST':
#         # username = request.post.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         contact = request.POST.get('contact')
#         user =authenticate(password=password,email=email,confirm_password=confirm_password,contact=contact )
#         if user:
            
#             messages.success(request,f"you are  register as {email}")
#             return redirect('get')
#     return render(request,'sellregister.html')

# def register(request):
#     if 'customer_button' in request.POST:
#         email =request.POST.get('email')
#         password=request.POST.get('password')
#         contact = request.POST.get('contact')
#         myuser = MyUser.objects.create_user(email=email,password=password,contact=contact)
#         myuser.user_type = 'CUSTOMER'
#         myuser.save()
#         messages.success(request,f"you are  register as customer for {email}")
#         return redirect('login')    
#     return render(request,'register.html')