from django.shortcuts import render , redirect

from .models import Familiar , Curso , Estudiante

from .forms import FamiliarForm , CursoForm , EstudianteForm

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def saludo(request):
    return HttpResponse('hola mundo')

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            nuevo_curso = Familiar(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                edad=form.cleaned_data['edad'],
                fecha_nacimiento = form.cleaned_data['fecha_nacimiento'],
                parentesco = form.cleaned_data['parentesco']
            )
            nuevo_curso.save()
            return redirect('inicio')
            
            
    
    else:
        form = FamiliarForm()
        return render(request, 'mi_primer_app/crear_familiar.html', {'form':form})
        
  
    
    
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = CursoForm()
        
    return render(request, 'mi_primer_app/crear_curso.html', {'form': form})    
   
        
        
def crear_estudiante(request): 
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nuevo_curso = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_curso.save()
            return redirect('inicio')
            
            
    
    else:
        form = EstudianteForm()
        return render(request, 'mi_primer_app/crear_estudiante.html', {'form':form})

    

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})
    
    
def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre','')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos':cursos, 'nombre':nombre})
     