from django.shortcuts import render
from apps.users.decorators import role_required
from .models import Equipo

@role_required(roles=["admin","tecnico"])
def lista_equipos(request):
    try:
        equipos = Equipo.objects.select_related('idPersona', 'idUbicacion').all()
    except Exception as e:
        print("Error al consultar equipos:", e)
        equipos = []
    return render(request, 'equipo/equipo_list.html', {'equipos': equipos})
