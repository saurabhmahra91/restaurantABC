from django.shortcuts import render

from django.shortcuts import get_object_or_404 #
from django.http import HttpResponse  #
from django.http import HttpResponseRedirect  #
from django.http import Http404  #
from django.urls import reverse 


# Create your views here.

def items_list(request):
    context = {
        'nearby_restaurant' :  
    }
