from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

# Create your views here.

def hello(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('This is my first django application')
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
  
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
  
]
