from django.urls import path
from . import  views

urlpatterns = [
    #A function home that is a function in views
    path('', views.home, name= 'home'),
    path('add', views.add, name= 'add')
   
]
