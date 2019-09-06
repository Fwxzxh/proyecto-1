import re

def poly(p, var_string='x'):
    res = ''
    first_pow = len(p) - 1
    for i, coef in enumerate(p):
        power = first_pow - i

        if coef:
            if coef < 0:
                sign, coef = (' - ' if res else '- '), -coef
            elif coef > 0:  # must be true
                sign = (' + ' if res else '')

            str_coef = '' if coef == 1 and power != 0 else str(coef)

            if power == 0:
                str_power = ''
            elif power == 1:
                str_power = var_string
            else:
                str_power = var_string + '^' + str(power)

            res += sign + str_coef + str_power
    return res

read_coef = open("C:\\Archivos\\coeficientes.txt", "r", encoding="utf-8")
get_coef = read_coef.read()
read_coef.close()

temp = re.findall(r'(-?\d*)x', get_coef) + re.findall(r'(-?\d*) ', get_coef) # toma los coeficientes
pot = ("".join(re.findall(r'(\^\d*)', get_coef))).split("^")  # toma las potencias

#arreglamos temp con espacio
for i in range(len(temp)):
    if temp[i] == '' or temp[i] == '-':
        if temp[i] == '':
            temp[i] = 1



potx = re.findall(r'(x\^)', get_coef)
pot1 = re.findall(r'(x\d*)', get_coef)

del pot[0]  # borra un lugar de la lista ocupado por un espacio en blanco
grado = int(pot[0]) + 1   # guardo la primer potencia para poder trabajar con ella
potencias = list(map(int, pot))  # convierte la lista de strings de potencias en lista de ints
coeficientes = list(map(int, temp))  # convierte la lista de strings de coeficientes en lista de ints
print(get_coef)
print(poly(coeficientes))  # mando a llamar la funcion e imprimo el resultado

Bandera = False
if len(pot1) != len(potx):  # agarrar la potencia 1 dek valro x      pot1 numero de x, potx numero de x con un ^
    potencias.append(1)
elif len(pot1) == len(potx) and len(potx)< len(coeficientes) and len(potx)>1:  #si el numero de x y de x^ es igual y el numero de coef es mayor al de potencias
    potencias.append(0)
elif len(pot1) == len(potx) and len(potx)==1:
    print("es una unica x ")
    Bandera = True       # if True es ua sola x y puede (o no) contener algun otro termino

#def Dic
#armamos el dicionario que relaciona coef y potencias
if len(potencias) == len(coeficientes):
    DicCoefPow = dict(zip(potencias, coeficientes))
else:
    potencias.append(0) #agrego un 0 para len(potencias) == len(coeficientes) y que sea posible armar el diccionario
    DicCoefPow = dict(zip(potencias, coeficientes))
    potencias.remove(0) #quito el cero que agregue arriba para que la variable potencias solo tenga las potencias necesarias
    # imprime el diccionario
for key in DicCoefPow:
    print(key, ":", DicCoefPow[key])

#def FixPotencias
# Arregla las potencias ////////////////////////////////(fixpow)
fixpow = []
for cont in range(grado+1):   # desde i en el rango de 0 a la potencia maxima
    if cont in potencias:  # si contador existe en la lista potencias
        fixpow.append(cont)   # a grega count a fixpow
    else:
        fixpow.append(None)
#las dejamos ordenadas sin Nones
fixpow = sorted(set(potencias))
fixpow.reverse()

#armamos fixcoef///////////////////////////////////////(fixcoef)
fixcoef = []
if  Bandera == True:     #si bandera True, agrega un elemento de control a fixpow, para incluir el termino independiente
    if len(coeficientes) > len(potencias): #si el # de Coef es mayor al de potencias ej 3x^2+3
        fixpow.append(0)        #se le agrega un 0 a las potencias para ordenarlas con el diccionario
        for cont in fixpow:
            clave = DicCoefPow.get(cont)
            if clave != None:
                fixcoef.append(clave)
            else:
                fixcoef.append(0)
        fixpow.remove(0)        #se le quita el 0
    elif len(coeficientes) == len(potencias):   #si el # de coef es igual al de potencias ej 2x^3
        for cont in fixpow:
            clave = DicCoefPow.get(cont)
            if clave != None:
                fixcoef.append(clave)
            else:
                fixcoef.append(0)
else:
    for cont in fixpow:
        clave = DicCoefPow.get(cont)
        if clave != None:
            fixcoef.append(clave)
        else:
            fixcoef.append(0)

print(fixpow)
print(fixcoef)
#print(poly(fixcoef))
