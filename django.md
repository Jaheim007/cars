- models.py

# Champs obligatoires (Convention de NaN) après chaque models
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

# nom du models dans l'admin
    class Meta():
        verbose_name = 'nom'
        verbose_name_plural = 'nom au pluriel'

- admin.py 


- @admin.register(models)
- class modelsAdmin(admin.ModelAdmin):
# Liste des champs a afficher
    list_display = ('images_view', 'title', 'date_add', 'date_update', 'status')
    list_display_links = ('images_view', 'title')

# Configuration du champ de recherche
    search_fields = ('title', )

# Permet d'avoir un aperçu des images

- from django.utils.safestring import mark_safe

def images_view(self, obj): 
    return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')

# Titre de l'onglet dans l'admin
    images_view.short_description = 'Aperçu des images'  




# exemple

- models.py

from django.db import models

class Python(models.Model)
    name = models.CharField(max_length=255)
    version = models.IntegerField()
    picture = models.FileField()

    class Meta():
        verbose_name = 'python'
        verbose_name_plural = 'pythons'


- admin.py

from django.utils.safestring import mark_safe
from . import models


@admin.register(models.Python)
class PythonAdmin(admin.ModelAdmin):

    list_display = ('images_view', 'name', 'date_add', 'date_update', 'status')

    def images_view(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')
