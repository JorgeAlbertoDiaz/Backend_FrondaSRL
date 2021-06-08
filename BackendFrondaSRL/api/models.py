from django.db import models
from django.db.models.fields import AutoField

class Usuario(models.Model):
   id_usuario = models.AutoField(primary_key = True)
   nombre_usuario = models.CharField('Nombre de Usuario', max_length=100)
   password = models.CharField('Password',max_length=100)

#    def __str__(self):
#        return '{0},{1}'.format(self.nombre_usuario, self.password