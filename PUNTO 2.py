#2.1 Suma de cuadrados del 1 al 100 (adaptación de Reto 6 - punto 1)
def suma_cuadrados(*args):
    return sum(x**2 for x in args)

#2.2 Suma de todos los números impares en un rango (Reto 6 - punto 2 adaptado)
def suma_impares(*args):
    return sum(x for x in args if x % 2 != 0)

#2.3 Mínimo o máximo entre varios números (útil en varios retos)
def minimo(*args):
    return min(args)

def maximo(*args):
    return max(args)