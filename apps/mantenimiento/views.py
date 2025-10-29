# apps/mantenimiento/views.py
from django.shortcuts import render
from apps.users.decorators import role_required  # ✅ importar desde users

@role_required(roles=["admin", "tecnico","usuario"])
def mante_list(request):
    return render(request, "mantenimiento/mante_list.html")

@role_required(roles=["admin", "tecnico","usuario"])
def mante_detalle(request):
    return render(request, "mantenimiento/mante_detalle.html")

@role_required(roles=["admin", "tecnico","usuario"])
def mante_cronograma(request):
    return render(request, "mantenimiento/mante_cronograma.html")

@role_required(roles=["admin", "tecnico","usuario"])
def mante_solicitar(request):
    return render(request, "mantenimiento/mante_solicitar.html")
