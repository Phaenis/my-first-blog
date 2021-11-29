from django.shortcuts import render
from .models import Tessiu
import math as mate

# Crea las vistas de aqui.

# El template_name sirve para
# ------------------------------------------------------------------------------------
# Funcion principal
template_name = "home/index.html"


def home(request):
    L = Tessiu.objects.get_queryset()
    lista_Procesada = procesalista(L)
    resultado = extraeGrafo(L)
    diccionario = {'lista': L, 'Lista2': lista_Procesada, 'resul': resultado}
    return render(request, template_name, diccionario)
# ------------------------------------------------------------------------------------
# Funcion del Umbral


def procesalista(lista):
    lista1 = []
    for elemento in lista:
        Norma = (elemento.Temperatura**2) + \
            (elemento.inflammation**2)+(elemento.Color**2)
        p = Norma**0.5
        if p > 50:
            lista1.append(p)
    return lista1
# ------------------------------------------------------------------------------------
# Funcion Generar Grafo


def extraeGrafo(list):
    distancia = []
    for i in list:
        registros = []
        for j in list:
            dist = mate.sqrt(((i.Temperatura-j.Temperatura)**2) +
                             ((i.Color-j.Color)**2)+((i.inflammation-j.inflammation)**2))
            registros.append(dist)
        distancia.append(registros)
    print(distancia)
    return distancia
# ------------------------------------------------------------------------------------
