import re
import numpy.polynomial.polynomial as poly
import numpy as np
from scipy import optimize


def getcoef():  # recuerda que si no hay termino independiente se le quita el espacio al final de la funcion
    read_coef = open("C:\\Archivos\\coeficientes.txt", "r", encoding="utf-8")
    get_coef = read_coef.read()
    read_coef.close()

    temp = re.findall(r'(-?\d*)x', get_coef) + re.findall(r'(-?\d*) ', get_coef)  # toma los coeficientes
    pot = ("".join(re.findall(r'(\^\d*)', get_coef))).split("^")  # toma las potencias

    # arreglamos temp con espacio
    for i in range(len(temp)):
        if temp[i] == '':
            temp[i] = 1
        elif temp[i] == '-':
            temp[i] == -1
    potx = re.findall(r'(x\^)', get_coef)
    pot1 = re.findall(r'(x\d*)', get_coef)

    global coeficientes

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
    global DicCoefPow
    if len(potencias) == len(coeficientes):
        DicCoefPow = dict(zip(potencias, coeficientes))
    else:
        potencias.append(0)  # agrego un 0 para len(potencias) == len(coeficientes) y que sea posible armar el
        # diccionario
        DicCoefPow = dict(zip(potencias, coeficientes))
        potencias.remove(0)  # quito el cero que agregue arriba para que la variable potencias solo tengapotencias
        # necesaria
    global grado
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


def bisection(a, b):  # funcion de biseccion descargada de internet
    if p(a) * p(b) >= 0:  # si el polinomio evaluado en a*b es mayor o igual a 0
        # print("You have not assumed right a and b\n")   # intervalo invalido
        return
    c = a  # copiamos a en una nueva variable

    while (b - a) >= 0.01:  # mientras b-a esten en un rango aceptable

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

    # print("El valor de la raiz es : ", "%.4f" % c)
    return c  # retornamos el valor de la raiz


# pol= polinimio para div sintetica
# ao = divisor de la div sintetica
# newcoef= aqui se guardan los resultados de la div sintetica (lista)
# residuo= si es 0 es porque se encontro una raiz

def syntheticdiv(dividend, divisor):  # esta funcion hace divison sintetica                                          p
    pol = list(dividend)  # hago el polinomio                                                                        u
    a0 = divisor  # asigno el divisonr                                                                            t
    newcoef = []  # creo el arreglo donde se van a guardar los resultados de la division                          o

    for i in range(len(pol)):  # para cada elemento se hace la divison                                             E
        if i == 0:  # siempre se baja el primer coeficiente en la division por default                              L
            newcoef.append(pol[i])  # aqui se guarda nada mas                                                       I
        elif i < len(pol):  # mientras que no se nos acabe el polinomio                                             U
            newcoef.append((a0 * newcoef[i - 1]) + pol[i])  # se realizan las operacines correspondientes
    residuo = newcoef[-1]  # el residuo es la ultima posicion siempre

    '''m = optimize.newton(p, a0 + 1j, Pder)
    real = round(m.real, 4)
    img = round(m.imag, 4)
    if real not in Iraices and img not in Iraices:
        Iraices.append(round(m.real, 4) + round(m.imag, 4) * 1j)'''

    for count in newcoef:  # por cada elemento en el resultado de la div sintetica
        if count < 0:  # verificamos si es negativo
            n = bisection(a0, a0 + 1)  # si no, mandamos ese divisior y el siguiennte a biseccion
            if flag is True:
                if n is not None:
                    n *= -1

            raices.append(n)  # agregamos a la lista de raices
            #raices.sort()

            break  # nos salimos del ciclo porque ya encontramos la raiz en ese intervalo

    if residuo == 0:  # si encontramos una raiz
        raices.append(a0)  # la agregamos
        print(f'{a0} es una raiz real')

    Fixraices = []
    for i in raices:
        if i is None:
            raices.remove(i)
        else:
            Fixraices.append(i)
        sorted(set(Fixraices))
    return newcoef


def newtonraphson(x):  # funcion de newton-Raphson descargada de internet
    P = p.deriv(1)  # primera derivada del polinomio p guardada en MAYUS p
    h = p(x) / P(x)
    while abs(h) >= 0.0001:
        h = p(x) / P(x)

        # x(i+1) = x(i) - f(x`) / f'(x)
        x = x - h

    # print("El valor de la raiz es : %.4f" % x)
    return x


