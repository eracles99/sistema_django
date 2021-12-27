from django import forms
from django.forms import ModelForm 
from django.db.models import fields
from ControlSilabico.models import*

class cargaForm(forms.ModelForm):
    class Meta:
        model=Carga
        fields=['idcarga','iddocente','idcursodetalle']