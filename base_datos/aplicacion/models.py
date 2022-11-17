from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

# Create your models here.
class Usuario(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    empleado = models.BooleanField(default=False)
    class Meta: 
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        db_table = "usuario"
        ordering = ['-id']

class Pais(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    clave = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    class Meta: 
        verbose_name = "pais"
        verbose_name_plural = "paises"
        db_table = "pais"
        ordering = ['-id']

class Ciudad(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    clave = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.ForeignKey(Pais,  related_name='+', on_delete=models.CASCADE)
    class Meta: 
        verbose_name = "ciudad"
        verbose_name_plural = "ciudades"
        db_table = "ciudad"
        ordering = ['-id']

class AereoPuerto(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    ciudad = models.ForeignKey(Ciudad, related_name='+', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=255)
    class Meta: 
        verbose_name = "aereoPuerto"
        verbose_name_plural = "aereoPuertos"
        db_table = "aereoPuerto"
        ordering = ['-id']

class Piloto(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    edad = models.IntegerField(default=22)
    experiencia = models.CharField(max_length=255)
    total_vuelos = models.IntegerField(default=0)
    class Meta: 
        verbose_name = "piloto"
        verbose_name_plural = "pilotos"
        db_table = "piloto"
        ordering = ['-id']

class Avion(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    folio = models.CharField(max_length=14)
    cap_max_pasajeros = models.IntegerField(default=0)
    cap_max_equipaje_kilos = models.FloatField(default=0)
    escalas = models.BooleanField(default=False)
    salida = models.DateField(auto_now_add=True)
    llegada = models.DateField(auto_now_add=True)
    filas = models.IntegerField(default=0)
    columnas = models.IntegerField(default=0)
    estado = models.CharField(max_length=255)
    origen_id = models.ForeignKey(AereoPuerto,  related_name='+', on_delete=models.CASCADE)
    destino_id = models.ForeignKey(AereoPuerto,  related_name='+', on_delete=models.CASCADE)
    piloto = models.ForeignKey(Piloto, related_name='+', on_delete=models.CASCADE)
    class Meta: 
        verbose_name = "avion"
        verbose_name_plural = "aviones"
        db_table = "avion"
        ordering = ['-id']

class Escalas(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    avion = models.ForeignKey(Avion, related_name='+', on_delete=models.CASCADE)
    aereoPuerto = models.ForeignKey(AereoPuerto,  related_name='+', on_delete=models.CASCADE)
    salida = models.DateField(auto_now_add=True)
    llegada = models.DateField(auto_now_add=True)
    class Meta: 
        verbose_name = "escala"
        verbose_name_plural = "escalas"
        db_table = "escala"
        ordering = ['-id']

class Asiento(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    fila = models.CharField(max_length=1)
    columna= models.CharField(max_length=1)
    primera_clase = models.BooleanField(default=False)
    Asiento = models.CharField(max_length=10)
    disponible = models.BooleanField(default=False)
    avion = models.ForeignKey(Avion, related_name='+', on_delete=models.CASCADE)
    costo = models.FloatField(default=0)
    class Meta: 
        verbose_name = "asiento"
        verbose_name_plural = "asientos"
        db_table = "asiento"
        ordering = ['-id']

class Equipaje(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    asiento = models.ForeignKey(Asiento, related_name='+', on_delete=models.CASCADE)
    peso_total = models.FloatField(default=0)
    costo_extra = models.FloatField(default=0)
    consecutivo = models.IntegerField(default=0)
    class Meta: 
        verbose_name = "equipaje"
        verbose_name_plural = "equipajes"
        db_table = "equipaje"
        ordering = ['-id']

class Boleto(SafeDeleteModel):
    _safe_delete_policy = SOFT_DELETE_CASCADE
    id = models.BigAutoField(primary_key=True)
    asiento = models.ForeignKey(Asiento, related_name='+', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='+', on_delete=models.CASCADE)
    folio= models.CharField(max_length=14)
    fecha_hora_compra = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    total = models.FloatField(default=0)
    class Meta: 
        verbose_name = "boleto"
        verbose_name_plural = "boletos"
        db_table = "boleto"
        ordering = ['-id']