from django.urls import path

from ControlSilabico.curso.views import *

urlpatterns=[
    path('crear_curso/',crearCurso,name='crear_curso'),
    path('listar_curso/',listarCurso,name='listar_curso'),
    path('editar_curso/<str:idcurso>',editarCurso,name='editar_curso'),
    path('eliminar_curso/<str:idcurso>',eliminarCurso,name='eliminar_curso'),
    #----------------------------Detalle cursos----------------------
    path('Detalle_Curso/<str:idcurso>',Detalle_Curso,name='Detalle_Curso'),
    path('crear_detalle/<str:idcurso>',crear_detalle,name='crear_detalle'),
    path('crear_horario/<str:idcurso>/<str:idcursodetalle>',crear_horario,name='crear_horario'),
]
