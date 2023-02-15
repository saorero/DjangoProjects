from django.db import models

# Create your models here.
#a class that holds 5 objects
class podcast(models.Model):
    
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    episodes = models.IntegerField()
    offer =  models.BooleanField(default=False)