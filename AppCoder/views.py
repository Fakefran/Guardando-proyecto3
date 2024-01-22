from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from django.core.exceptions import ValidationError
from AppCoder.forms import *




#Inicio:

def inicio(request): 
    return render(request,"AppCoder/inicio.html")





#Vista de estudiantes:

def estudiante(request):
    
    if request.method == "POST":
    
        est1 = estudianteForm(request.POST)
          
        if est1.is_valid():
            
            info = est1.cleaned_data
            
            
            NuevoEstudiante = Estudiante(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
        
            
            NuevoEstudiante.save()
                
            return render(request,"AppCoder/inicio.html")

    else:
        
        est1 = estudianteForm()

    return render(request, "AppCoder/estudiante.html", {"est2": est1} )




#Vista de profesores:

def profesor(request):
    
    if request.method == "POST":
    
        pro1 = profesorForm(request.POST)
          
        if pro1.is_valid():
            
            info = pro1.cleaned_data
            
            NuevoProfesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
            
            NuevoProfesor.save()
           
        return render(request,"Appcoder/inicio.html")
    
    else:
        
        pro1 = profesorForm()
        
    return render(request, "AppCoder/profesores.html", {"pro2" : pro1})





#Esta es la vista del curso :

def curso(request):
    
    
    if request.method == "POST":
    
        cur1 = cursoForm(request.POST)
          
        if cur1.is_valid():
            
            info = cur1.cleaned_data
            
            nuevo_curso = Curso(nombre=info["nombre"], camada=info["camada"])
            
            nuevo_curso.save()
            
            
           
            
        return render(request,"Appcoder/inicio.html")
    
    else:
        
        cur1 = cursoForm()
        
    return render(request, "AppCoder/cursos.html", {"cur2" : cur1})






#Esta es la vista de los entregables:

def entregable(request):
    
    
    if request.method == "POST":
    
        ent1 = entregableForm(request.POST)
          
        if ent1.is_valid():
            
            info = ent1.cleaned_data
            
            NuevoEntregable = Entregable(nombre=info["nombre"], fechaEntrega=info["fecha"])
            
            NuevoEntregable.save()
            
            
           
            
        return render(request,"Appcoder/inicio.html")
    
    else:
        
        ent1 = entregableForm()
        
    return render(request, "AppCoder/entregables.html", {"ent2" : ent1})




#Busqueda de informacion

def BuscarInfo(request):
    
    return render(request,"AppCoder/BuscarInfo.html")


def Resultado(request):
    
    
    if request.GET["camada"]:
        
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains = camada)
      
        return render(request, "AppCoder/resultados.html", {"cursos":cursos, "camada": camada } )
    
    else:
        
        respuesta = "No enviaste datos."
        
    return HttpResponse(respuesta)

    

        