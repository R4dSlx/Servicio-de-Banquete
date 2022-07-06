"""Proyecto_BankeT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from Proyecto_BankeT.views import hija1
from Proyecto_BankeT.views import hija2
from Proyecto_BankeT.views import index
from Proyecto_BankeT.views import register
from zeus.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hija1/', hija1),
    path('hija2/', hija2),
    path('register/', register),
    path('', LoginView.as_view(template_name='index.html')),
    path('comidas', home),

]
