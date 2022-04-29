from django.contrib import admin
from .models import Car
from django.utils.safestring import mark_safe

class CarShow(admin.ModelAdmin):
    
    list_display = ('nom', 'modele', 'colour', 'description', 'image')
    list_display_links = ('image','nom')
    search_fields = ["nom"] 
    
    def images_views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')  
    
admin.site.register(Car,CarShow)


        

# Register your models here.
