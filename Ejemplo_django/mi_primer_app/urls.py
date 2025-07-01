from django.urls import path

from .views import saludo

urlpatterns = [
    path('Hola mundo/', saludo),
]
