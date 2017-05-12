# from django.http import HttpResponse
from django.shortcuts import render
from .models import Restaurant, Food

# Create your views here.

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    
    return render(request, 'restaurants/index.django.html', context)
