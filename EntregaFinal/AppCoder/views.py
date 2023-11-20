from django.shortcuts import render
from django.http import HttpResponse

def inicio_view(request):
    return HttpResponse("Hola mundo")

def cursos_view(request):
    return render(request, "AppCoder/padre.html")
