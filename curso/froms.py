from django import forms
from django.db.models import fields
from .models import curso,CursosHorarios
class cursoForm(forms.ModelForm):
    
    class Meta:
        model = curso
        fields = ["code","name","credits","carrera","grupo"]
class cursohForm(forms.ModelForm):
    
    class Meta:
        model = CursosHorarios
        fields = ['tipo','ht','hp','day','hr_i','hr_f','matriculados','semestre','id_curso']
