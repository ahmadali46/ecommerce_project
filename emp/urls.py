from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [  
     
     path('password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
          name='password_reset'),
     
     path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
          name='password_reset_done'),
     
     path('password-reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
     
     path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
          name='password_reset_complete'),

     path('add/',views.add,name='home'),
     
     path('delete/<int:pk>/',views.deleteemploye,name='delete'),     
     
     path('get/',views.getemployee,name='get'),  
     
     path('edit/<int:id>/',views.editemployee,name='edit'),
     
     path('register/',views.register,name = 'register'),
     
     path('sellregister/',views.sellregister,name = 'sellregister'),
     
     path("login/",views.loggin,name='login'),
     
     path("customerlogin/",views.customer_view,name='customerlogin'),
     
     path("sellerlogin/",views.seller_view,name='sellerslogin'),
     
     path('start/',views.start,name='start'),
     
     path('logout/',views.logout,name='logout'),
     
     path('about/',views.about,name='about'),
     
     path('',views.productview, name = 'product'),
     
     path('editproduct/<slug:ahmad>/',views.editproduct,name='editproduct'),
     
     path('selladdproduct/',views.selleraddproductview, name = 'selladdproduct'),
     
     path('deleteproduct/<slug:pk>',views.deleteproduct,name='deleteproduct'),
     
     path('add_to_wishlist/<slug:id>',views.wishlist,name='add_to_wishlist'),
    
     path('wishlist/',views.Wish,name='Wish'),

     path('add_to_cart/<str:pk>',views.addtocart,name='add_to_cart')
     
     # path('deleteproduct/<int:pk>',views.deleteproduct,name='deleteproduct'),
     
     
     

     
     
     
     
     
       
        
    #path('home/',views.home,name='home'),
        
    ]  + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()