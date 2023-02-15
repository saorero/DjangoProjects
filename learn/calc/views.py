from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #The name can be from any place to make it dynamic 
    return render(request, 'home.html', {'name': 'Navin'})

def add(request):
#num1 and num2 are from the home html which are rendered in results
    val1 = request.POST['num1'] 
    val2 = request.POST['num2'] 
    res = int(val1) + int(val2)       
    return render(request, 'results.html' , {'result' : res})