def pminus():
    for key in DicCoefPow.keys():
        if key % 2 is not 0:
            DicCoefPow[key] *= -1
    Pminusminus = []
    for k in range(grado + 1):
        if DicCoefPow.get(k) in coeficientes * -1 or coeficientes:
            Pminusminus.append(DicCoefPow.get(k))
        else:
            Pminusminus.append(0)
    Pminusminus.reverse()
    pmenos = []

    for j in range(grado + 1):
        if Pminusminus[j] is not None:
            pmenos.append(Pminusminus[j])
        elif Pminusminus[j] is None:
            pmenos.append(0)

    if pmenos[0] < 0:
        for j in range(grado + 1):
            pmenos[j] = (pmenos[j] * -1)

    return pmenos


def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - float(f_value) / dfdx(x)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", x)

        f_value = f(x)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter


def maxminf():
    maximos = []
    minimos = []
    Pinflex = []
    df = p.deriv(1)  # calculamos la primera derivada
    d2f = p.deriv(2)  # calcilamos la segunda derivada
    d3f = p.deriv(3)

    maxmin = np.roots(df)
    for i in range(len(maxmin)):
        if np.polyval(d2f, maxmin[i]) > 0:
            minimos.append(maxmin[i])
        else:
            maximos.append(maxmin[i])
    # puntos de inflecion
    inflex = np.roots(d2f)
    for i in range(len(inflex)):
        if np.polyval(d3f, inflex[i]) != 0:
            Pinflex.append(inflex[i])

    # imprimimos maximos y minimos en intervalos
    for i in range(len(maximos)):
        print(f"Los maximos son ({maximos[i]}, {np.polyval(p, maximos[i])})")
    for i in range(len(minimos)):
        print(f"Los minimos son ({minimos[i]}, {np.polyval(p, minimos[i])})")

    print(f"Los puntos de infleccion son: ")
    for i in range(len(Pinflex)):
        print(f"({i}, {np.polyval(p,i)})")

    print("***Intervalos de crecimiento***")
    # sacamos intervalos de crecimiento y decrecimiento
    for i in maxmin:
            if np.polyval(df, i+1) > 0 and np.polyval(df, i-1) < 0:
                print(f'(Decrece,({i}, {np.polyval(p, i)}), Crece)')
            if np.polyval(df, i + 1) < 0 and np.polyval(df, i - 1) > 0:
                print(f'(Crece,({i}, {np.polyval(p, i)}), Decrece)')
    print("***Intervalos de concavidad***")
    # sacamos intervalos de concavidad
    for i in range(len(Pinflex)):
        if np.polyval(d2f, i+1) < 0 :
            print(f"Es concaba despues de ({i},{np.polyval(p,i)} y convexa antes de ({i},{np.polyval(p,i)})")
        if np.polyval(d2f, i+1) >0:
            print(f"Es Convexa despues de ({i},{np.polyval(p, i)}) y concava antes de ({i},{np.polyval(p, i)}) ")


if __name__ == '__main__':  # función main
    p = np.poly1d(getcoef())  # p es nuestro polinomio, lo obtenemos de los coeficientes de la funcion getcoef()
    print("El polinomio original es:")
    print(f"{p}\n")

    raices = []  # lista con las raices
    Iraices = []  # raices imaginarias
    iraci = []
    Pder = p.deriv(1)
    flag = False
    flag1 = False

    for j in range(-5,5,1):
        m = optimize.newton(p, j+1j, Pder)
        real = round(m.real, 6)
        img = float("{0:.5f}".format(m.imag)) * 1j
        # img = round(m.imag, 4) *1j

        if real not in Iraices:
            Iraices.append(real)

        if img not in iraci:
            iraci.append(img)
            iraci.append(-img)

    for i in range(25):  # asigno el numero de iteraciones de la buscqueda de raices
        syntheticdiv(p, i)  # mando el polinomio y la iteracion a synteticdiv()
    maxminf() #---------------------------
    print("\nTodas las raices son:")
    print(p.r)
    p = np.poly1d(pminus())  # polinomio invertido
    Pder = p.deriv(1)
    flag = True
    flag1 = True

    for i in range(25):
        syntheticdiv(p, i)


    print(f"Las raices reales por Biseccion son: {raices}")
    print(f"Las raices por Newton-Raphson son: {Iraices}")
    print(f"                          {iraci} ")

