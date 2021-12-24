from django.shortcuts import render,redirect,get_object_or_404
from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from ControlSilabico.models import Docente
from .forms import DocenteForm
# Create your views here.
def listar_docente(request):
    docentes=Docente.objects.all()
    return render(request,'docentes/inicio.html',{'docentes':docentes}) # con esto le mande al templetes 

def create_docente(request):
    if request.method=="POST":
        docente_form=DocenteForm(request.POST)
        if docente_form.is_valid():
            docente_form.save()
            return redirect('listar_docente')
    else:
        docente_form=DocenteForm()
    return render(request,'docentes/create.html',{'docente_form':docente_form})
def update_docente(request,iddocente):
    docente_form=None
    error=None
    try:
        docente1=Docente.objects.get(iddocente=iddocente)
        if request.method == 'GET':
            docente_form=DocenteForm(instance=docente1)
        else:
            docente_form=DocenteForm(request.POST,instance=docente1)  
            if docente_form.is_valid():
                docente_form.save()  
            return redirect('listar_docente')
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'docentes/create.html',{'docente_form':docente_form,"error":error})

def delete_docente(request,iddocente):
    Docente1=get_object_or_404(Docente,iddocente=iddocente)
    if Docente1:
        Docente1.delete()
        return redirect('listar_docente')