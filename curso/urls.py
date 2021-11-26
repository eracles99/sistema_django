from django.urls import path,re_path
from curso.views import crearCurso, listarCurso,editarCurso,eliminarCurso
urlpatterns = [
    path('crear_curso/',crearCurso,name='crear_curso'),
    path('listar_curso/',listarCurso,name='listar_curso'),
    path('editar_curso/<str:code>',editarCurso,name='editar_curso'),
    path('eliminar_curso/<str:code>',eliminarCurso,name='eliminar_curso'),
]
