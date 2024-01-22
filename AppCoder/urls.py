
from django.urls import path
from AppCoder.views import *



urlpatterns = [
    path("", inicio, name="Inicio"),
    path("profesores/", profesor, name="Profesor"),
    path("estudiantes/", estudiante, name="Estudiante"),
    path("entregables/", entregable, name="Entregable"),
    path("cursos/", curso, name="Curso"),
    path("BuscarInfo", BuscarInfo, name="BuscarInfo"),
    path("Resultado/", Resultado, name= "Buscar" ),
   


]
