from django.shortcuts import render,redirect,get_object_or_404
from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from ControlSilabico.curso.froms import CursoDetallForm
from ControlSilabico.models import *
from ControlSilabico.carga.froms import *
# Create your views here.
from django.db.models.query import InstanceCheckMeta

from django.db.models import Q
from django.db import connection
def listar_carga(request):
    cursor=connection.cursor()
    try:
        cursor.execute('select * from vcargadocente')
        resultado=cursor.fetchall()
        print(resultado)
        return render(request,'carga/inicio.html',{'carga':resultado}) # con esto le mande al templetes
    finally:
        cursor.close()
def listar_cursos(request):
    cursor=connection.cursor()
    try:
        cursor.execute('select * from vcursosdisponibles')
        resultado=cursor.fetchall()
        print(resultado)
        return render(request,'carga/cursos_disponibles.html',{'cursosd':resultado}) # con esto le mande al templetes
    finally:
        cursor.close()
def asignar_cargafail(request,idCursoDetalle):
    #carga1= Cursodetalle.objects.filter(idcursodetalle=idCursoDetalle).first()
    print("************************",idCursoDetalle)

    return render(request,'carga/generar_carga.html',{'CursoDetalle':idCursoDetalle})
def asignando(request,idCursoDetalle):
    codeDetalle=idCursoDetalle
    codeDocente=request.POST['txtCodigo']

    #print("==========",codeDetalle,codeDocente)

    carga=Carga.objects.create(iddocente=codeDocente , idcursodetalle=codeDetalle)
    return render(request,'carga/generar_carga.html')

def asignar_carga(request,idCursoDetalle):
    print('****************',idCursoDetalle)
    carga_form=None
    error=None
    try:
        if request.method=='POST':
            carga_form = cargaForm(initial={'idCursoDetalle': idCursoDetalle})
            carga_form=cargaForm(request.POST)
            if carga_form.is_valid():
                carga_form.save()
                return redirect('listar_curso') 
        else:
            carga_form=cargaForm()
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'carga/generar_carga.html',{'carga_form':carga_form})