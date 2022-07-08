from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Request: Sirve para realizar peticiones
# HTTPResponse: Para enviar la respuesta usando el protocolo HTTPS.

# Esto es una vista: 

def inicio(request):
	print(request.user)
	return render(request, "Doctor.html", {})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			message.success(request, f'Usuario {username} creado')
	else:
		form = UserCreationForm()

	context = {'form' : form }

	return render(request, 'register.html', context)

def hija1(request):
	return render(request, "P1.html", {})

def contacto(request):
	return render(request, "contacto.html", {})

def acerca(request):
	return render(request, "acerca.html", {})

def hija2(request):
	return render(request, "P2.html", {})

def login(request):
	return render(request, "login.html", {})

