from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import LoginForm

# -------------------- LOGIN --------------------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirigir según rol
            if user.role == 'admin':
                return redirect('dashboard:admin')
            elif user.role == 'tecnico':
                return redirect('dashboard:tecnico')
            elif user.role == 'usuario':
                return redirect('dashboard:usuario')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# -------------------- PERFIL --------------------
@login_required
def perfil_users(request):
    return render(request, 'users/perfil.html')

# -------------------- EDITAR PERFIL --------------------
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, '✅ Perfil actualizado correctamente.')
        return redirect('users:perfil_users')
    else:
        return render(request, 'users/editar_perfil.html')

# -------------------- CAMBIAR CONTRASEÑA --------------------
@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '🔒 Contraseña actualizada correctamente.')
            return redirect('users:perfil_users')
        else:
            messages.error(request, '⚠ Error al cambiar la contraseña. Verifique los campos.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/cambiar_password.html', {'form': form})

# -------------------- LOGOUT --------------------
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, '👋 Sesión cerrada correctamente.')
    return redirect('users:login')
