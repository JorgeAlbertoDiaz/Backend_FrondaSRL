from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Usuario(models.Model):
	usuario_nombre = models.CharField(max_length=100)
	usuario_password = models.CharField(max_length=100)

class Empresa(models.Model):
	razon_social = models.CharField(max_length=100)

class Sucursales(models.Model):
	nombre_sucursal = models.CharField(max_length=100)
	direccion_sucursal = models.CharField(max_length=200)
	empresa = models.ForeignKey(Empresa, on_delete= models.CASCADE)

class Niveles_Usuario(models.Model):
	nombre_nivel_usuario = models.CharField(max_length=100)
	descripcion_nivel_usuario = models.CharField(max_length=200)


class Acceso_Empresa(models.Model):
	fecha_hora_acceso = models.DateTimeField(auto_now_add=True, blank=True)
	mensaje_acceso = models.CharField(max_length=250)
	empresa = models.ForeignKey(Empresa, on_delete= models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
	Niveles_Usuario = models.ForeignKey(Niveles_Usuario, on_delete= models.CASCADE)

class Permiso_Usuario(models.Model):
	nombre_permiso = models.CharField(max_length=100)
	descripcion_permiso = models.CharField(max_length=200)
	nombre_modulo = models.CharField(max_length=200)
	ruta_modulo = models.CharField(max_length=200)
	listar = models.BooleanField(default = False)
	ver = models.BooleanField(default = False)
	crear = models.BooleanField(default = False)
	modificar = models.BooleanField(default = False)
	eliminar = models.BooleanField(default = False)
	
class Permiso(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE)
	permiso = models.ForeignKey(Permiso_Usuario, on_delete= models.CASCADE)