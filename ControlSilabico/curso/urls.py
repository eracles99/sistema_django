from django.urls import path

from ControlSilabico.curso.views import *
urlpatterns=[
    path('crear_curso/',crearCurso,name='crear_curso'),
    path('listar_curso/',listarCurso,name='listar_curso'),
    path('editar_curso/<str:codeC>',editarCurso,name='editar_curso'),
    path('eliminar_curso/<str:codeC>',eliminarCurso,name='eliminar_curso'),
    #----------------------------horarios cursos----------------------
]
