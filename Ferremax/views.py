from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "core/index.html")


def Nosotros(request):
    return render(request, "core/Nosotros.html")


def Contacto(request):
    return render(request, "core/Contacto.html")
