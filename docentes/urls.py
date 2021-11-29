# he creado esta url para mi app
from django.urls import path
from . import views
from .views import inicio

urlpatterns = [
    path('tododocentes/',inicio, name='inicio'),
    path('creardocente/', views.create_docente, name='create'),
    path('update/<str:code>',views.update_docente,name='update'),
    path('delete/<str:code>',views.delete_docente,name='delete'),
    
]