from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='nueva_noticia/')

    def __str__(self):
        return self.titulo


class InicioSesion(models.Model):
	usuario = models.CharField(max_length=15)
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.usuario