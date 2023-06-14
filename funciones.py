import math
grado = 0

def cambiar_grado(g):
    global grado 
    grado = g

def exponencial(x):
    imagen = 0
    for n in range(grado):
        imagen += x**n / math.factorial(n)
    return imagen


def exponencial_decreciente(x):
    imagen = 0
    for n in range(grado):
        imagen += (-x)**n / math.factorial(n)
    return imagen


def seno(x):
    imagen = 0
    for n in range(grado):
        imagen += (-1)**n * x**(2*n+1) / math.factorial(2*n+1)
    return imagen


def coseno(x):
    imagen = 0
    for n in range(grado):
        imagen += (-1)**n * x**(2*n) / math.factorial(2*n)
    return imagen


def senohyp(x):
    imagen = 0
    for n in range(grado):
        imagen += x**(2*n+1) / math.factorial(2*n+1)
    return imagen


def cosenohyp(x):
    imagen = 0
    for n in range(grado):
        imagen += x**(2*n) / math.factorial(2*n)
    return imagen
