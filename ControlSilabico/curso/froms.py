
from django import forms
from django.db.models import fields
from ControlSilabico.models import*

class CursoDetallForm(forms.ModelForm):
    class Meta:
        model=Cursodetalle
        fields=['idcursodetalle','idcurso','idtipocurso']
class cursoForm(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = ["idcurso","nombre","carrera","grupo","creditos","idcat_curso"]
class horarioForm(forms.ModelForm):
    class Meta:
        model=Horario
        fields=['idhorario','ht','hp','idd','hrinicio','hrfin','aula','idcursodetalle']
        
'''class M(forms.ModelForm):
    
    class Meta:
        model = deta
        fields = ['tipo','ht','hp','day','hr_i','hr_f','matriculados','semestre','id_curso']'''

