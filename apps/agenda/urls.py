from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path("agenda/", views.agenda_list, name="agenda_list"),
]
