# apps/mantenimiento/views.py

from django.shortcuts import render, redirect
from apps.users.decorators import role_required  # ✅ importar desde users
from apps.mantenimiento.models import Ticket
@role_required(roles=["admin", "tecnico","usuario"])
def mante_list(request):
    return render(request, "mantenimiento/mante_list.html")

@role_required(roles=["admin", "tecnico","usuario"])
def mante_detalle(request):
    return render(request, "mantenimiento/mante_detalle.html")

@role_required(roles=["admin", "tecnico","usuario"])
def mante_cronograma(request):
    return render(request, "mantenimiento/mante_cronograma.html")

@role_required(roles=["admin","usuario"])
def mante_solicitar(request):
    if request.method == "POST":
        tipo = request.POST.get("tipo")
        descripcion = request.POST.get("descripcion")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")

        # Crear el ticket
        Ticket.objects.create(
            tipo=tipo,
            descripcion=descripcion,
            fecha_inicio_t=fecha_inicio if fecha_inicio else None,
            fecha_fin_t=fecha_fin if fecha_fin else None,
            estado_ticket="PENDIENTE"
        )
        if role_required =="admin":
            return redirect('dashboard:admin')
        else:
            return redirect('dashboard:usuario') 
        # Si usas HTMX, solo devuelve una parte del HTML
        
    # Si es GET, muestra el formulario
    return render(request, "mantenimiento/mante_solicitar.html")