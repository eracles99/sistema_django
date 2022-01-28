from django.urls import path
from . import views
from ControlSilabico.carga.views  import *
from django.conf.urls.static import static
from django.conf  import settings
urlpatterns = [
    path('listarcarga/',listar_carga, name='listar_carga'),
    path('listarcursosdisponibles/', views.listar_cursos, name='listar_cursosdisponibles'),
    path('asignar/<int:idCursoDetalle>',views.asignar_carga,name='asignar'),
    path('asignando/<int:idCursoDetalle>',views.asignando,name='asignando'),
    #path('asignar/<str:idcursodetalle>',views.asignar_carga,name='asignar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)