"""sistema_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_django.views import Home
from django.conf.urls.static import static
from django.conf  import settings
from django.urls.conf import include

#from ControlSilabico.curso.views import Home
#from docentes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),    
    #path('',Home.as_view(), name='home'),
    path('',include('ControlSilabico.login.urls'),name='iniciar'),
    path('curso/',include('ControlSilabico.curso.urls'),name='curso'),
    #path('carga/', include('Carga_Academica.urls'),name='carga'),
    path('docentes/',include('ControlSilabico.docente.urls'),name='docentes'),
    path('carga/',include('ControlSilabico.carga.urls'),name='carga'),
    #path('',Home,name='home')

    path('usuario/',include('ControlSilabico.usuario.urls'),name='usuario'),
    #path('iniciar/',include('ControlSilabico.login.urls'),name='iniciar'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',Home.as_view(), name='home'),
    path('curso/',include('ControlSilabico.curso.urls'),name='curso'),
    #path('carga/', include('Carga_Academica.urls'),name='carga'),
    path('docentes/',include('ControlSilabico.docente.urls'),name='docentes'),
    path('carga/',include('ControlSilabico.carga.urls'),name='carga'),
    #path('',Home,name='home')

    path('usuario/',include('ControlSilabico.usuario.urls'),name='usuario'),
    path('iniciar/',include('ControlSilabico.login.urls'),name='iniciar'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''