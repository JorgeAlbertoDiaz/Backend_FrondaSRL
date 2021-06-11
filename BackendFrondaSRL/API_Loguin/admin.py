from django.contrib import admin
from .models import Empresa, Niveles_Usuario, Permiso_Usuario, Sucursales, Usuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Permiso_Usuario)
admin.site.register(Sucursales)
admin.site.register(Niveles_Usuario)