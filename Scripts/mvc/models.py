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

class Products(models.Model):
	nm_produto = models.CharField(max_length=255)
	valor_produto =  models.DecimalField(decimal_places=2,max_digits=7)
	photo = models.ImageField(upload_to='products')

class Kart(models.Model):
	produto = models.ForeignKey('Products', on_delete=models.CASCADE)
	qtd = models.IntegerField(default=0)
	valor_produto =  models.DecimalField(decimal_places=2,max_digits=7)
	dt_cadastro = models.DateField(blank=True)
	dt_termino = models.DateField(null=True, blank=True)

class Order(models.Model):
	kart = models.ForeignKey('Kart', on_delete=models.CASCADE)
	dt_cadastro = models.DateField(blank=True)
	dt_termino = models.DateField(null=True, blank=True)

