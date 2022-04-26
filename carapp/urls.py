
from django.urls import path 
from .import views

apps_name = 'work'

urlpatterns = [
    path('', views.index , name='index'),
    path('main', views.main, name = 'main'),
]
