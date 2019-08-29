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
pot = ("".join(re.findall(r'(\^\d*)', get_coef))).split("^") # toma las potencias
del pot[0]  # borra un lugar de la lista ocupado por un espacio en blanco
ptnc = pot[0]  # guardo la primer potencia para poder trabajar con ella
potencias = list(map(int, pot))  # convierte la lista de strings de potencias en lista de ints
coeficientes = list(map(int, temp))  # convierte la lista de strings de coeficientes en lista de ints
print(poly(coeficientes))  # mando a llamar la funcion e imprimo el resultado
