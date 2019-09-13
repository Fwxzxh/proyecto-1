import re
import numpy.polynomial.polynomial as poly
import numpy as np
from scipy import optimize


def getcoef():
    read_coef = open("C:\\Archivos\\coeficientes.txt", "r", encoding="utf-8")
    get_coef = read_coef.read()
    read_coef.close()

    temp = re.findall(r'(-?\d*)x', get_coef) + re.findall(r'(-?\d*) ', get_coef)  # toma los coeficientes
    pot = ("".join(re.findall(r'(\^\d*)', get_coef))).split("^")  # toma las potencias

    # arreglamos temp con espacio
    for i in range(len(temp)):
        if temp[i] == '' or temp[i] == '-':
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
        bandera = True  # if True es ua sola x y puede (o no) contener algun otro termino

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
    for cont in range(grado + 1):
        fixpow.append(cont)
    fixpow.reverse()

    # def fixcoef
    # Arregla los coeficientes /////////////////////////////(fixcoef)
    fixcoef = []
    for i in range(grado + 1):
        if DicCoefPow.get(i) in coeficientes:
            fixcoef.append(DicCoefPow.get(i))
        else:
            fixcoef.append(0)
    fixcoef.reverse()

    return fixcoef


def syntheticdiv(dividend, divisor): # esta funcion hace divison sintetica                                          p
    pol = list(dividend) # hago el polinomio                                                                        u
    ao = divisor    # asigno el divisonr                                                                            t
    newcoef = []    # creo el arreglo donde se van a guardar los resultados de la division                          o
    for i in range(len(pol)):   # para cada elemento se hace la divison                                             E
        if i == 0:  # siempre se baja el primer coeficiente en la division por default                              L
            newcoef.append(pol[i])  # aqui se guarda nada mas                                                       I
        elif i < len(pol):  # mientras que no se nos acabe el polinomio                                             U
            newcoef.append((ao * newcoef[i - 1]) + pol[i])  # se realizan las operacines correspondientes
    residuo = newcoef[-1]   # el residuo es la ultima posicion siempre
    print(f"Dividendo = {dividend}")
    print(f"Divisor = {divisor}")
    print(f'Resultado = {newcoef}')
    print(f'Residuo = {residuo}\n')

    if residuo == 0:
        print(f'{a0} es una raiz real')
    return newcoef


def bisection(a, b):   # funcion de biseccion descargada de internet
    if p(a) * p(b) >= 0:
        print("You have not assumed right a and b\n")
        return
    c = a
    while (b - a) >= 0.01:

        # Find middle point
        c = (a + b) / 2

        # Check if middle point is root
        if p(c) == 0.0:
            break

        # Decide the side to repeat the steps
        if p(c) * p(a) < 0:
            b = c
        else:
            a = c

    print("El valor de la raiz es : ", "%.4f" % c)


def newtonraphson(x): # funcion de newton-Raphson descargada de internet
    P = p.deriv(1)
    h = p(x) / P(x)
    while abs(h) >= 0.0001:
        h = p(x) / P(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("El valor de la raiz es : %.4f" % x)


if __name__ == '__main__':  # función main
    p = np.poly1d(getcoef())    # p es nuestro polinomio, lo obtenemos de los coeficientes de la funcion getcoef()
    print("El polinomio original es:")
    print(f"{p}\n")
    a0 = p.coef[-1]     # a0 es nuestro intervalo mayor
    root = optimize.newton(p, -50, p.deriv(1))  # fucncion de newton encontrada en una libreria (solo encuentra 1 root)
    root1 = optimize.bisect(p, -2, 2)   # funcion de biseccion encontrada en una libreria (solo encuentra un root)
    w = np.roots(p.coef).round(4)   # aqui saco todas las racies haciendo trampa
    for item in w:  # imprimo cada raiz
        print('Las raiz es:', + item)
