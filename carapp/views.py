from django.shortcuts import render, get_object_or_404
from .models import Car

def index(request): 
    store = Car.objects.all()
    return render(request,'html_car/index.html',context={'store_cars':store} )

def main(request, id): 
    store = Car.objects.get(id = id)
    return render(request, 'html_car/amin.html', context={'store':store})

# Create your views here.
