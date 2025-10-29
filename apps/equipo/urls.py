from django.urls import path
from . import views

app_name = 'equipo'

urlpatterns = [
    path('lista/', views.lista_equipos, name='equipo_list'),
]
