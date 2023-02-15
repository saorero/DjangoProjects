from django.urls import path
from . import  views

urlpatterns = [
   
    path('', views.pod, name= 'pod'),
   
]
