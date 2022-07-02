from django.http import HttpResponse 
from django.shortcuts import render

# Request: Sirve para realizar peticiones
# HTTPResponse: Para enviar la respuesta usando el protocolo HTTPS.

# Esto es una vista: 

def hija1(request):
	return render(request, "P1.html", {})

def hija2(request):
	return render(request, "P2.html", {})

