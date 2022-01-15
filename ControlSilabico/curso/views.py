from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from ControlSilabico.curso.froms import *
from ControlSilabico.models import *
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy  
    
# Create your views here.

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
    cursos=Curso.objects.all()
    return render(request,'curso/listar_curso.html',{'cursos':cursos})

def editarCurso(request,idcurso):
    curso_form=None
    error=None
    try:
        curso1=Curso.objects.get(idcurso=idcurso)
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
def eliminarCurso(request,idcurso):
    curso1=Curso.objects.get(idcurso=idcurso)
    curso1.delete()
    return redirect('listar_curso')

    
#-------------------------------funciones cursos-horarios--------------------------------
def Detalle_Curso(request,idcurso):
    import  pymysql
    #from django.db import co
    conn = pymysql.connect(host='localhost', user='root', password='admin', database='dbsilabos', charset='utf8mb4')
    cur = conn.cursor()
    Args=(idcurso,)
    cur.callproc('sp_HroPorCurso',Args)
    conn.commit()
    result = cur.fetchall()
    result1=[]
    #print('{0}   {1}   {2}   {3}   {4}   {5}   {6}   {7} '.format('id', 'tipo', 'ht', 'hp','dia','hrInicio','hrFin','Aula'))
    for row in result:
        result1.append(list(row))
    conn.close()
    if request.method == 'GET':
            CursoDetalleO=Curso.objects.get(idcurso=idcurso)
            CursoDetalleFilter=Cursodetalle.objects.filter(idcurso_id=idcurso)
            contexto={'consultas':result1,'CursoDetalleO':CursoDetalleO,'CursoDetFilter':CursoDetalleFilter}
            #shared =CursoDetalleO.objects.filter(id_idcurso=idc'CursoDetalleO':CursoDetalleOurso)
    return render(request,'curso/Detalle_Curso/Listar_Detalle.html',contexto)

def crear_horario(request,idcurso):
    print('+++++++++++crear_horario')
    if(request.method == 'POST'):
        cursoDetalle_form=CursoDetallForm(request.POST)
        horario_form=horarioForm(request.POST)
        if cursoDetalle_form.is_valid() and horario_form.is_valid() :
            cursoDetalle_form.save()
            horario_form.save()
            return redirect('listar_carga')
    else:
        horario_form=horarioForm()
        cursoDetalle_form=CursoDetallForm()
    RecuCurso=Curso.objects.get(idcurso=idcurso)
    return render(request,'curso/Detalle_Curso/Crear_Horario.html',{'cursoDetalle_form':cursoDetalle_form,'horario_form':horario_form,'RecuCurso':RecuCurso})
        
        
    
    

'''def listarCursoH(request):
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
#-----------------------horios-curso------------------------------
def mostrarNomCod(request,code):
    if request.method == 'GET':
            cursoHD=curso.objects.get(code=code)
            shared =CursosHorarios.objects.filter(id_curso_id=code)
    return render(request,'curso/CursoHorario/horarios_curso.html',context={'cursoHD':cursoHD,'shared':shared})
'''