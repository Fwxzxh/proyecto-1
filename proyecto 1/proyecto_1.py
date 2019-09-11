import re
import numpy.polynomial.polynomial as poly
import numpy as np


def getcoef():
    read_coef = open("C:\\Archivos\\coeficientes.txt", "r", encoding="utf-8")
    get_coef = read_coef.read()
    read_coef.close()

    temp = re.findall(r'(-?\d*)x', get_coef) + re.findall(r'(-?\d*) ', get_coef) # toma los coeficientes
    pot = ("".join(re.findall(r'(\^\d*)', get_coef))).split("^")  # toma las potencias

    # arreglamos temp con espacio
    for i in range(len(temp)):
        if temp[i] == '' or temp[i] == '-':
            if temp[i] == '':
                temp[i] = 1

    potx = re.findall(r'(x\^)', get_coef)
    pot1 = re.findall(r'(x\d*)', get_coef)

    del pot[0]  # borra un lugar de la lista ocupado por un espacio en blanco
    potencias = list(map(int, pot))  # convierte la lista de strings de potencias en lista de ints
    coeficientes = list(map(int, temp))  # convierte la lista de strings de coeficientes en lista de ints

    bandera = False
    if len(pot1) != len(potx):  # agarrar la potencia 1 dek valro x      pot1 numero de x, potx numero de x con un ^
        potencias.append(1)
    # si el numero de x y de x^ es igual y el numero de coef es mayor al de potencias
    elif len(pot1) == len(potx) and len(coeficientes) > len(potx) > 1:
        potencias.append(0)
    elif len(pot1) == len(potx) and len(potx) == 1:
        print("es una unica x ")
        bandera = True       # if True es ua sola x y puede (o no) contener algun otro termino

    # def Dic
    # armamos el dicionario que relaciona coef y potencias
    if len(potencias) == len(coeficientes):
        DicCoefPow = dict(zip(potencias, coeficientes))
    else:
        potencias.append(0)  # agrego un 0 para len(potencias) == len(coeficientes) y que sea posible armar el
        # diccionario
        DicCoefPow = dict(zip(potencias, coeficientes))
        potencias.remove(0)  # quito el cero que agregue arriba para que la variable potencias solo tengapotencias
        # necesaria

    potencias.sort()
    potencias.reverse()
    grado = potencias[0]

    # def FixPotencias
    # Arregla las potencias ////////////////////////////////(fixpow)
    fixpow = []
    for cont in range(grado+1):
        fixpow.append(cont)
    fixpow.reverse()

    # def fixcoef
    # Arregla los coeficientes /////////////////////////////(fixcoef)
    fixcoef = []
    for i in range(grado+1):
        if DicCoefPow.get(i) in coeficientes:
            fixcoef.append(DicCoefPow.get(i))
        else:
            fixcoef.append(0)
    fixcoef.reverse()

    return fixcoef


def syntheticdiv(dividend, divisor):
    pol = list(dividend)
    ao = divisor
    newcoef = []
    for i in range(len(pol)):
        if i == 0:
            newcoef.append(pol[i])
        elif i < len(pol):
            newcoef.append((ao*newcoef[i-1]) + pol[i])
    residuo = newcoef[-1]
    print(newcoef)
    print(residuo)
    return newcoef


if __name__ == '__main__':
    p = np.poly1d(getcoef())
    a0 = getcoef()[-1]
    print(p.r)
    print(a0)
    n = syntheticdiv(getcoef(), a0)

    while a0 > 0:
        if all(i >= 0 for i in n):
            a0 -= 1
            print(a0)
            n = syntheticdiv(getcoef(), a0)
        elif all(i < 0 for i in n):
            a0 += 1
            print(a0)
            n = syntheticdiv(getcoef(), a0)


