from django.urls import path
from . import views

app_name = 'equipo'

urlpatterns = [
    path('lista/', views.lista_equipos, name='lista_equipos'),
    path('agregar-lugar/', views.agregar_lugar, name='agregar_lugar'),
    
]

