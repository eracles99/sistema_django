from django.shortcuts import render, redirect
from .models import CargaAcademica
from django.contrib import messages

# Create your views here.


def home(request):
    CargasAcademicasListados = CargaAcademica.objects.all()
    messages.success(request, '¡Cargas Academicas listados!')
    return render(request, "carga_academica/gestionCargaAcademica.html", {"CargaAcademica": CargasAcademicasListados})


def registrarCargaAcademica(request):
    Codigo = request.POST['txtCodigo']
    Carrera = request.POST['txtCarrera']
    Docente = request.POST['txtDocente']
    Creditos = request.POST['numCreditos']
    Tipo = request.POST['txtTipo']
    Gpo = request.POST['txtGpo']
    Ht = request.POST['txtHt']
    Hp = request.POST['txtHp']
    Dia = request.POST['txtDia']
    Horario_I = request.POST['txtHorario_I']
    Horario_F = request.POST['txtHorario_F']
    Aula = request.POST['txtAula']
    Matriculados = request.POST['txtMatriculados']

    cargaAcademica = CargaAcademica.objects.create(
        Codigo=Codigo, Carrera=Carrera, Docente=Docente, Creditos=Creditos, Tipo=Tipo, Gpo=Gpo, Ht=Ht, Hp=Hp, Dia=Dia, Horario_I=Horario_I,Horario_F=Horario_F, Aula=Aula, Matriculados=Matriculados)
    messages.success(request, '¡Carga Academica registrado!')
    return redirect('/')


def edicionCargaAcademica(request, Codigo):
    cargaAcademica = CargaAcademica.objects.get(Codigo=Codigo)
    return render(request, "carga_academica/edicionCargaAcademica.html", {"cargaAcademica": cargaAcademica})


def editarCargaAcademica(request):
    Codigo = request.POST['txtCodigo']
    Carrera = request.POST['txtCarrera']
    Docente = request.POST['txtDocente']
    Creditos = request.POST['numCreditos']
    Tipo = request.POST['txtTipo']
    Gpo = request.POST['txtGpo']
    Ht = request.POST['txtHt']
    Hp = request.POST['txtHp']
    Dia = request.POST['txtDia']
    Horario_I = request.POST['txtHorario_I']
    Horario_F = request.POST['txtHorario_F']
    Aula = request.POST['txtAula']
    Matriculados = request.POST['txtMatriculados']

    cargaAcademica = CargaAcademica.objects.get(Codigo=Codigo)
    cargaAcademica.Carrera = Carrera
    cargaAcademica.Docente = Docente
    cargaAcademica.Creditos = Creditos
    cargaAcademica.Tipo =Tipo
    cargaAcademica.Gpo =Gpo
    cargaAcademica.Ht =Ht
    cargaAcademica.Hp = Hp
    cargaAcademica.Dia = Dia
    cargaAcademica.Horario_I = Horario_I
    cargaAcademica.Horario_I = Horario_F
    cargaAcademica.Aula = Aula
    cargaAcademica.Matriculados = Matriculados
    cargaAcademica.save()

    messages.success(request, '¡Cargas Academicas actualizado!')

    return redirect('/')


def eliminarCargaAcademica(request, Codigo):
    cargaAcademica = CargaAcademica.objects.get(Codigo=Codigo)
    cargaAcademica.delete()

    messages.success(request, '¡Carga Academica eliminado!')

    return redirect('/')