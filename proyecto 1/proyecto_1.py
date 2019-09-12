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
            #if temp[i] == '':
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
    print(f"Dividendo = {dividend}")
    print(f"Divisor = {divisor}")
    print(f'Resultado = {newcoef}')
    print(f'Residuo = {residuo}\n')

    if residuo == 0:
        print(f'{a0} es una raiz real')
    return newcoef


def bisection1(a, b):
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

    print("The value of root is : ", "%.4f" % c)



def bisection(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.
'''
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2


if __name__ == '__main__':
    p = np.poly1d(getcoef())
    print(p)
    a0 = p.coef[-1]
    print(bisection(p,-a0,a0,30))
    bisection1(-a0,a0)
    if p.coef[0] < 0:
        p = (-p)
        a0 = p.coef[-1]
        n = syntheticdiv(p.coef, a0)
        while a0 != 0:
            if all(i >= 0 for i in n):
                a0 -= 1
                # print(a0)
                n = syntheticdiv(p.coef, a0)
            else:
                a0 += 1
                #print(a0)
                n = syntheticdiv(p.coef, a0)
    else:
        a0 = p.coef[-1]
        n = syntheticdiv(p.coef, a0)
        while a0 != 0:
            if all(i >= 0 for i in n):
                a0 -= 1
                # print(a0)
                n = syntheticdiv(p.coef, a0)
            else:
                a0 += 1
                # print(a0)
                n = syntheticdiv(p.coef, a0)

    '''if len(getcoef()) % 2 == 0:
        getcoef()[:1]
    else:
        print(len(getcoef())+1)'''

    a0 = p.coef[-1]
    n = syntheticdiv(p.coef, a0)
    while a0 != 0:
        if all(i >= 0 for i in n):
            a0 -= 1
            # print(a0)
            n = syntheticdiv(p.coef, a0)
        else:
            a0 += 1
            # print(a0)
            n = syntheticdiv(p.coef, a0)