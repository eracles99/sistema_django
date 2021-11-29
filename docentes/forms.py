from django.forms import ModelForm 
from .models import Docente

class DocenteForm(ModelForm):
    class Meta:
        model=Docente
        fields='__all__'