from django.db import models
import datetime
from django.utils import timezone 

# Create your models here.

class FoodItem(models.Model):

    
    price = models.FloatField()
    name = models.CharField(max_length=500)
    rating = models.DecimalField()
    



    def __repr__(self):
        return f'{self.pk}.> {self.name}'

    def __str__(self):
        return f'{self.pk}.> {self.name}'

