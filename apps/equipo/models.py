from django.db import models

class Lugar(models.Model):
    idLugar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Lugar'
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    idPersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidop = models.CharField(max_length=50, blank=True, null=True)
    apellidom = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    idLugar = models.ForeignKey(Lugar, on_delete=models.PROTECT, db_column='idLugar')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'Persona'
    def __str__(self):
        return f"{self.nombre} {self.apellidop or ''}"


class Equipo(models.Model):
    idEquipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    aec = models.CharField(max_length=50)
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    so = models.CharField(max_length=50, blank=True, null=True)
    procesador = models.CharField(max_length=50, blank=True, null=True)
    tipoRam = models.CharField(max_length=50, blank=True, null=True)
    ram = models.CharField(max_length=50, blank=True, null=True)
    tipoDisco = models.CharField(max_length=50, blank=True, null=True)
    disco = models.CharField(max_length=50, blank=True, null=True)
    serial = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=20, default='Activo')
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    idUbicacion = models.ForeignKey(Lugar, on_delete=models.SET_NULL, null=True, blank=True, db_column='idUbicacion')
    idPersona = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True, db_column='idPersona')

    class Meta:
        db_table = 'Equipo'

    def __str__(self):
        return f"{self.tipo} - {self.marca} {self.modelo}"