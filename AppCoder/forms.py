from django import forms
from .models import *



    
    
    
    
class estudianteForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
    
    
class profesorForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    
    
class cursoForm(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class entregableForm(forms.Form):
    nombre = forms.CharField()
    fecha = forms.DateField()
    enviado = forms.BooleanField(required=  False)
  