from django.shortcuts import render
from django.http import HttpResponse
from .models import podcast


# Create your views here.
def pod(request):
    """
    
WHEN THERE WAS NO DATABASE
    podcast1 = podcast() #our class name is podcast in models so instantiate
    podcast2 = podcast()
    podcast3 = podcast()
    

    podcast1.name = 'Technology'
    podcast1.episodes = 59
    podcast1.img = 'topics\woman-practicing-yoga-mat-home.jpg'
    podcast1.offer = False

    podcast2.name = 'Publishing'
    podcast2.episodes = 200
    podcast2.img = 'topics\physician-consulting-his-patient-clinic.jpg'
    podcast2.offer = True
    
    podcast3.name = 'Gaming'
    podcast3.episodes = 519
    podcast3.img = 'topics\delicious-meal-with-sambal-arrangement.jpg'
    podcast3.offer = False
    
    pods = [podcast1, podcast2, podcast3 ]

    """
#DATABASE PRESENT podcast is model

    pods = podcast.objects.all()

    
    return render(request, 'podtalk.html', {'pods': pods} )