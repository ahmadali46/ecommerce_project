from django.urls import path
from . import views

urlpatterns = [
    path('sellerregister/',views.sellerregister,name='sellerregister'),
    path("sellerlogin/",views.sellerlogin,name='sellerlogin'),
    path('sellerhome/',views.sellerhome,name='sellerhome'),
    path('connection/',views.formView, name = 'loginsell'),
    
]
