from django import forms
from . import models

class PhotoForm(forms.ModelForm):       
    class Meta:
       model = models.Car        
       fields = '__all__'