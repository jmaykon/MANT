from django.shortcuts import render
from apps.users.decorators import role_required  # ✅ importar desde users

@role_required(roles=["admin", "usuario","tecnico"])
def agenda_list(request):
    return render(request, "agenda/agenda_list.html")