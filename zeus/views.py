#from django.http import HttpResponse
from django.shortcuts import render
from .models import comidas

# Create your views here.

def home(request):
	comidaslistadas = comidas.objects.all()
	return render(request, "gestioncomidas.html", {"comidas": comidaslistadas})

	#return HttpResponse("<h1> --> Hola Mundo! <-- </h1>")