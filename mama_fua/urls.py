"""Defines Urls for full_belly_project"""


from django.urls import path
from . import views

app_name = 'mama_fua'

urlpatterns = [

    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('cloth_details/', views.cloth_details, name='cloth_details'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('history/', views.history, name='history'),
    path('cart/', views.cart, name='cart'),
    path('create_order/', views.create_order, name='create_order'),

]
