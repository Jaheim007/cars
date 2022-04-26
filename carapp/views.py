from django.shortcuts import render

def index(request):     
    return render(request,'html_car/index.html',)

def main(request):      
    return render(request, 'html_car/amin.html', )

# Create your views here.
