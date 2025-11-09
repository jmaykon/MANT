from .models import Equipo
from .models import Lugar
from .models import Componente
from django.shortcuts import render, redirect
from .forms import LugarForm
from django.utils import timezone
from apps.users.decorators import role_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


@role_required(roles=["admin","tecnico"])
def lista_equipos(request):
    try:
        equipos = Equipo.objects.select_related('id_lugar', 'id_users').all()
        componentes = Componente.objects.select_related('id_equipo').all() 
    except Exception as e:
        print("Error al consultar equipos:", e)
    return render(request, 'equipo/equipo_list.html', {'equipos': equipos,'componentes': componentes})


@role_required(roles=["admin","tecnico"])
def agregar_lugar(request):
    try:
        if request.method == 'POST':
            form = LugarForm(request.POST)
            if form.is_valid():
                lugar = form.save(commit=False)
                lugar.creado_por = request.user
                lugar.modificado_por = request.user
                lugar.fecha_creacion = timezone.now()
                lugar.fecha_modificacion = timezone.now()
                lugar.save()

                # Retorna solo el fragmento para HTMX
                lugares = Lugar.objects.all()
                return render(request, 'equipo/equipo_list_partial.html', {'lugares': lugares})

        else:
            form = LugarForm()
    except Exception as e:
        print("Error al consultar lugares:", e)
    return render(request, 'equipo/agregar_lugar.html', {'form': form})




