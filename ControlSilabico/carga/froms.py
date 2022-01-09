from django import forms
from django.forms import ModelForm 
from django.db.models import fields
from ControlSilabico.models import*

class cargaForm(forms.ModelForm):
    class Meta:
        model=Carga
        fields=['idcarga','iddocente','idhorario']
        
'''class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()#'''