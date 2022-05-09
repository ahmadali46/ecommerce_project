# from datetime import datetime
# from urllib import response
import datetime
# from django import shortcuts
# from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
# from django.shortcuts import render_to_response
from django.views import View
from . forms import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext

def sellerregister(request):
    if request.method  == 'POST':
        form=SellerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'registration successfully done')
            return redirect('sellerregister')
        raise ValidationError('registration error')
    form = SellerRegistrationForm()
    return render(request,'sellerregister.html',{'form':form})



# def sellerlogin(request):
#     if request.method == 'POST':
#         fam = AuthenticationForm(request,data=request.POST)
#         if fam.is_valid():
#             username = fam.cleaned_data.get('username')
#             password = fam.cleaned_data.get('password')
#             user = authenticate(username=username,password=password)
#             if user:
#                 login(request,user)
#                 messages.success(request,f'you are logged in {username}')
#                 return redirect('sellerhome')
               
#         else:
#             messages.error(request,'invalid username or password')
#             return redirect('sellerlogin')
#     fam = AuthenticationForm()
#     return render(request,'sellerlogin.html',{'fam':fam})
                
                
def sellerlogin(request):
    username = 'not in logged in'
    if request.method == 'POST':
        MySellerLogin=SellerLoginForm(request.POST)
        if MySellerLogin.is_valid():
            username = MySellerLogin.cleaned_data['username']
        else:
            MySellerLogin = SellerLoginForm()
    response = render(None,'sellerlogin.html',{'username':username},RequestContext(request))
    response.set_cookie('last_connection',datetime.datetime.now())
    response.set_cookie('username', datetime.datetime.now())
    return response

def formView(request):
    if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
        username = request.COOKIES['username']
        last_connection = request.COOKIES['last_connection']
        last_connection_time = datetime.datetime.strptime(last_connection[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.datetime.now() - last_connection_time).seconds < 10:
            return render(request, 'sellerlogin.html', {"username" : username})
        else:
            return render(request, 'loginsell.html', {})
    else:
          return render(request, 'loginsell.html', {})






def sellerhome(request):
    return render(request,'sellerhome.html')
        
        
# Create your views here.
