from django.forms import ModelForm 
from ControlSilabico.models import *
class DocenteForm(ModelForm):
    class Meta:
        model=Docente
        fields=["iddocente","nombrecompleto","correo","idcategoria",]