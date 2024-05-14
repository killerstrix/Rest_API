from django.urls import path
from .views import (
    index,
    Nosotros,
    Contacto,
)

urlpatterns = [
    path("", index, name="index"),
    path("Nosotros", Nosotros, name="Nosotros"),
    path("Contacto", Contacto, name="Contacto"),
]
