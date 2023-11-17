from django.urls import path
from django.http import HttpResponse

def view_inicio(request):
    return HttpResponse("Hola mundo")

urlpatterns = [
    path('inicio/', view_inicio),
]
