from django.urls import path
from . import views
from ControlSilabico.usuario.views  import *
from django.conf.urls.static import static
from django.conf  import settings
urlpatterns = [
    path('crear_usuario/',asignation, name='crear_usuario'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)