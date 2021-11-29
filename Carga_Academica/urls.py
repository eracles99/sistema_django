from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCargaAcademica/', views.registrarCargaAcademica,name='registrarCargaAcademica'),
    path('edicionCargaAcademica/<Codigo>', views.edicionCargaAcademica),
    path('editarCargaAcademica/', views.editarCargaAcademica),
    path('eliminarCargaAcademica/<Codigo>', views.eliminarCargaAcademica)
]