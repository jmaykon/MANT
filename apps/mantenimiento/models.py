from django.db import models
from django.conf import settings


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    ubicacion = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Mantenimiento(models.Model):
    TIPO_CHOICES = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ]

    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='mantenimientos')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha_programada = models.DateField()
    fecha_realizada = models.DateField(null=True, blank=True)
    tecnico = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.equipo.nombre}"
