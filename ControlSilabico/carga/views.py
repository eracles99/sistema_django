from django.shortcuts import render,redirect,get_object_or_404
from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from ControlSilabico.models import Docente
from ControlSilabico.models import Cursodetalle
from ControlSilabico.models import Carga
#from .forms import CargaForm
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
def asignar_carga(request,idCursoDetalle):
    carga1= Cursodetalle.objects.filter(idcursodetalle=idCursoDetalle).first()
    print(carga1)
    return render(request,'carga/generar_carga.html',{'CursoDetalle':carga1})
def asignando(request,idCursoDetalle):
    codeDetalle=idCursoDetalle
    codeDocente=request.POST['txtCodigo']

    carga=Carga.objects.create(iddocente=codeDocente , idcursodetalle=codeDetalle)
    return render(request,'carga/generar_carga.html')

