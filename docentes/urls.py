# he creado esta url para mi app
from django.urls import path
from . import views

urlpatterns = [
    path('tododocentes/', views.inicio, name='inicio'),
    path('creardocente/', views.create_docente, name='create'),
    path('update_<int:id>/',views.update_docente,name='update'),
    path('delete_<int:id>/',views.delete_docente,name='delete'),
    
]