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
	user_ins = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	user_alt = models.ForeignKey(Usuario,related_name='products_user_alt',null=True, blank=True)
	nm_produto = models.CharField(max_length=255)
	valor_produto =  models.DecimalField(decimal_places=2,max_digits=7)
	dt_cadastro = models.DateField(blank=True)
	dt_termino = models.DateField(null=True, blank=True)
	photo = models.ImageField(upload_to='products',null=True, blank=True)

class Kart(models.Model):
	produto = models.ForeignKey('Products', on_delete=models.CASCADE)
	user_ins = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	user_alt = models.ForeignKey(Usuario,related_name='kart_user_alt',null=True, blank=True)
	qtd = models.IntegerField(default=0)
	valor_produto =  models.DecimalField(decimal_places=2,max_digits=7)
	dt_cadastro = models.DateField(blank=True)
	dt_termino = models.DateField(null=True, blank=True)

class Order(models.Model):
	kart = models.ForeignKey('Kart', on_delete=models.CASCADE)
	user_ins = models.ForeignKey('Usuario', on_delete=models.CASCADE)
	user_alt = models.ForeignKey(Usuario,related_name='order_user_alt',null=True, blank=True)
	dt_cadastro = models.DateField(blank=True)
	dt_termino = models.DateField(null=True, blank=True)

