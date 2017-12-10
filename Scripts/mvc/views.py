from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.base import View

from django.template.loader import render_to_string

from django.template import Context, Template

import time

from datetime import date

from mvc.models import *

from django.conf import settings

from django.core.files.storage import FileSystemStorage



# Create your views here.
class HomePageView(View):

	def registrar(request):
		if(request.method == "POST"):
			usr = Usuario.objects.filter(usuario=request.POST.get('user'))
			if len(usr) != 0:
				msg = "Usuário já cadastrado!!"
				return render(request,'registrar.html', {'message' : msg})
			else:
				msg = "Usuário inserido com sucesso!!"
				usuario = Usuario(usuario=request.POST.get('user'),senha=request.POST.get('pwd'),dt_cadastro=date.today().isoformat())
				usuario.save()
				return render(request,'registrar.html', {'message' : msg})
		return render(request,'registrar.html',)
	def kart(request):
		if(request.method == "POST"):
			msg = "Adicionado no carrinho!!"
			return render(request,'kart.html',{'message': msg})
		return render(request,'kart.html',)
	def order(request):
	    return render(request,'order.html',)
	
	def products(request):
		list_product = Products.objects.filter(dt_termino__isnull=True)
		try:
			user =  Usuario.objects.get(pk=request.session['user_id'])
		except KeyError:
			return render(request,'products.html',{'message' : 'Usuário deve estar logado!!'})
		if(request.method == "POST"):
			msg = "Produto cadastrado com sucesso!!"
			try:
				product = Products(nm_produto=request.POST['n_product'],valor_produto=request.POST['v_product'],
					photo=request.FILES['i_product'] ,user_ins=user,dt_cadastro=date.today().isoformat())
			except:
				product = Products(nm_produto=request.POST['n_product'],valor_produto=request.POST['v_product']
					,user_ins=user,dt_cadastro=date.today().isoformat())
			product.save()
			list_product = Products.objects.filter(dt_termino__isnull=True)
			return render(request,'products.html',{'message': msg, 'list_product' : list_product})
		if(request.method == "GET" and request.GET.get('id') is not None):
			msg = "Produto finalizado com sucesso!!"
			product = Products.objects.get(pk=request.GET['id'])
			product.dt_termino = date.today().isoformat()
			product.user_alt = user
			product.save()
			list_product = Products.objects.filter(dt_termino__isnull=True)
			return render(request,'products.html',{'message': msg, 'list_product' : list_product})
		return render(request,'products.html',{'list_product': list_product})


	def home(request):
		list_product = Products.objects.filter(dt_termino__isnull=True)
		return render(request,'home.html',{'list_product': list_product})
	def login(request):
		if(request.method == "POST"):
			try:
				del request.session['user_id']
				del request.session['user_name']
			except KeyError:
				pass
			usuario = Usuario.objects.filter(usuario=request.POST.get('user'),senha=request.POST.get('psw'))
			if len(usuario) == 0:
				msg = "Usuário Inválido!"
				return render(request,'login.html',{'message': msg})
			else: #criar sessao
				request.session['user_id'] = usuario[0].id
				request.session['user_name'] = usuario[0].usuario
				return home(request);
		return render(request,'login.html',)

	def logout(request):
	    try:
	        del request.session['user_id']
	        del request.session['user_name']
	    except KeyError:
	        pass
	    return render(request,'home.html',)
