from django.contrib import admin
from .models import Car

class CarShow(admin.ModelAdmin):
    
    list_display = ('nom' , 'modele', 'colour', 'description')
    search_fields = ["nom"] 

admin.site.register(Car,CarShow)

# Register your models here.
