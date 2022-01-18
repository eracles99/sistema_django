from django.forms import ModelForm 
from ControlSilabico.models import *
class ResgistrarDocenteForm(ModelForm):
    class Meta:
        model=Users
        fields=["iduser","nombre","contrasenia","tipo","iddocente"]