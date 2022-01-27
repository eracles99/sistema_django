from django.urls import path
from . import views
from ControlSilabico.login.views  import *
from django.conf.urls.static import static
from django.conf  import settings
urlpatterns = [
    path('',iniciar, name='iniciar_sesion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)