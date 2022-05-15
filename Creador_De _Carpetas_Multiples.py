#!/usr/bin/python3
from pathlib import Path
from os import system

ubicacion = Path('/home/dani/Documentos/python/') 

print(f"Este script está diseñado para crear carpetas numeradas hasta donde quieras.\nLas carpetas se immprimirán en el siguiente directorio: {ubicacion} \nVamos a crear unas cuantas carpetas!")

def elegir_rango():
    rango = input("¿Cuantas carpetas quieres crear?  ")
    rango_str = str(rango)
    rango_int = int(rango)
    return rango_str

def crear_carpetas(r):
    cuenta = 1
    # r_int= int(r)
    system('clear')
    texto= input('¿Qué texto quieres que aparezca en cada carpeta?\n Por ejemmplo: "Carpeta Número " o "Día "\n No olvides añadir un espacio al final si no quieres que el número vaya pegado al texto\n')
    while cuenta < int(r) +1:
        cuenta_str = str(cuenta) 
        nombre = str(texto) + cuenta_str
        ruta_creacion = Path(ubicacion , nombre)
        Path.mkdir(ruta_creacion)
        cuenta += 1
    print(f"Carpetas creadas de 1 al {r}")
numero_rango = elegir_rango()
crear_carpetas(numero_rango)

#n=0
#while n< rango_int:
#    crear_carpetas(rango_int)
#    n +=1
#
