from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from .froms import cursoForm,cursohForm
from .models import curso,CursosHorarios
def Home(request):
    return render(request,'index.html')
def crearCurso(request):
    if request.method=='POST':
        curso_form=cursoForm(request.POST)
        if curso_form.is_valid():
            curso_form.save()
            return redirect('listar_curso') 
    else:
        curso_form=cursoForm()
    return render(request,'curso/crear_curso.html',{'curso_form':curso_form})
def listarCurso(request):
    cursos=curso.objects.all()
    return render(request,'curso/listar_curso.html',{'cursos':cursos})

def editarCurso(request,code):
    curso_form=None
    error=None
    try:
        curso1=curso.objects.get(code=code)
        if request.method == 'GET':
            curso_form=cursoForm(instance=curso1)
        else:
            curso_form=cursoForm(request.POST,instance=curso1)  
            if curso_form.is_valid():
                curso_form.save()  
            return redirect('listar_curso') 
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'curso/crear_curso.html',{'curso_form':curso_form,"error":error})
def eliminarCurso(request,code):
    curso1=curso.objects.get(code=code)
    curso1.delete()
    return redirect('listar_curso')
#-------------------------------funciones cursos-horarios--------------------------------
def listarCursoH(request):
    cursosH=CursosHorarios.objects.all()
    return render(request,'curso/cursoHorario/listar_cursoH.html',{'cursosH':cursosH})
def crearCursoH(request):
    if request.method=='POST':
        cursoH_form=cursohForm(request.POST)
        if cursoH_form.is_valid():
            cursoH_form.save()
            return redirect('listar_cursoh') 
    else:
        cursoH_form=cursohForm()
    return render(request,'curso/cursoHorario/crear_cursoH.html',{'cursoH_form':cursoH_form})

def editarCursoH(request,id):
    cursoH_form=None
    error=None
    try:
        cursoH=CursosHorarios.objects.get(id=id)
        if request.method == 'GET':
            cursoH_form=cursohForm(instance=cursoH)
        else:
            cursoH_form=cursohForm(request.POST,instance=cursoH)  
            if cursoH_form.is_valid():
                cursoH_form.save()  
            return redirect('listar_cursoh') 
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'curso/cursoHorario/crear_cursoH.html',{'cursoH_form':cursoH_form,"error":error})
def eliminarCursoH(request,id):
    curso1=CursosHorarios.objects.get(id=id)
    curso1.delete()
    return redirect('listar_cursoh')