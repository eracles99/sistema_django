from django.urls import path,re_path
from curso.views import crearCurso, editarCursoH, listarCurso,editarCurso,eliminarCurso,listarCursoH,crearCursoH,eliminarCursoH,mostrarNomCod
urlpatterns = [
    path('crear_curso/',crearCurso,name='crear_curso'),
    path('listar_curso/',listarCurso,name='listar_curso'),
    path('editar_curso/<str:code>',editarCurso,name='editar_curso'),
    path('eliminar_curso/<str:code>',eliminarCurso,name='eliminar_curso'),
    #----------------------------horarios cursos----------------------
    path('listar_cursoh/',listarCursoH,name='listar_cursoh'),
    path('crear_cursoh/',crearCursoH,name='crear_cursoh'),
    
    path('editar_cursoh/<int:id>',editarCursoH,name='editar_cursoh'),
    path('eliminar_cursoh/<int:id>',eliminarCursoH,name='eliminar_cursoh'),
    
    #--------------------------horario -curso---------------------------
    path('mostrarNomCod/<str:code>',mostrarNomCod,name='mostrarNomCod')
    
]
