from django.shortcuts import render, redirect
from .forms import LugarForm
from .models import Lugar
from apps.users.decorators import role_required
from django.utils import timezone

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
        
        # Retorna la tabla actualizada solo con activos
        lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)
        return render(request, 'lugar/partials/lugar_table.html', {'lugares': lugares})

    return redirect('lugar:lista_lugares')


@role_required(roles=["admin", "tecnico"])
def editar_lugar(request, id):
    lugar = get_object_or_404(Lugar, id_lugar=id)
    if request.method == "POST":
        lugar.nombre = request.POST.get("nombre")
        lugar.direccion = request.POST.get("direccion")
        lugar.area = request.POST.get("area")
        lugar.ciudad = request.POST.get("ciudad")
        lugar.save()
        lugares = Lugar.objects.filter(fecha_eliminacion__isnull=True)
        return render(request, "lugar/lugar_table.html", {"lugares": lugares})
    return render(request, "lugar/editar_form_inline.html", {"lugar": lugar})








