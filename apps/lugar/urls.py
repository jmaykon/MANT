from django.urls import path
from . import views

app_name = 'lugar'

urlpatterns = [
    
    path('', views.lugar_view, name='lugar_view'),
    path('lista/', views.lista_lugares, name='lista_lugares'),
    path('agregar_lugares/', views.agregar_lugares, name='agregar_lugares'),
    path('eliminar/<int:id>/', views.eliminar_lugar, name='eliminar_lugar'),
    path('editar/<int:id>/', views.editar_lugar, name='editar_lugar'),

    

    
    



    
]
