from django.db import models

# Create your models here.


class Usuario(models.Model):
	#Id = models.IntField(max_length=11)
	usuario = models.CharField(max_length=255)
	senha = models.CharField(max_length=255)
	dt_cadastro = models.DateField(blank=True)
	dt_termino = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.usuario	
