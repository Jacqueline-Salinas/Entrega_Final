from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/', views.inicio_view),
    path('cursos/', views.cursos_view),
]
