from django.shortcuts import render,redirect,get_object_or_404

from .models import Docente
from .forms import DocenteForm
# Create your views here.
def inicio(request):
    docentes=Docente.objects.all()
    context= {
        'docentes':docentes
    }
    return render(request,'docentes/inicio.html',context) # con esto le mande al templetes 

def create_docente(request):
    if request.method=="POST":
        docente_form=DocenteForm(request.POST)
        if docente_form.is_valid():
            docente_form.save()
            return redirect('inicio')
    else:
        docente_form=DocenteForm()
    return render(request,'docentes/create.html',{'docente_form':docente_form})
def update_docente(request,id):
    docente=get_object_or_404(Docente,id=id)
    if request.method=='POST':
        docente_form=DocenteForm(request.POST,instance=docente)
        if docente_form.is_valid():
            docente_form.save()
            return redirect('inicio')
    else:
        docente_form=DocenteForm()
    return render(request,'docentes/editar.html',{'docente_form':docente_form})

def delete_docente(request,id):
    docente=get_object_or_404(Docente,id=id)
    if docente:
        docente.delete()
        return redirect('inicio')