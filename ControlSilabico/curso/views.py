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
    conn = pymysql.connect(host='localhost', user='root', password='', database='dbsilabos', charset='utf8mb4')
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
            print('CURSO CURSO CURSOS',CursoDetalleO)
            CursoDetalleFilter=Cursodetalle.objects.filter(idcurso_id=idcurso)
<<<<<<< HEAD
            tamanio=len(CursoDetalleFilter)


            contexto={'consultas':result1,'CursoDetalleO':CursoDetalleO,'CursoDetFilter':CursoDetalleFilter,'tamanio':tamanio}
=======
            contexto={'consultas':result1,'CursoDetalleO':CursoDetalleO,'CursoDetFilter':CursoDetalleFilter}
            print(CursoDetalleO.carrera)
>>>>>>> 629018a5480522218cb4868e4c26ea3ddcdddad0
            #shared =CursoDetalleO.objects.filter(id_idcurso=idc'CursoDetalleO':CursoDetalleOurso)
    return render(request,'curso/Detalle_Curso/Listar_Detalle.html',contexto)
# errores con la siguiente funcion
'''
def crear_horario(request,idcurso):
    print('+++++++++++crear_horario')
    #curso_detalle1=Cursodetalle.objects.get(idcurso=idcurso)
    if(request.method == 'POST'):
        #cursoDetalle_form=CursoDetallForm(request.POST)
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
'''
def crear_detalle(request,idcurso):
    print('+++++++++++crear_horario')
    #curso_detalle1=Cursodetalle.objects.get(idcurso=idcurso)
    if(request.method == 'POST'):
        #cursoDetalle_form=CursoDetallForm(data)
        cursoDetalle_form=CursoDetallForm(request.POST)
        if cursoDetalle_form.is_valid():
            cursoDetalle_form.save()
            #return redirect('listar_carga')
            return redirect('Detalle_Curso',idcurso)
            #return render(request,'curso/Detalle_Curso/Listar_Detalle.html')
    else:
        cursoDetalle_form=CursoDetallForm()
    #RecuCurso=Curso.objects.get(idcurso=idcurso)
    return render(request,'curso/Detalle_Curso/Crear_Detalle.html',{'cursoDetalle_form':cursoDetalle_form})
''' 
def crear_horario(request,idcurso,idcursodetalle):
    print('+++++++++++crear_horario')
    #curso_detalle1=Cursodetalle.objects.get(idcurso=idcurso)
    #idhorario','ht','hp','idd','hrinicio','hrfin','aula','idcursodetalle'
    
    #horario=Horario.objects.get(idcursodetalle=idcursodetalle)
    if(request.method == 'POST'):
        #cursoDetalle_form=CursoDetallForm(data)
        #cursoHorario_form=horarioForm(initial={'idcursodetalle':idcursodetalle})
        data={'idhorario':'','ht':'','hp':'','idd':'','hrinicio':'','hrfin':'','aula':'','idcursodetalle':idcursodetalle}
        cursoHorario_form=horarioForm(request.POST or None,initial=data)
        
        if cursoHorario_form.is_valid():
            cursoHorario_form.save()
            #return redirect('listar_carga')
            return redirect('Detalle_Curso',idcurso)
            #return render(request,'curso/Detalle_Curso/Listar_Detalle.html')
    else:
        cursoHorario_form=horarioForm()
    #RecuCurso=Curso.objects.get(idcurso=idcurso)
    return render(request,'curso/Detalle_Curso/Crear_Horario.html',{'cursoHorario_form':cursoHorario_form,'idcursodetalle':idcursodetalle})
'''

def crear_horario(request,idcurso,idcursodetalle):
    initial_data={'idhorario':'','ht':'','hp':'','idd':'','hrinicio':'','hrfin':'','aula':'','idcursodetalle':idcursodetalle}
    
    
    cursoHorario_form=horarioForm(request.POST or None,initial=initial_data)
    if cursoHorario_form.is_valid():
        cursoHorario_form.save()
        return redirect('Detalle_Curso',idcurso)
    cursoHorario_form={'cursoHorario_form':cursoHorario_form}   
   
    #return render(request,'curso/Detalle_Curso/Crear_Horario.html',{'cursoHorario_form':cursoHorario_form,'idcursodetalle':idcursodetalle})
    return render(request,'curso/Detalle_Curso/Crear_Horario.html',cursoHorario_form)



   
    

#def eliminar_detalle_curso(request,id)
'''
# su reemplazo

def crear_horario(request,idcurso):
    curso_detalle_form=None
    error=None
    try:
        curso_detalle1=Cursodetalle.objects.get(idcurso=idcurso)
        if request.method == 'GET':
            curso_detalle_form=CursoDetallForm(instance=curso_detalle1)
        else:
            curso_detalle_form=CursoDetallForm(request.POST,instance=curso_detalle1)  
            if curso_detalle_form.is_valid():
                curso_detalle_form.save()  
            return redirect('listar_docente')
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'docentes/create.html',{'docente_form':curso_detalle_form,"error":error})
        
'''  
    



'''
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
#-----------------------horios-curso------------------------------
def mostrarNomCod(request,code):
    if request.method == 'GET':
            cursoHD=curso.objects.get(code=code)
            shared =CursosHorarios.objects.filter(id_curso_id=code)
    return render(request,'curso/CursoHorario/horarios_curso.html',context={'cursoHD':cursoHD,'shared':shared})
'''