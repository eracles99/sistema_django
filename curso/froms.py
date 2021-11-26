from django import forms
from .models import curso
class cursoForm(forms.ModelForm):
    
    class Meta:
        model = curso
        fields = ["code","name","credits","carrera","grupo"]
