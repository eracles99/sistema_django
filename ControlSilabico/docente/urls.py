# he creado esta url para mi app
from django.urls import path
from . import views
from ControlSilabico.docente.views  import *

urlpatterns = [
    path('tododocentes/',listar_docente, name='listar_docente'),
    path('creardocente/', views.create_docente, name='create'),
    path('update/<str:iddocente>',views.update_docente,name='update'),
    path('delete/<str:iddocente>',views.delete_docente,name='delete'),
]