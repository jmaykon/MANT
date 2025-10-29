from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls', namespace='users')),  # login raíz
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('users/', include('apps.users.urls')),
    
    path("mantenimiento/", include("apps.mantenimiento.urls", namespace="mantenimiento")),
    path("agenda/", include("apps.agenda.urls", namespace="agenda")),
    path("equipo/", include("apps.equipo.urls", namespace="equipo")),
]
