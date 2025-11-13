


from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from .models import Lugar
from .forms import LugarForm
from apps.users.decorators import role_required


@role_required(roles=["admin", "tecnico"])
def lugar_view(request):
    # Solo los activos
    lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)
    return render(request, 'lugar/lugar_list.html', {'lugares': lugares})


@role_required(roles=["admin", "tecnico"]) 
def lista_lugares(request):
    try:
        # Solo los activos
        lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)
    except Exception as e:
        print("Error al consultar lugares:", e)
        lugares = []
    
    return render(request, 'lugar/lugar_list.html', {'lugares': lugares})


@role_required(roles=["admin", "tecnico"])
def agregar_lugares(request):
    if request.method == 'POST':
        form = LugarForm(request.POST)
        if form.is_valid():
            lugar = form.save(commit=False)
            lugar.creado_por = request.user.username
            lugar.save()

            # Solo los activos
            lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)

            if request.headers.get('HX-Request'):
                return render(request, 'lugar/partials/lugar_table.html', {'lugares': lugares})

            return redirect('lugar:lista_lugares')

    else:
        form = LugarForm()
    
    # Solo los activos
    lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)
    if request.headers.get('HX-Request'):
        return render(request, 'lugar/partials/lugar_table.html', {'lugares': lugares})
    
    return render(request, 'lugar/lugar_list.html', {'form': form, 'lugares': lugares})


@role_required(roles=["admin", "tecnico"])
def eliminar_lugar(request, id):
    if request.method == "DELETE" and request.headers.get('HX-Request'):
        try:
            lugar = Lugar.objects.get(id_lugar=id)
            lugar.fecha_eliminacion = timezone.now()  # marca como eliminado
            lugar.eliminado_por = request.user.username
            lugar.save()
        except Lugar.DoesNotExist:
            pass
        
        lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)
        return render(request, 'lugar/partials/lugar_table.html', {'lugares': lugares})

    return redirect('lugar:lista_lugares')


@role_required(roles=["admin", "tecnico"])
def editar_lugar(request, id):
    lugar = get_object_or_404(Lugar, id_lugar=id)

    # CARGAR DATOS EN EL MODAL
    if request.method == "GET" and request.headers.get("HX-Request"):
        form = LugarForm(instance=lugar)
        return render(request, "lugar/partials/lugar_edit_form.html", {"form": form, "lugar": lugar})

    # GUARDAR CAMBIOS
    if request.method == "POST":
        form = LugarForm(request.POST, instance=lugar)
        if form.is_valid():
            lugar = form.save(commit=False)
            lugar.modificado_por = request.user.username
            lugar.save()

            # Traer solo los lugares activos para recargar la tabla
            lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)

            if request.headers.get("HX-Request"):
                return render(request, "lugar/partials/lugar_table.html", {"lugares": lugares})

            return redirect("lugar:lista_lugares")

    return redirect("lugar:lista_lugares")






