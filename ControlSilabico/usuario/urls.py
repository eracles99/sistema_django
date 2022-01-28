from django.urls import path
from . import views
from ControlSilabico.usuario.views  import *
from django.conf.urls.static import static
from django.conf  import settings
urlpatterns = [
    path('crear_usuario/',asignation, name='crear_usuario'),
    path('cursos_usuario/<str:iddocente>',cursos_usuario,name='cursos_usuario'),
    path('silabo/<str:codCurso>/<str:IdDocente>/<str:carrera>/<str:semestre>',silabos,name='silabo')
    #path('crear_usuario_docente/',registrar_usuario_docente, name='crear_usuario_docente'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)