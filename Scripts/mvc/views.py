from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.base import View

from django.template.loader import render_to_string

from django.template import Context, Template

import time

from datetime import date

from mvc.models import Usuario



# Create your views here.
class HomePageView(View):
	def dispatch(request, *args, **kwargs):
		now = datetime.datetime.now()
		t = Template('''
            	<!DOCTYPE html>
                <html lang="pt-br">
                <head>
                    <title>Meu template</title>
                    <meta charset="utf-8"/>
                </head>
                    <body>
                        <p>Meu nome é {{ name }}</p>
                        <p>Agora são: {{ current_date }}.</p>
                    </body>
                </html>
            ''')
		html = t.render(Context({'current_date': now,
                                 'name': 'André Ramos Neves'
                                 }))
		return HttpResponse(html)

	def registrar(request):
		if(request.method == "POST"):
			usr = Usuario.objects.filter(usuario=request.POST.get('user'))
			if len(usr) != 0:
				msg = "Usuário já cadastrado!!"
				return render(request,'registrar.html', {'message' : msg})
			else:
				usuario = Usuario(usuario=request.POST.get('user'),senha=request.POST.get('pwd'),dt_cadastro=date.today().isoformat())
				usuario.save()
		return render(request,'registrar.html',)
	def kart(request):
	    return render(request,'kart.html',)
	def order(request):
	    return render(request,'order.html',)
	def products(request):
	    return render(request,'products.html',)
	def home(request):
	    return render(request,'home.html',)
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
				msg = request.session['user_name']
				return render(request,'home.html',{'message' : msg})
		return render(request,'login.html',)

	def logout(request):
	    try:
	        del request.session['user_id']
	        del request.session['user_name']
	    except KeyError:
	        pass
	    return render(request,'home.html',)



