#!/usr/bin/env python
'''
Listas [Python]
Ejercicios de clase
---------------------------
Autor: Johana Rangel
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Johana Rangel"
__email__ = "johanarang@hotmail.com"
__version__ = "1.2"

import math


def practica_listas():
    # 1) Crear una lista que contenga los nùmeros del -5 al 5

    # La lista solicitada es una secuencia numérica ordenada, se puede
    # crear utilizando range

    lista1 = []  # Lista vacia

    # Crear una lista de rango -5 a 5 inclusive

    for numero in range(-5, 6):
        lista1.append(numero)

    print('1:', lista1)

    # 2) Crear una lista que contengo unicamente los nùmeros
    # impares entre -5 y 5

    lista2 = []  # Lista vacia
    # Crear una lista de rango -5 a 5 inclusive de 
    # solo nùmeros impares

    for numero in range(-5, 6):
        if (numero % 2 != 0):
            lista2.append(numero)

    print('2:', lista2)

    # 3) De la lista1 filtrar los números negativos, es decir,
    # crear una lista a partir de lista1 de solo números negativos

    lista3 = []  # Lista vacia
    # Filtrar numeros negativos
    for numero in lista1:
        if numero < 0:
            lista3.append(numero)


    print('3:', lista3)

    # 4) De la lista1 filtrar los números mayores a 2, es decir,
    # crear una lista a partir de lista1 de solo números mayores a 2

    lista4 = []  # Lista vacia
    # Filtrar numeros mayores a 2
    for n in lista1:
        if n > 2:
            lista4.append(n)

    print('4:', lista4)

    # 5) De la lista1 realizar la suma de todos los números

    suma_total = 0
    # Sumar numeros
    
    suma_total = sum(lista1)

    print('5:', suma_total)

    # 6) De la lista1 realizar el modelo, es decir, pasar todos
    # los números a positivo

    lista6 = []  # Lista vacia
    # Aplicar mdulo

    for numero in lista1:
        lista6.append(abs(numero))

    print('6:', lista6)

    # 7) Calcular la suma entre la lista 1 y la lista 6
    # Como son del mismo utilizar len para calcular el largo
    # y recorrer con indices

    lista7 = []  # Lista vacia
    # Sumar listas

    for i in range(len(lista1)):
        suma = lista1[i] + lista6[i]
        lista7.append(suma)
        
    print('7:', lista1)
    print('7:', lista6)
    print('7:', lista7)

    # 8) De la lista1 calcular multiplicar por dos todos los números

    lista8 = []  # Lista vacia
    # Multiplicar por dos
    for numero in lista1:
        lista8.append(numero * 2) #DECIA MULTIPLICAR POR DOS, NO ELEVAR A LA DOS.
    
    print('8:', lista8)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    practica_listas()
