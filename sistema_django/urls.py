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
#from sistema_django.views import Home

from django.urls.conf import include

from curso.views import Home
from docentes.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/',Home.as_view(), name='home'),
<<<<<<< HEAD 
    path('home/',Home,name='home'),
    path('curso/',include('curso.urls'),name='curso'),
    path('docentes/',include('docentes.urls'),name='docentes'),
=======
    path('',Home,name='home'),
    path('curso/',include('curso.urls'),name='curso')
>>>>>>> papicha
    
]
