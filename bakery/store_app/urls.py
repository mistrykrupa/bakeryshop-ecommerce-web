from django.urls import path
#from . import views
from .views import *
from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import ( 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView 
)


urlpatterns = [
   
    path('',base,name='base'),
    path('',hf,name='hf'),
    path('item/', item, name='item'),
    path('category/',category,name='category'),
    path('home/', home, name='home'),
    path('gallary/', gallary, name='gallary'),
    path('about/', about, name='about'),
    path('contact/', Contact_Page, name='contact'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),

    path('search/',search,name='search'),
    path('search/<str:id>',product_details,name='product_details'),
    path('item/<str:id>',product_details,name='product_details'),
    #path('submit/<int:id>',submit_review,name=submit_review),
    #path('submit_review/<int:item_id>', submit_review, name='submit_review'),
    #path('view_reviews/<int:item_id>/', view_reviews, name='view_reviews'),
    path('add_review/<int:id>',add_review, name='add_review'),
    
    path('wishlist/add/<int:item_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),

    # for cart
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_detail,name='cart_detail'),
    

    path('cart/checkout/', Check_out, name='checkout'),
    path('cart/checkout/placeorder', Place_Order, name='place_order'),
    path('success/',success,name='success'),
    path('cart/cart_view/',cart_view,name='cart_view'),
    # path('cart/checkout/cart_view/',checkout_view,name='checkout_view'),

    path('Your_Order', Your_Order, name='your_order'),
    path('generateinvoice/<int:order_id>/', generate_invoice, name = 'generateinvoice'),
    #for profile

    # path('profile/', profile, name='profile'),
    # path('edit/', profile_edit, name='edit'),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # for forgot password

    #path('forgotpassword/', forgotpassword, name='forgotpassword'),
    #path('ChangePassword/', Change_Password, name='ChangePassword'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='forgot/forgotpassword.html'),name='password_reset'), 
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='forgot/pass_reset_done.html'),name='password_reset_done'), 
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='forgot/confirm_password.html'),name='password_reset_confirm'), 
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='forgot/pass_reset_complete.html'),name='password_reset_complete'),


]
