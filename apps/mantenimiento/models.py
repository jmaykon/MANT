from django.db import models
from django.conf import settings
from apps.lugar.models import Lugar
from apps.equipo.models import Equipo
from django.utils import timezone

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True, db_column='id_ticket')
    id_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, db_column='id')
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_equipo')
    
    id_lugar = models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_lugar')
    fecha_inicio_t = models.DateTimeField(null=True, blank=True, db_column='fecha_inicio_t')
    fecha_fin_t = models.DateTimeField(null=True, blank=True, db_column='fecha_fin_t')
    estado_ticket = models.CharField(max_length=20, default='Pendiente', db_column='estado_ticket')
    motivo_cancelacion = models.CharField(max_length=300, blank=True, null=True, db_column='motivo_cancelacion')
    fecha_cancelacion = models.DateTimeField(null=True, blank=True, db_column='fecha_cancelacion')
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='fecha_modificacion')
    fecha_eliminacion = models.DateTimeField(null=True, blank=True, db_column='fecha_eliminacion')

    creado_por = models.CharField(max_length=50, blank=True, null=True, db_column='creado_por')
    modificado_por = models.CharField(max_length=50, blank=True, null=True, db_column='modificado_por')
    eliminado_por = models.CharField(max_length=50, blank=True, null=True, db_column='eliminado_por')

    class Meta:
        db_table = 'Ticket'

    def __str__(self):
        return f"Ticket {self.id_ticket} - {self.estado_ticket}"

class ReporteMantenimiento(models.Model):
    id_reporte = models.AutoField(primary_key=True, db_column='id_reporte')
    id_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, db_column='id_ticket')
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_equipo')
    
    id_elaborado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='elaborados', db_column='id_elaborado_por')
    id_aprobado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='aprobados', db_column='id_aprobado_por')
    id_lugar = models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_lugar')
    fecha_mantenimiento = models.DateTimeField(null=True, blank=True, db_column='fecha_mantenimiento')
    descripcion = models.CharField(max_length=300, blank=True, null=True, db_column='descripcion')
    observaciones = models.CharField(max_length=300, blank=True, null=True, db_column='observaciones')
    firma_tecnico = models.CharField(max_length=100, blank=True, null=True, db_column='firma_tecnico')
    firma_responsable = models.CharField(max_length=100, blank=True, null=True, db_column='firma_responsable')
    fecha_envio = models.DateTimeField(null=True, blank=True, db_column='fecha_envio')
    fecha_aprobacion = models.DateTimeField(default=timezone.now)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='fecha_modificacion')
    fecha_eliminacion = models.DateTimeField(null=True, blank=True, db_column='fecha_eliminacion')

    creado_por = models.CharField(max_length=50, blank=True, null=True, db_column='creado_por')
    modificado_por = models.CharField(max_length=50, blank=True, null=True, db_column='modificado_por')
    eliminado_por = models.CharField(max_length=50, blank=True, null=True, db_column='eliminado_por')


    class Meta:
        db_table = 'Reporte_Mantenimiento'

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    id_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_users')
    id_ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, blank=True, db_column = 'id_ticket')
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, null=True, blank=True, db_column = 'id_equipo')
    id_lugar = models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, db_column = 'id_lugar')
    descripcion = models.CharField(max_length=300, blank=True, null=True, db_column='descripcion')
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    fecha_modificacion = models.DateTimeField(auto_now=True, db_column='fecha_modificacion')
    fecha_eliminacion = models.DateTimeField(null=True, blank=True, db_column='fecha_eliminacion')

    creado_por = models.CharField(max_length=50, blank=True, null=True, db_column='creado_por')
    modificado_por = models.CharField(max_length=50, blank=True, null=True, db_column='modificado_por')
    eliminado_por = models.CharField(max_length=50, blank=True, null=True, db_column='eliminado_por')


    class Meta:
        db_table = 'Notificacion'
