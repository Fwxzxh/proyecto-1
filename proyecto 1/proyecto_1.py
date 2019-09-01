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

potx = re.findall(r'(x\^)', get_coef)
pot1 = re.findall(r'(x\d*)', get_coef)

del pot[0]  # borra un lugar de la lista ocupado por un espacio en blanco
grado = int(pot[0]) + 1   # guardo la primer potencia para poder trabajar con ella
potencias = list(map(int, pot))  # convierte la lista de strings de potencias en lista de ints
coeficientes = list(map(int, temp))  # convierte la lista de strings de coeficientes en lista de ints
print(get_coef)
print(poly(coeficientes))  # mando a llamar la funcion e imprimo el resultado

if len(pot1) != len(potx):  # agarrar la potencia 1 dek valro x
    potencias.append(1)
elif len(pot1) == len(potx) and len(pot1)< len(coeficientes):
    potencias.append(0)


# Arregla las potencias
fixpow = []
for cont in range(grado):   # desde i en el rango de 0 a la potencia maxima
    if cont in potencias:  # si contador existe en la lista potencias
        fixpow.append(cont)   # a grega count a fixpow
    else:
        fixpow.append(None)
fixpow.reverse()

#def fixcoef
fixcoef = []
if len(potencias) == len(coeficientes):
    DicCoefPow = dict(zip(potencias, coeficientes))
else:
    potencias.append(0)
    DicCoefPow = dict(zip(potencias, coeficientes))

for cont in fixpow:
    clave = DicCoefPow.get(cont)
    if clave != None:
        fixcoef.append(clave)
    else:
        fixcoef.append(0)

for key in DicCoefPow:
    print(key, ":", DicCoefPow[key])
