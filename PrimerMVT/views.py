from http.client import HTTPResponse
from mailbox import NoSuchMailboxError
from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Context, Template, loader

def familia(request):
    
    familia=Familia(nombre="Hector", apellido="Valdez",edad=15,fechanac="1990-12-1")
    familia.save()
    familia_1=Familia(nombre="Raul", apellido="Guitos",edad=40,fechanac="1975-4-9")
    familia_1.save
    familia_2=Familia(nombre="Micaela", apellido="Cubito",edad=35,fechanac="1923-7-12")
    familia_2.save
    
    
    lista_fechanac=[familia.fechanac,familia_1.fechanac,familia_2.fechanac]
    lista_nombres=[familia.nombre,familia_1.nombre,familia_2.nombre]
    lista_apellidos=[familia.apellido,familia_1.apellido,familia_2.apellido]
    lista_edades=[familia.edad,familia_1.edad,familia_2.edad]
    diccionario={"nombre":familia.nombre,"apellido":familia.apellido,"edad":familia.edad,
    "nombre_1":familia_1.nombre,"apellido_1":familia_1.apellido,"edad_1":familia_1.edad,
    "nombre_2":familia_2.nombre,"apellido_2":familia_2.apellido,"edad_2":familia_2.edad,
    "listanombres":lista_nombres,"listaapellidos":lista_apellidos,"listaedades":lista_edades,"listanac":lista_fechanac,"fechanac":familia.fechanac
    ,"fechanac_1":familia_1.fechanac,"fechanac_2":familia_2.fechanac
    
    }
    
    plantilla=loader.get_template("template1.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)


