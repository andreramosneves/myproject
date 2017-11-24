from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.base import View

from django.template.loader import render_to_string

from django.template import Context, Template

import datetime



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

	def index(request):
	    return render(request,'login.html',)
	def registrar(request):
	    return render(request,'registrar.html',)
	def kart(request):
	    return render(request,'kart.html',)
	def order(request):
	    return render(request,'order.html',)
	def products(request):
	    return render(request,'products.html',)
	def home(request):
	    return render(request,'home.html',)


class UsuarioPageView(View):
	def current_datetime(request):
	    now = datetime.datetime.now()
	    html = "<html><body>It is now %s.</body></html>" % now
	    return HttpResponse(html)

