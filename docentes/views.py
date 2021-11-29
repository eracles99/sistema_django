from django.shortcuts import render,redirect,get_object_or_404
from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from .models import Docente
from .forms import DocenteForm
# Create your views here.
def inicio(request):
    docentes=Docente.objects.all()
    return render(request,'docentes/inicio.html',{'docentes':docentes}) # con esto le mande al templetes 

def create_docente(request):
    if request.method=="POST":
        docente_form=DocenteForm(request.POST)
        if docente_form.is_valid():
            docente_form.save()
            return redirect('inicio')
    else:
        docente_form=DocenteForm()
    return render(request,'docentes/create.html',{'docente_form':docente_form})
def update_docente(request,code):
    docente_form=None
    error=None
    try:
        docente1=Docente.objects.get(code=code)
        if request.method == 'GET':
            docente_form=DocenteForm(instance=docente1)
        else:
            docente_form=DocenteForm(request.POST,instance=docente1)  
            if docente_form.is_valid():
                docente_form.save()  
            return redirect('listar_curso')
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'docentes/create.html',{'docente_form':docente_form,"error":error})

def delete_docente(request,code):
    docente=get_object_or_404(Docente,code=code)
    if docente:
        docente.delete()
        return redirect('inicio')