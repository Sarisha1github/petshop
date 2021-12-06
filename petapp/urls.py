from django.urls import path
from petapp import views
urlpatterns=[
path('',views.index),
path('about/',views.about),
path('contact/',views.contact),
path('gallery/',views.gallery),
path('userregister/',views.userregister),
path('shopregister/',views.shopregister),
path('petsregister/',views.petsregister),
path('viewtbl/',views.viewtbl),
path('petshome/',views.petshome),
path('petsupdate/',views.petsupdate),
path('petsedit/',views.petsedit),
path('delete/',views.delete),
path('shopupdate/',views.shopupdate),
path('shopedit/',views.shopedit),
path('userlogin/',views.user_login),
path('logout/',views.logout),
path('pets_addcart/',views.pets_addcart),
path('delete_cartitem/',views.delete_cartitem),
path('cart/',views.cart),
path('buynow/',views.buynow),
path('makepayment/',views.makepayment),
path('continue_shopping/',views.continue_shopping),
path('cancel/',views.cancel),
path('view_profile/',views.view_profile),
path('change_pswd/',views.change_pswd),
path('forget_pswd/',views.forget_pswd),
path('forgetchangepswd/',views.forgetchangepswd),


path('adminindex/',views.adminindex),
path('adminlogin/',views.admin_login),
path('adminsignup/',views.admin_signup),
path('adminlogout/',views.admin_logout),
path('pets_view/',views.pets_view),
path('users_view/',views.users_view)


]