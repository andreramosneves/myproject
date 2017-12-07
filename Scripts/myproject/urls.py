"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from mvc import views

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^teste/' , views.HomePageView.as_view()),
#   url(r'^UserPageView/' , views.UsuarioPageView.as_view()),
#   url(r'^login' , views.HomePageView.index, name='index'),
   url(r'^registrar' , views.HomePageView.registrar, name='registrar'),
   url(r'^kart' , views.HomePageView.kart, name='kart'),
   url(r'^order' , views.HomePageView.order, name='order'),
   url(r'^products' , views.HomePageView.products, name='products'),
   url(r'^home' , views.HomePageView.home, name='home'),
   url(r'^logout', views.HomePageView.logout, name='logout'),
   url(r'^login', views.HomePageView.login, name='login'),

] 